import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))

import PySimpleGUI as sg
from src.controllers import data_controller as dc


def launch_gui():

    sg.theme("DarkTeal2")
    layout = [
        [sg.T("")],
        [sg.Text("Qlikview Excel File: "), sg.Input(), sg.FileBrowse(key="-IN-")],
        [sg.Button("Select")],
        [sg.Button("Exit")],
    ]
    window = sg.Window("H&S Courses - Incomplete", layout, size=(600, 150))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            break
        elif event == "Select":
            datapath = values["-IN-"]
            dc.get_and_convert_data(datapath)


if __name__ == "__main__":
    launch_gui()
        

