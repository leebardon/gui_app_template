import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import PySimpleGUI as sg
import time
from src.models import parse_data
from src.controllers import output_controller
from src.views import working_gui


def get_and_convert_data(datapath):
    working_gui.working(task_list, i=0)
    raw_csv = parse_data.excel_to_csv(datapath)

    working_gui.working(task_list, i=1)
    raw_dataframe = parse_data.csv_to_df(raw_csv)

    working_gui.working(task_list, i=2)
    interim_dataframe = parse_data.remove_dash(raw_dataframe)

    working_gui.working(task_list, i=3)
    processed_dataframe = parse_data.convert_datetime(interim_dataframe)

    working_gui.working(task_list, i=4)
    parse_data.df_to_csv(processed_dataframe)

    output_controller.generate_results(processed_dataframe)


def task_list():
    task_list = [
        "Converting excel file to csv...",
        "Reading into dataframe...",
        "Replacing dashes with 'None'...",
        "Converting data strings to DateTime objects...",
        "Saving processed data to csv..."
    ]
    return task_list
