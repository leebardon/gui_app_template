import sys, time, os
from pathlib import Path
from subprocess import run
from PyQt5.QtWidgets import (QPushButton, QHBoxLayout, QApplication, QWidget, QProgressBar, QLabel, 
QFrame, QVBoxLayout, QFileDialog, QVBoxLayout, QPushButton, QMainWindow, QDialog)
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, QObject, pyqtSlot
from PyQt5.QtGui import QFont, QColor
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from qt_material import apply_stylesheet

from src.controllers import AnalysisController
from src.models import ParseData, GenerateResults, Save
from ui_setup.ui_splash import Ui_SplashScreen

basepath = Path(os.path.abspath(__file__)).parents[2]
stylesheets = f"{basepath}/ui_setup"



class SplashScreen(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        # set UI from ui_setup
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        # loading progressbar timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)


    def loading(self):
        self.ui.progressBar.setValue(self.ui.counter)

        if self.ui.counter < self.ui.counter_max:
            self.ui.counter += 2

        else:
            self.timer.stop()
            self.close()
            self.launch = Start()
            self.launch.show()



class Start(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Health & Safety")
        self.setFixedSize(600, 500)
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 500, 75)
        self.pbar.setMinimum(0)
        self.pbar.setMaximum(0)
        self.select_button = QPushButton("Select Spreadsheet")
        self.start_button = QPushButton("Start")

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.pbar)
        layout.addWidget(self.select_button)
        layout.addWidget(self.start_button)
        self.pbar.hide()
        self.start_button.hide()

        self.select_button.clicked.connect(self.launch_browser)


    def launch_browser(self):
        FileBrowser()
     
        apply_stylesheet(app, theme='dark_blue.xml') 
        time.sleep(1)
        self.start_tasks()
        # self.close()


    def start_tasks(self):
        self.select_button.clear()

        self.start_button.setCheckable(True)
        self.start_button.toggle()
        self.start_button.show()


        # if self.start_button.clicked.connect(self.run_tasks):
        if self.start_button.isChecked():
            self.start_button.hide()
            self.pbar.show()
            self.run_tasks()



    def run_tasks(self):

        time.sleep(3)
        breakpoint()
        raw_csv = ParseData.excel_to_csv(FILE)
        raw_dataframe = ParseData.csv_to_df(raw_csv)
        breakpoint()
        interim_dataframe = ParseData.remove_dash(raw_dataframe)
        ParseData.df_to_csv(interim_dataframe)
        incomplete_all = GenerateResults.not_completed(interim_dataframe)
        active_users = GenerateResults.get_ldap_users_list()
        not_completed = GenerateResults.remove_inactive(incomplete_all, active_users)
        faculties = GenerateResults.get_faculties_list(not_completed)
        faculty_results = GenerateResults.results_by_faculty(faculties, not_completed)
        Save.save_faculties_dataframes(faculty_results)
        GenerateResults.results_by_department(faculty_results)
            



class FileBrowser(QDialog):

    def __init__(self):
        super().__init__()
        apply_stylesheet(app, theme='light_cyan_500.xml',  invert_secondary=True) 
        self.setFixedSize(600, 500)
        self.open_filename_dialog()     
        self.show()

    @pyqtSlot(str)
    def open_filename_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Please Select Qlikview Spreadsheet", "","All Files (*);;Excel Files (*.xlsx)", options=options)
        
        if file_name:
            global FILE
            FILE = file_name
            return
            # self.close()
    





if __name__ == '__main__':
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    try: 
        # extra = open(f"{stylesheets}/launch.css").read()
        app = QApplication(sys.argv)
        apply_stylesheet(app, theme='dark_blue.xml') 
        stylesheet = app.styleSheet()

        with open(f"{stylesheets}/launch.css") as file:
            app.setStyleSheet(stylesheet + file.read())

        window = SplashScreen()
        window.show()
        sys.exit(app.exec_())

    except SystemExit:
        print('Closing Window...')


