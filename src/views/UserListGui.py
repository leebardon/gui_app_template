import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))

import threading
import time
import PySimpleGUI as sg
from pathlib import Path
from subprocess import run

basepath = Path.cwd()


def get_users_thread(window):
    run(["python", f"{basepath}/src/controllers/UsersController.py"])
    window.write_event_value("-THREAD DONE-", "")
    window.close()


def running_thread(window):
    print(" \n This process could take a while....")
    while True:
        window["bar"].Widget["value"] += 5
        time.sleep(0.3)


def get_users(window):
    threading.Thread(target=get_users_thread, args=(window,), daemon=True).start()


def running(window):
    threading.Thread(target=running_thread, args=(window,), daemon=True).start()


def user_list_gui():
    sg.theme("BrightColors")
    sg.set_options(font=("Helvetica", 12))
    progressbar = [
        [sg.ProgressBar(max_value=100, orientation="h", size=(50, 10), key="bar")]
    ]
    outputwin = [[sg.Output(size=(48, 6), key="out")]]
    layout = [
        [sg.Frame(" Progress ", layout=progressbar)],
        [sg.Frame(" Update Active Users  ", layout=outputwin)],
        [sg.Button("Update"), sg.Button("Start")],
    ]

    window = sg.Window("Update Active User List", layout).Finalize()
    window["bar"].Widget.config(mode="indeterminate")
    window["out"].update(" ========= Welcome to Hassle Blaster ========= ")
    print(" \n")
    print(">> 'UPDATE' refreshes active users' list \n ")
    print(">> 'START' launches main program   ")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        elif event == "Update":
            window["out"].update("  -------- Updating Active Users List ---------  \n")
            get_users(window)
            running(window)
            print(" \n ---- DONE ---- ")

        elif event == "-THREAD DONE-":
            window["out"].update(" -------- Launching Main Application -------- ")
            time.sleep(1)
            window.close()
            run(["python", f"{basepath}/src/views/LaunchGui.py"])

        elif event == "Start":
            window["out"].update(" ----------- Starting Main Program ----------- \n")
            time.sleep(2)
            window.close()
            run(["python", f"{basepath}/src/views/LaunchGui.py"])


if __name__ == "__main__":
    user_list_gui()
