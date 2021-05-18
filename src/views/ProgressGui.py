import PySimpleGUI as sg
import time


def progress_gui(num_tasks, windowtype):
    sg.theme("BrightColors")
    sg.set_options(font=("Helvetica", 14))
    progressbar = [
        [sg.ProgressBar(num_tasks, orientation="h", size=(46, 10), key="progressbar")]
    ]
    outputwin = [[sg.Output(size=(44, 6))]]
    layout = [
        [sg.Frame("  Progress  ", layout=progressbar)],
        [sg.Frame("Output", layout=outputwin, key="message")],
    ]
    window = sg.Window(windowtype, layout).Finalize()
    progress_bar = window["progressbar"]

    return window, progress_bar


def update(window, progress_bar, current, total, message):
    if current == 1:
        print(f" ------- Total Number of Tasks = {total} -------")

    progress_bar.UpdateBar(current, total)
    window.FindElement("message").Update(message)
    print(f"Processing task number {current}")
    time.sleep(2)

    if current == total:
        time.sleep(2)
        window.close()
