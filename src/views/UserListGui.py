import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))

import threading
import time
import PySimpleGUI as sg
from pathlib import Path
from subprocess import run
from src.models import Gui as gui

basepath = Path.cwd()


def get_users_thread(window):
    run(["python", f"{basepath}/src/controllers/UsersController.py"])
    window.write_event_value("-THREAD DONE-", "")
    window.close()


def running_thread(window):
    print(" \n This process could take a while....")
    while True:
        window["bar"].Widget["value"] += 3
        time.sleep(0.15)


def get_users(window):
    threading.Thread(target=get_users_thread, args=(window,), daemon=True).start()


def running(window):
    threading.Thread(target=running_thread, args=(window,), daemon=True).start()


def user_list_gui():
    window = gui.user_list_gui_settings(" H&S Course Completion Analyser ")
    window["out"].update(" ========= Welcome to Hassle Blaster ========= ")
    print(" \n")
    print(" >> 'UPDATE' refreshes active users' list \n ")
    print(" >> 'START' launches main program   ")

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break

        elif event == "Update":
            window["out"].update("  -------- Updating Active Users List ---------  \n")
            get_users(window)
            running(window)
            print(" \n ---- DONE ---- ")

        elif event == "-THREAD DONE-":
            time.sleep(1)
            window.close()
            run(["python", f"{basepath}/src/views/FileBrowserGui.py"])

        elif event == "Start":
            window["out"].update(" -------- Launching Main Application -------- ")
            time.sleep(1)
            window.close()
            run(["python", f"{basepath}/src/views/FileBrowserGui.py"])


if __name__ == "__main__":
    user_list_gui()
