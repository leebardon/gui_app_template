from subprocess import run
import os
from pathlib import Path
import subprocess


basepath = Path(os.path.abspath(__file__)).parents[0]
# subprocess.call(f"{basepath}/src/controllers/GuiController.py")
# maybe conditional in here - if ldap userlist > 30 days, launch user update gui

run(["python", f"{basepath}/src/controllers/GuiController.py"])

# run(["python", f"{basepath}/src/models/collect_results.py"])

# if __name__ == "__main__":
#     UserListGui.main()
