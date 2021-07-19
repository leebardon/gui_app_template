import sys
import time
import os
from pathlib import Path
from subprocess import run
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QApplication, QWidget, QProgressBar, QLabel, QFrame, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor, QMovie
from qt_material import apply_stylesheet

from src.views import FileBrowserGui 

basepath = Path(os.path.abspath(__file__)).parents[2]
stylesheets = f"{basepath}/ui_style"



class SplashScreen(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Health & Safety")
        self.setFixedSize(600, 500)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.counter = 0
        self.n = 200 # total instance for loading bar

        self.init_UI()

        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)


    def init_UI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.frame = QFrame()
        layout.addWidget(self.frame)

        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName('LabelTitle')

        # center labels
        self.labelTitle.resize(self.width() - 20, 160)
        self.labelTitle.move(0, 40)
        self.labelTitle.setText("Course Helper")
        self.labelTitle.setAlignment(Qt.AlignCenter)
        self.labelTitle.setFont(QFont('Segoe UI', 25, QFont.Bold))

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 200 - 10, 50)
        self.progressBar.move(100, self.labelTitle.y() + 200)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.n)
        self.progressBar.setValue(20)
        self.progressBar.setStyleSheet(open(f"{stylesheets}/welcome_pbar.css").read())

        self.labelLoading = QLabel(self.frame)
        self.labelLoading.resize(self.width() - 10, 50)
        self.labelLoading.move(0, self.progressBar.y() + 70)
        self.labelLoading.setObjectName('LabelLoading')
        self.labelLoading.setAlignment(Qt.AlignCenter)
        self.labelLoading.setText('loading...')
        self.labelLoading.setFont(QFont('Segoe UI', 15, QFont.DemiBold))



    def loading(self):
        self.progressBar.setValue(self.counter)

        if self.counter == self.n*0.8:
            self.labelTitle.setText("Launching...")

        elif self.counter == self.n:
            time.sleep(1)
            self.timer.stop()
            self.close()

            run(["python", f"{basepath}/src/views/FileBrowserGui.py"])

        self.counter += 2


if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_blue.xml') 
    splash = SplashScreen()
    splash.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')


