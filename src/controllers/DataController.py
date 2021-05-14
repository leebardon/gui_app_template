import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import time as t
from src.models import ParseData
from src.controllers import OutputController
from src.views import ProgressGui as pbar


def get_and_convert_data(datapath):
    tasks = 6
    window, bar = pbar.progress_gui(tasks, "Preparing Data...")

    pbar.update(window, bar, 1, tasks, task_list(1))
    raw_csv = ParseData.excel_to_csv(datapath)
    t.sleep(2)

    pbar.update(window, bar, 2, tasks, task_list(2))
    raw_dataframe = ParseData.csv_to_df(raw_csv)
    t.sleep(2)

    pbar.update(window, bar, 3, tasks, task_list(3))
    interim_dataframe = ParseData.remove_dash(raw_dataframe)
    t.sleep(2)

    pbar.update(window, bar, 4, tasks, task_list(4))
    processed_dataframe = ParseData.convert_datetime(interim_dataframe)
    t.sleep(2)

    pbar.update(window, bar, 5, tasks, task_list(5))
    ParseData.df_to_csv(processed_dataframe)
    t.sleep(2)

    pbar.update(window, bar, 6, tasks, task_list(6))
    OutputController.generate_results(processed_dataframe)


def task_list(i):
    task_list = [
        " >> Converting excel file to csv...  ",
        " >> Reading into dataframe...  ",
        " >> Cleaning data for analysis...  ",
        " >> Working...  ",
        " >> Saving processed data to csv...  ",
        " >> Preparing to generate results...  ",
    ]
    return task_list[i - 1]
