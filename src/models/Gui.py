import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))

import PySimpleGUI as sg
import threading
import time
import pandas as pd
import PySimpleGUI as sg
from datetime import date
from pathlib import Path
from subprocess import run
from src.models import ParseData, CollectResults, Save


TODAY = str(date.today())
BASEPATH = Path.cwd()
DATAPATH = f"{BASEPATH}/data/processed_data"


def progress_gui_settings(window_message):
    sg.theme("DefaultNoMoreNagging")
    sg.set_options(font=("Helvetica", 12))
    progressbar = [
        [sg.ProgressBar(max_value=100, orientation="h", size=(50, 10), key="bar")]
    ]
    outputwin = [[sg.Output(size=(48, 6), key="out")]]
    layout = [
        [sg.Frame(" Progress ", layout=progressbar)],
        [sg.Frame(" Output ", layout=outputwin)],
        [sg.Button("Start")],
    ]
    window = sg.Window(window_message, layout).Finalize()
    window["bar"].Widget.config(mode="indeterminate")

    return window


def user_list_gui_settings(window_message):
    sg.theme("DefaultNoMoreNagging")
    sg.set_options(font=("Helvetica", 12))
    progressbar = [
        [sg.ProgressBar(max_value=100, orientation="h", size=(50, 10), key="bar")]
    ]
    outputwin = [[sg.Output(size=(48, 6), key="out")]]
    layout = [
        [sg.Frame(" Progress ", layout=progressbar)],
        [sg.Frame(" Output ", layout=outputwin)],
        [sg.Button("Update"), sg.Button("Start")],
    ]
    window = sg.Window(window_message, layout).Finalize()
    window["bar"].Widget.config(mode="indeterminate")

    return window


def analysis_tasks_thread(window, datapath):
    message = update_message(1)
    window["out"].update(message)
    raw_csv = ParseData.excel_to_csv(datapath)
    time.sleep(2)

    message = update_message(2)
    window["out"].update(message)
    raw_dataframe = ParseData.csv_to_df(raw_csv)
    time.sleep(2)

    message = update_message(3)
    window["out"].update(message)
    interim_dataframe = ParseData.remove_dash(raw_dataframe)
    time.sleep(2)
    # update_message(window, 4)
    # processed_dataframe = ParseData.convert_datetime(interim_dataframe)
    message = update_message(4)
    window["out"].update(message)
    ParseData.df_to_csv(interim_dataframe)
    time.sleep(2)
    
    message = update_message(5)
    window["out"].update(message)
    time.sleep(2)

    window.write_event_value("-THREAD DONE-", "")
    window.close()


def results_tasks_thread(window, processed_course_data):
    message = update_message(6)
    window["out"].update(message)
    incomplete_all = CollectResults.not_completed(processed_course_data)
    time.sleep(2)

    message = update_message(7)
    window["out"].update(message)
    active_users = CollectResults.get_ldap_users_list()
    time.sleep(2)

    message = update_message(8)
    window["out"].update(message)
    not_completed = CollectResults.remove_inactive(incomplete_all, active_users)
    time.sleep(2)

    message = update_message(9)
    window["out"].update(message)
    faculties = CollectResults.get_faculties_list(not_completed)
    time.sleep(2)

    message = update_message(10)
    window["out"].update(message)
    faculty_results = CollectResults.results_by_faculty(faculties, not_completed)
    time.sleep(2)

    Save.save_faculties_dataframes(faculty_results)

    message = update_message(11)
    window["out"].update(message)
    CollectResults.results_by_department(faculty_results)

    window.write_event_value("-THREAD DONE-", "")
    window.close()


def progressbar_thread(window):
    while True:
        window["bar"].Widget["value"] += 2
        time.sleep(0.1)


def analysis_tasks(window, data):
    threading.Thread(
        target=analysis_tasks_thread, args=(window, data), daemon=True
    ).start()


def results_tasks(window, data):
    threading.Thread(
        target=results_tasks_thread, args=(window, data), daemon=True
    ).start()


def run_progressbar(window):
    threading.Thread(target=progressbar_thread, args=(window,), daemon=True).start()


def update_message(i):
    task_list = [
        "\n >> Converting excel file to csv...  ",
        "\n >> Reading into dataframe...  ",
        "\n >> Cleaning data for analysis...  ",
        # "\n >> Converting strings to datetimes...   ",
        "\n >> Saving processed data to csv...  ",
        "\n >> Preparing to generate results...  ",
        "\n >> Gathering non-completed course data...  ",
        "\n >> Gathering currently active users list... ",
        "\n >> Removing inactive users from course data... ",
        "\n >> Obtaining Faculty & Dept. data...  ",
        "\n >> Organising results by Faculty & Dept...  ",
        "\n >> Generating spreadsheets...  ",
    ]
    return task_list[i-1]
