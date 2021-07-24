import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot
from PyQt5.QtWidgets import (
    QDialog,
    QLabel,
    QFrame,
    QMainWindow,
    QApplication,
    QPushButton,
    QWidget,
    QHBoxLayout,
    QProgressBar,
    QVBoxLayout,
)
from qt_material import apply_stylesheet, QtStyleTools


from src.models import ProcessData, GenerateResults, Save


def main(T_RECORDS_PATH, NOT_COMPLETED_PATH):

    # convert to csv for speed, then to pandas dataframe
    TR_csv, NC_csv = ProcessData.excel_to_csv(T_RECORDS_PATH, NOT_COMPLETED_PATH)
    TR_df, NC_df = ProcessData.csv_to_df(TR_csv, NC_csv)

    # clean data and save as interim csv
    TR_interim, NC_interim = ProcessData.remove_dash(*[TR_df, NC_df])
    ProcessData.df_to_csv(TR_interim, NC_interim)

    ###################################
    ### 'NOT COMPLETED' SPREADSHEET ###
    ###################################

    # sort results by faculty
    faculties_nc = GenerateResults.get_faculties_list(NC_interim)
    faculty_results_nc = GenerateResults.results_by_faculty(faculties_nc, NC_interim)

    # save sorted results
    Save.save_faculties_dataframes(faculty_results_nc)

    # Final processing and generating output dirs, subdirs and csv's
    GenerateResults.process_outputs(faculty_results_nc, "-NOT-COMPLETED-")

    ######################################
    ### 'TRAINING RECORDS' SPREADSHEET ###
    ###              &                 ###
    ###  'DSE OVER 40%' SPREADSHEET    ###
    ######################################
    faculties_tr = GenerateResults.get_faculties_list(TR_interim)
    faculty_results_tr = GenerateResults.results_by_faculty(faculties_tr, TR_interim)

    # save sorted results
    Save.save_faculties_dataframes(faculty_results_tr)

    # Final processing and generating output dirs, subdirs and csv's
    # process_outputs() has a subprocess for generating 'dse over 40' spreadsheet
    GenerateResults.process_outputs(faculty_results_tr, "-TRAINING-RECORD-")

    return
