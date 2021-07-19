import sys, time
from src.models import ParseData, GenerateResults, Save
# from src.controllers import AnalysisController
# from src.views import ProgressGui
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QFrame, QHBoxLayout, QProgressBar, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot


class FileBrowser(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Please Select Qlikview Spreadsheet'
        self.setFixedSize(600, 500)
        self.setWindowTitle(self.title) 
        self.open_filename_dialog()     
        self.show()
    
    @pyqtSlot(str)
    def open_filename_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Please Select Qlikview Spreadsheet", "","All Files (*);;Excel Files (*.xlsx)", options=options)
        
        if file_name:
            global DATAPATH 
            DATAPATH = file_name
            self.close()
            main_window = MainWindow()
            sys.exit(app.exec_())
            

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 600, 500
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("Widget")
        self.h_box = QHBoxLayout(self)
        self.start_button = QPushButton("Start Analysis")
        self.popup = PopUpProgressBar()  # Creating an instance instead as an attribute instead of creating one 
        # everytime the button is pressed 
        self.start_button.clicked.connect(self.popup.start_progress)  # To (re)start the progress
        self.h_box.addWidget(self.start_button)
        self.setLayout(self.h_box)
        self.show()


class Worker(QObject):
    finished = pyqtSignal()
    intReady = pyqtSignal(int)

    @pyqtSlot()
    def run_tasks(self):  # A slot takes no params

        # AnalysisController.main_analysis(DATAPATH)
        
        raw_csv = ParseData.excel_to_csv(DATAPATH)
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
        self.finished.emit()


class PopUpProgressBar(QWidget):

    def __init__(self):
        super().__init__()
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 500, 75)
        self.pbar.setMinimum(0)
        self.pbar.setMaximum(0)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pbar)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 550, 100)
        self.setWindowTitle('Progress Bar')

        self.obj = Worker()
        self.thread = QThread()
        self.obj.intReady.connect(self.on_count_changed)
        self.obj.moveToThread(self.thread)
        self.obj.finished.connect(self.thread.quit)
        self.obj.finished.connect(self.hide)  # To hide the progress bar after the progress is completed
        self.thread.started.connect(self.obj.run_tasks)


    def start_progress(self):  # To restart the progress every time
        self.show()
        self.thread.start()

    def on_count_changed(self, value):
        self.pbar.setValue(value)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileBrowser()
    sys.exit(app.exec_())

