from PyQt5.QtWidgets import (QPushButton, QHBoxLayout, QApplication, QWidget, QProgressBar, QLabel, 
QFrame, QVBoxLayout, QFileDialog, QVBoxLayout, QPushButton, QMainWindow, QDialog)
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, QObject, pyqtSlot, QMetaObject
from PyQt5.QtGui import QFont, QColor

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Start(object):
    def setupUi(self, Start):

        if Start.objectName():
            Start.setObjectName(u"Start")
        Start.resize(600, 500)

        self.centralwidget = QWidget(Start)
        self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)

        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
        "	background-color: rgb(56, 58, 89);	\n"
        "	color: rgb(220, 220, 220);\n"
        "	border-radius: 10px;\n"
        "}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)

        self.message = QLabel(self.dropShadowFrame)
        self.message.setObjectName(u"message")
        # self.message.resize(430, 200)
        self.message.move(85, 40)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(20)
        self.message.setFont(font)
        self.message.setStyleSheet(u"color: rgb(230, 251, 255);")
        self.message.setAlignment(Qt.AlignCenter)

        # Main title settings
        self.instruction = QLabel(self.dropShadowFrame)
        self.instruction.setObjectName(u"instruction")
        self.instruction.resize(430, 240)
        self.instruction.move(75, 90)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(11)
        self.instruction.setFont(font)
        self.instruction.setStyleSheet(u"color: rgb(230, 251, 255);")
        self.instruction.setAlignment(Qt.AlignCenter)


        self.progress = QProgressBar(self.dropShadowFrame)
        self.progress.setObjectName(u"progress")
        self.progress.setGeometry(QRect(50, 280, 561, 23))
        self.progress.resize(600 - 180, 35)
        self.progress.move(80, 320)
        self.progress.setStyleSheet(u"QprogressBar {\n"
        "	\n"
        "	background-color: rgb(98, 114, 164);\n"
        "	color: rgb(200, 200, 200);\n"
        "	border-style: none;\n"
        "	border-radius: 10px;\n"
        "	text-align: center;\n"
        "}\n"
        "QProgressBar::chunk{\n"
        "	border-radius: 10px;\n"
        "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
        "}")
        self.progress.setValue(24)
        self.progress.setMinimum(0)
        self.progress.setMaximum(0)

        self.select_button = QPushButton(self.dropShadowFrame)
        self.select_button.setObjectName(u"select_button")
        self.select_button.resize(200, 100)
        self.select_button.move(190, 310)
        self.select_button.setStyleSheet(u"QPushButton {\n"
        "	\n"
        # "	background-color: rgb(98, 114, 164);\n"
        "	color: rgb(255, 255, 255);\n"
        "	border-style: solid;\n"
        "	border-radius: 18px;\n"
        "	text-align: center;\n"
        "}")

        self.start_button = QPushButton(self.dropShadowFrame)
        self.start_button.setObjectName(u"start_button")
        self.start_button.resize(200, 100)
        self.start_button.move(190, 310)
        self.start_button.setStyleSheet(u"QPushButton {\n"
        "	\n"
        # "	background-color: rgb(98, 114, 164);\n"
        "	color: rgb(255, 255, 255);\n"
        "	border-style: solid;\n"
        "	border-radius: 18px;\n"
        "	text-align: center;\n"
        "}")


        self.verticalLayout.addWidget(self.dropShadowFrame)

        Start.setCentralWidget(self.centralwidget)

        self.retranslateUi(Start)

        QMetaObject.connectSlotsByName(Start)


    def retranslateUi(self, Start):
        Start.setWindowTitle(QCoreApplication.translate("Start", u"MainWindow", None))
        Start.setWindowFlag(Qt.FramelessWindowHint)
        Start.setAttribute(Qt.WA_TranslucentBackground)
        self.message.setText(QCoreApplication.translate("Start", u"<strong>Select Spreadsheets</strong>", None))
        self.instruction.setText(QCoreApplication.translate("Start", u"= Student Training Records =\n  \n= Not Completed =  \n\n\n [Hold ctrl & click to add both]" , None))
        self.select_button.setText(QCoreApplication.translate("Start", u"Select .xlsx Files", None))
        self.start_button.setText(QCoreApplication.translate("Start", u"Start", None))
