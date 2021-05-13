import os, sys
from subprocess import run
from pathlib import Path


sys.path.insert(0, os.path.abspath("."))
basepath = Path(os.path.abspath(__file__)).parents[0]


run(["python", f"{basepath}/src/views/launch_gui.py"])

# run(["python", f"{basepath}/src/models/collect_results.py"])
