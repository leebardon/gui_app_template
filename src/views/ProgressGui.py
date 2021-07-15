import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))

import threading
import time
import sys
import PySimpleGUI as sg
from pathlib import Path
from subprocess import run
from src.models import ParseData
from src.models import Gui as gui

basepath = Path.cwd()


def progress_gui(data, task_type, window_message):
    window = gui.progress_gui_settings(window_message)

    if task_type == "analysis":
        print("\n >> Click 'START' to analyse data  ")
        analysis_event_loop(window, data)
        window.close()

    elif task_type == "results":
        print("\n >> Click 'START' to generate results  ")
        results_event_loop(window, data)
        window.close()


def analysis_event_loop(window, datapath):
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            # sys.exit(0)
            break
        elif event == "Start":
            gui.analysis_tasks(window, datapath)
            gui.run_progressbar(window)
        elif event == "-THREAD DONE-":
            time.sleep(2)
            print(" \n\n >> Generating Results ..... ")
            run(["python", f"{basepath}/src/controllers/ResultsController.py"])


def results_event_loop(window, course_data):
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == "Start":
            gui.results_tasks(window, course_data)
            gui.run_progressbar(window)
        elif event == "-THREAD DONE-":
            window["out"].update(" ------------- Program Finished ------------- ")
            time.sleep(1)
            window.close()
