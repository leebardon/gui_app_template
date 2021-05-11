import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))

import PySimpleGUI as sg
import time

class Progressbar:

    def __init__(self, i, j, message):
        self._task = i
        self._maxtasks = j
        self._message = message

    def progress_gui(self):
        sg.theme("DarkTeal2")
        progressbar = [
            [sg.ProgressBar(self._maxtasks, orientation="h", size=(51, 10), key="progressbar")]
        ]
        outputwin = [[sg.Output(size=(50, 8))]]
        layout = [
            [sg.Frame("Progress", layout=progressbar)],
            [sg.Frame("Output", layout=outputwin)],
        ]
        window = sg.Window("Program Running...", layout).Finalize()
        progress_bar = window["progressbar"]

        progress_bar.UpdateBar(self._task, self._maxtasks)
        window.update_idletasks()
        print(self._message)
        time.sleep(5)

    @property
    def update_progress(self, message):
        self._task += 1
        self._message += "/n" + message 
        self.progress_gui


# print(task_list[i])
# progress_bar.UpdateBar(i, len(task_list))

# if i == (len(task_list) - 1):
#     print(f"{done_message}")
#     window.close()
# if __name__ == '__main__':
#     Progressbar()