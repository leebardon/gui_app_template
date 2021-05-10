import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))

import PySimpleGUI as sg
import time


def working(task_list, i, done_message=""):
    sg.theme("DarkTeal2")
    progressbar = [
        [sg.ProgressBar(5, orientation='h', size=(51, 10), key='progressbar')]
    ]
    outputwin = [
        [sg.Output(size=(600, 150))]
    ]
    layout = [
        [sg.Frame('Progress',layout= progressbar)],
        [sg.Frame('Output', layout = outputwin)]
    ]
    window = sg.Window('Custom Progress Meter', layout).Finalize()
    progress_bar = window['progressbar']

    print(task_list[i])
    progress_bar.UpdateBar(i, len(task_list))

    if i == (len(task_list) - 1):
        print(f"{done_message}")
        window.close()


