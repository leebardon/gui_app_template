import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))

import PySimpleGUI as sg
from src.controllers import DataController as dc
from src.views import ProgressGui as pg


def file_browser_gui():
    sg.theme("DefaultNoMoreNagging")
    layout = [
        [sg.T("")],
        [sg.Text("Qlikview Excel File: "), sg.Input(), sg.FileBrowse(key="-IN-")],
        [sg.T("")],
        [sg.Button("Select"), sg.Button("Exit")],
    ]
    window = sg.Window(" Qlikview Data ", layout, size=(500, 120))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            break
        elif event == "Select":
            datapath = values["-IN-"]
            window.close()
            dc.get_and_convert_data(datapath)


if __name__ == "__main__":
    file_browser_gui()
