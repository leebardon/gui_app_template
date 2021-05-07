import os, sys
from subprocess import run
from pathlib import Path
from src.controllers import data_controller

sys.path.insert(0, os.path.abspath("."))
basepath = Path(os.path.abspath(__file__)).parents[0]

run(['python', f"{basepath}/src/controllers/data_controller.py"])