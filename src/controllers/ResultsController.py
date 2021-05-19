import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import time as t
from src.models import ParseData
from src.models import ParseData, CollectResults, Save
from src.views import ProgressGui as pg

import pandas as pd


def generate_results():

    processed_course_data = ParseData.return_dataframe()

    pg.progress_gui(processed_course_data, "results", " Analysing Data ")


if __name__ == "__main__":
    generate_results()
