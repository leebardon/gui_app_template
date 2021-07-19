import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot
from PyQt5.QtWidgets import  QDialog, QLabel, QFrame, QApplication, QPushButton, QWidget, QHBoxLayout, QProgressBar, QVBoxLayout
from qt_material import apply_stylesheet

# from src.controllers import AnalysisController 

class MainWindow(QWidget):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.window_width, self.window_height = 600, 500
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("Widget")
        self.h_box = QHBoxLayout(self)
        self.start_button = QPushButton("Start")
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
        # jobs = False
        # jobs = AC.main('pathpath')

        # if jobs == True:
        print('working')
        time.sleep(3)
        print('still working')
        time.sleep(3)
        print('done')
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
		apply_stylesheet(app, theme='dark_blue.xml')
		main_window = MainWindow()
		sys.exit(app.exec_())







# TIME_LIMIT = 100

# class External(QThread):
#     """
#     Runs a counter thread.
#     """
#     countChanged = pyqtSignal(int)

#     def run(self):
#         count = 0
#         while count < TIME_LIMIT:
#             count +=1
#             time.sleep(1)
#             self.countChanged.emit(count)

# class Actions(QDialog):
#     """
#     Simple dialog that consists of a Progress Bar and a Button.
#     Clicking on the button results in the start of a timer and
#     updates the progress bar.
#     """
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Progress Bar')
#         self.progress = QProgressBar(self)
#         self.progress.setGeometry(0, 0, 300, 25)
#         self.progress.setMaximum(100)
#         self.button = QPushButton('Start', self)
#         self.button.move(0, 30)
#         self.show()

#         self.button.clicked.connect(self.onButtonClick)

#     def onButtonClick(self):
#         self.calc = External()
#         self.calc.countChanged.connect(self.onCountChanged)
#         self.calc.start()

#     def onCountChanged(self, value):
#         self.progress.setValue(value)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Actions()
#     sys.exit(app.exec_())
