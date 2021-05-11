import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import PySimpleGUI as sg
import time
from src.models import parse_data
from src.controllers import output_controller
from src.views import progress_gui as pbar

 
def get_and_convert_data(datapath):
    # bar = pb.Progressbar(1, 5, "converting excel to csv")
    # bar.progress_gui()
    tasks = pbar.Tasks(1, 5, "starting")
    pbar.launch_pb2(tasks := tasks)
    # raw_csv = parse_data.excel_to_csv(datapath)

    # bar = pb.Progressbar(2, 5)
    tasks.update(message="building raw dataframe")
    tasks.update(message="task2")
    tasks.update(message="task3")
    tasks.update(message="task4e")
    tasks.update(message="task5")
    # raw_dataframe = parse_data.csv_to_df(raw_csv)

    # bar = pb.Progressbar(3, 5)
    # bar.update_progress("cleaning data for analysis")
    # interim_dataframe = parse_data.remove_dash(raw_dataframe)

    # bar = pb.Progressbar(4, 5)
    # bar.update_progress("converting strings to DateTime objects")
    # processed_dataframe = parse_data.convert_datetime(interim_dataframe)

    # bar = pb.Progressbar(5, 5)
    # bar.update_progress(" -- saving processed dataframe -- ")
    # parse_data.df_to_csv(processed_dataframe)

    # output_controller.generate_results(processed_dataframe)


def task_list():
    task_list = [
        "Converting excel file to csv...",
        "Reading into dataframe...",
        "Replacing dashes with 'None'...",
        "Converting data strings to DateTime objects...",
        "Saving processed data to csv...",
    ]
    return task_list
