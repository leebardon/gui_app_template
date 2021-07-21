import sys, time, os
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QVBoxLayout, QFileDialog, QPushButton, QMainWindow, QDialog
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PySide2.QtWidgets import *
from qt_material import apply_stylesheet

from src.controllers import AnalysisController
from src.models import ParseData, GenerateResults, Save
from src.views.ui_splash import Ui_SplashScreen


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
        self.progress = QProgressBar(self)
        self.progress.setGeometry(30, 40, 500, 75)
        self.progress.setMinimum(0)
        self.progress.setMaximum(0)
        self.select_button = QPushButton("Select Spreadsheet")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.progress)
        self.layout.addWidget(self.select_button)
        self.progress.hide()

        # bind filebrowser dialog window to button click
        self.select_button.clicked.connect(self.launch_browser)


    def launch_browser(self):
        FileBrowser()
        self.select_button.hide()

        # bind controls to events
        self.start_button = QPushButton("Start")
        self.layout.addWidget(self.start_button)
        self.start_button.clicked.connect(self.begin_analysis)   


    def begin_analysis(self):
        self.start_button.hide()
        self.progress.show()

        # set up thread for analysis
        self.analysis = Analysis()
        self.simulThread = QThread()

        self.analysis.moveToThread(self.simulThread)
        self.analysis.started.connect(self.analysis.run)
        self.analysis.finished.connect(self.analysis_complete)

        self.analysis.completed.connect(self.analysis.stop)
        self.analysis.start()


    def analysis_complete(self):
        print('Im done :D')
        self.progress.hide()
        

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


class Analysis(QThread):
    """
    Runs a counter thread for processing calculations
    """
    completed = pyqtSignal()

    def __init__(self, parent=None):
        super(Analysis, self).__init__(parent)
        self.running = True


    def run(self):
        while self.running:
            print("doing stuff")
            time.sleep(1)
            print("doing more stuff")
            time.sleep(2)
            print("done")
            break

        self.completed.emit()


    def stop():
        print('finished stuff')
        self.running = False

        

class FileBrowser(QDialog):

    def __init__(self):
        super().__init__()
        # apply_stylesheet(app, theme='light_cyan_500.xml',  invert_secondary=True) 
        self.setFixedSize(600, 500)
        self.open_filename_dialog()     
        self.show()

    # @pyqtSlot(str)
    def open_filename_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Please Select Qlikview Spreadsheet", "","All Files (*);;Excel Files (*.xlsx)", options=options)
        
        if file_name:
            global FILE
            FILE = file_name
            # apply_stylesheet(app, theme='dark_blue.xml') 
            # return
            self.close()
            # time.sleep(3)
    





if __name__ == '__main__':
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    try: 
        # extra = open(f"{stylesheets}/launch.css").read()
        app = QApplication(sys.argv)
        apply_stylesheet(app, theme='dark_blue.xml') 
        # stylesheet = app.styleSheet()

        # with open(f"{stylesheets}/launch.css") as file:
        #     app.setStyleSheet(stylesheet + file.read())

        window = SplashScreen()
        window.show()
        sys.exit(app.exec_())

    except SystemExit:
        print('Closing Window...')
