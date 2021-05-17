import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))
from pathlib import Path
from subprocess import run

basepath = Path.cwd()

run(["python", f"{basepath}/src/models/GetActiveUsers.py"])
