import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))

import pandas as pd
import PySimpleGUI as sg
from xlsx2csv import Xlsx2csv
from pathlib import Path
from datetime import date
from src.models import parse_data

basepath = Path.cwd()


def get_and_convert_data(gui):
    today = str(date.today())
    csv_save = f"{basepath}/data/interim_data/incomplete-courses-{today}.csv"
    Xlsx2csv(gui.datapath, outputencoding="utf-8").convert(csv_save)

    course_str_data = pd.read_csv(f"{basepath}/data/interim_data/incomplete-courses-{today}.csv")
    course_data_no_dash = parse_data.remove_dash(course_str_data)
    course_data = parse_data.convert_datetime(course_data_no_dash)


class Data:
    def __init__(self, path):
        self.path = path


class Gui:
    def __init__(self):
        sg.theme("DarkTeal2")
        layout = [[sg.T("")], 
                [sg.Text("Qlikview Excel File: "), sg.Input(), sg.FileBrowse(key="-IN-")],
                [sg.Button("Select")],
                [sg.Button("Exit")]]

        window = sg.Window('H&S Courses - Incomplete', layout, size=(600,150))
    
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event=="Exit":
                break
            elif event == "Select":
                data = Data(values["-IN-"])


if __name__ == "__main__":
    new Gui()
    print(Data.path)
    get_and_convert_data(gui.datapath)





