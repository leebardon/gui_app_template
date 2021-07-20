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


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):

        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(600, 500)

        self.centralwidget = QWidget(SplashScreen)
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

        # Main title settings
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.resize(430, 200)
        self.label_title.move(75, 40)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(30)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 150, 661, 31))
        self.label_description.move(-55, 180)
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description.setAlignment(Qt.AlignCenter)

        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 280, 561, 23))
        self.progressBar.resize(600 - 180, 35)
        self.progressBar.move(80, 320)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
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
        self.progressBar.setValue(24)

        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 320, 661, 31))
        self.label_loading.move(60, 380)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)

        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_loading.setAlignment(Qt.AlignCenter)

        self.counter = 0
        self.counter_max = 200

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)


    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        SplashScreen.setWindowFlag(Qt.FramelessWindowHint)
        SplashScreen.setAttribute(Qt.WA_TranslucentBackground)
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<strong>Course Helper</strong>", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u" = Health & Safety =", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))

        # if SplashScreen.objectName():
        #     SplashScreen.setObjectName(u"SplashScreen")

        # # SplashScreen.resize(680, 400)
        # layout = QVBoxLayout()
        # # self.setLayout(layout)
        # # self.frame = QFrame()
        # # layout.addWidget(self.frame)
        # SplashScreen.setFixedSize(600, 500)
        # # self.setWindowTitle("Health & Safety")
        # # self.setFixedSize(600, 500)
        # SplashScreen.setWindowFlag(Qt.FramelessWindowHint)
        # SplashScreen.setAttribute(Qt.WA_TranslucentBackground)
        # self.counter = 0
        # self.counter_max = 200

        # self.labelTitle = QLabel()
        # self.labelTitle.setObjectName(u'labelTitle')
        # self.labelTitle.resize(400, 160)
        # self.labelTitle.move(80, 40)
        # self.labelTitle.setText("Course Helper")
        # self.labelTitle.setAlignment(Qt.AlignCenter)
        # self.labelTitle.setFont(QFont('Segoe UI', 28, QFont.Bold))

        # self.labelSubTitle = QLabel()
        # self.labelSubTitle.setObjectName(u'labelSubTitle')
        # self.labelSubTitle.resize(400, 160)
        # self.labelSubTitle.move(80, 95)
        # self.labelSubTitle.setText("== Health & Safety ==")
        # self.labelSubTitle.setAlignment(Qt.AlignCenter)
        # self.labelSubTitle.setFont(QFont('Segoe UI', 12))

        # self.progressBar = QProgressBar()
        # self.progressBar.setObjectName(u'progressBar')
        # self.progressBar.resize(600 - 205, 45)
        # # self.progressBar.resize(self.width() - 205, 45)
        # self.progressBar.move(90, self.labelTitle.y() + 250)
        # self.progressBar.setAlignment(Qt.AlignCenter)
        # self.progressBar.setFormat('%p%')
        # self.progressBar.setTextVisible(True)
        # self.progressBar.setRange(0, self.counter_max)
        # self.progressBar.setValue(20)

        # self.labelLoading = QLabel()
        # # self.labelLoading.resize(self.width() - 10, 50)
        # self.labelLoading.resize(600 - 10, 50)
        # self.labelLoading.move(-5, self.progressBar.y() + 70)
        # self.labelLoading.setObjectName(u'labelLoading')
        # self.labelLoading.setAlignment(Qt.AlignCenter)
        # self.labelLoading.setText('loading...')
        # self.labelLoading.setFont(QFont('Segoe UI', 12))

        # QMetaObject.connectSlotsByName()