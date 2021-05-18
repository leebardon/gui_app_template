import os, sys
from subprocess import run
from pathlib import Path


sys.path.insert(0, os.path.abspath("."))
basepath = Path(os.path.abspath(__file__)).parents[0]

# maybe conditional in here - if ldap userlist > 30 days, launch user update gui

run(["python", f"{basepath}/src/views/UserListGui.py"])

# run(["python", f"{basepath}/src/models/collect_results.py"])
