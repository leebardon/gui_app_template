
from src.models import ParseData
from src.models import ParseData, GenerateResults, Save
import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot
from PyQt5.QtWidgets import  QDialog, QLabel, QFrame, QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout, QProgressBar, QVBoxLayout
from qt_material import apply_stylesheet, QtStyleTools

# from src.views.LaunchGui import MainWindow



class Analysis(QWidget):
    def __init__(self, data):
        super().__init__()
        vbox = QVBoxLayout()
        MainLabel= QLabel("My Window")
        vbox.addWidget(MainLabel)
        self.show()
        # self.layout() is MainLayoutHbox
        # self.layout().addLayout(vbox)
        breakpoint()



def main(self, app, layout, datapath):

    self.show()
    time.sleep(2)
    for i in reversed(range(layout.count())): 
        layout.itemAt(i).widget().setParent(None)

    # apply_stylesheet(app, theme='dark_blue.xml')
    self.show()
    time.sleep(2)
    breakpoint()



    
#     print("new anal controller!")
#     time.sleep(2)
#     # breakpoint()
#     # self.hide()
#     # sys.exit(app.exec_())
#     app.quit()

    # raw_csv = ParseData.excel_to_csv(datapath)
    # raw_dataframe = ParseData.csv_to_df(raw_csv)
    # interim_dataframe = ParseData.remove_dash(raw_dataframe)
    # ParseData.df_to_csv(interim_dataframe)
    # incomplete_all = GenerateResults.not_completed(interim_dataframe)
    # active_users = GenerateResults.get_ldap_users_list()
    # not_completed = GenerateResults.remove_inactive(incomplete_all, active_users)
    # faculties = GenerateResults.get_faculties_list(not_completed)
    # faculty_results = GenerateResults.results_by_faculty(faculties, not_completed)
    # Save.save_faculties_dataframes(faculty_results)
    # GenerateResults.results_by_department(faculty_results)


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setFixedSize(600, 500)
#         # self.main = QUiLoader()
#         # self.apply_stylesheet(self.main, theme='dark_blue.xml') 
#         # self.window_width, self.window_height = 600, 500
#         # self.setMinimumSize(self.window_width, self.window_height)
#         self.setWindowTitle("Run Analysis")
#         # self.h_box = QHBoxLayout(self)
#         self.start_button = QPushButton("Start")
#         # self.popup = PopUpProgressBar()  # Creating an instance instead as an attribute instead of creating one 
#         # # everytime the button is pressed 
#         # self.start_button.clicked.connect(self.popup.start_progress)  # To (re)start the progress
#         # self.addWidget(self.start_button)
#         # self.setLayout(self.h_box)
#         self.show()
      


# class Worker(QObject):
#     finished = pyqtSignal()
#     intReady = pyqtSignal(int)

#     @pyqtSlot()
#     def run_tasks(self):  # A slot takes no params
#         # jobs = False
#         # jobs = AC.main('pathpath')

#         # if jobs == True:
#         print('working -', DATAPATH)
#         time.sleep(3)
#         print('still working')
#         time.sleep(3)
#         print('done')
#         self.finished.emit()


# class PopUpProgressBar(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.pbar = QProgressBar(self)
#         self.pbar.setGeometry(30, 40, 500, 75)
#         self.pbar.setMinimum(0)
#         self.pbar.setMaximum(0)
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.pbar)
#         self.setLayout(self.layout)
#         self.setGeometry(300, 300, 550, 100)
#         self.setWindowTitle('Progress Bar')

#         self.obj = Worker()
#         self.thread = QThread()
#         self.obj.intReady.connect(self.on_count_changed)
#         self.obj.moveToThread(self.thread)
#         self.obj.finished.connect(self.thread.quit)
#         self.obj.finished.connect(self.hide)  # To hide the progress bar after the progress is completed
#         self.thread.started.connect(self.obj.run_tasks)


#     def start_progress(self): 
#         breakpoint() # To restart the progress every time
#         self.show()
#         self.thread.start()

#     def on_count_changed(self, value):
#         self.pbar.setValue(value)




# if __name__ == "__main__":
#     main_analysis(datapath)