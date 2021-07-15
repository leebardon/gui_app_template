import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import time as t
from src.views import ProgressGui as pg


def get_and_convert_data(datapath):

    pg.progress_gui(datapath, "analysis", " Analysing Data ")
