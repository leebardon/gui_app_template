import sys, time, os
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QProgressBar,
    QVBoxLayout,
    QFileDialog,
    QPushButton,
    QMainWindow,
    QDialog,
)
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PySide2.QtWidgets import *
from qt_material import apply_stylesheet

from src.controllers import AnalysisController
from src.views.ui_splash import Ui_SplashScreen
from src.views.ui_start import Ui_Start


class SplashScreen(QMainWindow):
    """Initialises a pyqt5 window. Loads views/ui_setup.py params for elements and style
        Generates cosmetic progressbar and counter, instantiates Start() object
    Args:
        QMainWindow (class): Inherits from QMainWindow base class (PyQt5)
    """

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


class Start(QMainWindow):
    """Instantiates Start screen, loads elements and style from views/ui_start.py
        Binds actions to Start button and Select button
        Launches FileBrowser Dialog to collect paths to Qlikview spreadsheets
        Instantiates Analysis() object and threading functionality
    Args:
        QMainWindow (class): Inherits from QMainWindow base class (PyQt5)
    """

    def __init__(self):
        # super().__init__()
        QMainWindow.__init__(self)
        self.ui = Ui_Start()
        self.ui.setupUi(self)
        self.ui.progress.hide()
        self.ui.start_button.hide()

        # bind filebrowser dialog window to button click
        self.ui.select_button.clicked.connect(self.launch_browser)
        self.ui.start_button.clicked.connect(self.begin_analysis)

    def launch_browser(self):
        FileBrowser()
        self.ui.select_button.hide()
        self.ui.instruction.hide()
        self.ui.start_button.show()
        self.ui.message.move(85, 150)
        self.ui.message.setText(u"<strong> Click to Proceed </strong>")

    def begin_analysis(self):
        self.ui.start_button.hide()
        self.ui.progress.show()
        self.ui.message.setText(u"- program running -")

        # set up thread for analysis
        self.analysis = Analysis()
        self.simulThread = QThread()
        self.analysis.moveToThread(self.simulThread)

        # bind controls to events
        self.analysis.started.connect(self.analysis.run)
        self.analysis.finished.connect(self.analysis_complete)
        self.analysis.completed.connect(self.analysis.stop)

        self.analysis.start()

    def analysis_complete(self):
        self.end_program()

    def end_program(self):
        self.ui.progress.hide()
        self.ui.message.setText("<== Completed ==>")
        time.sleep(2)
        self.ui.message.setText("exiting...")
        time.sleep(2)
        sys.exit()


# NOTE Need to handle error if wrong file type seleted, or if no file is selected
# At present, you can press start even if you cancel out of file browser, and program exits
class Analysis(QThread):
    """Instantiates counter thread for processing calculations
    Args:
        QThread (class): Base class from PyQt5 for emit and collect signal passing
    """

    completed = pyqtSignal()

    def __init__(self, parent=None):
        super(Analysis, self).__init__(parent)
        self.running = True

    def run(self):
        while self.running:
            print("starting analysis")
            AnalysisController.main(TRAINING_RECORDS_PATH, NOT_COMPLETED_PATH)
            print("finished analysis")
            break

        self.completed.emit()

    def stop():
        self.running = False
        print("finished")


class FileBrowser(QDialog):
    """Opens file browser dialog for selecting qlikview excel spreadsheets
        Requires input excel files to be in .xlsx format
        Requires input excel files to contain substrings "record" and "complete"
    Args:
        QDialog (class): Base class from PyQt5
    """

    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 500)
        self.open_filename_dialog()
        self.show()

    # NOTE spreadsheets must be saved in xlsx format - maybe add to Start screen instructions?
    def open_filename_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Please Select Qlikview Spreadsheets",
            "",
            "All Files (*);;Excel Files (*.xlsx)",
            options=options,
        )

        # NOTE error handling not robust, needs attention
        global TRAINING_RECORDS_PATH, NOT_COMPLETED_PATH
        if len(files) == 2:

            for i in range(len(files)):

                if "record" in files[i].lower():
                    TRAINING_RECORDS_PATH = files[i]

                elif "complete" in files[i].lower():
                    NOT_COMPLETED_PATH = files[i]

        else:
            print("Wrong number of files selected: 2 required to proceed.")

        self.close()


if __name__ == "__main__":

    try:
        app = QApplication(sys.argv)
        apply_stylesheet(app, theme="dark_purple.xml")
        window = SplashScreen()
        window.show()
        sys.exit(app.exec_())

    except SystemExit:

        print("Closing Application...")
