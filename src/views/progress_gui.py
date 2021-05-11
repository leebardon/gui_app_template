import PySimpleGUI as sg
import time
import threading
from multiprocessing import Process


class Tasks:
    def __init__(self, i, j, message):
        self._tasknum = i
        self._maxtasks = j
        self._message = message

    def update(self, message):
        self._tasknum += 1
        self._message = message

    def get_current_vals(self):
        return self._tasknum, self._maxtasks, self._message


def launch_pb2(tasks):

    print(tasks)
    global tasknum, message
    tasknum, message = tasks._tasknum, tasks._message

    sg.theme("DarkTeal2")
    progressbar = [
        [
            sg.ProgressBar(
                tasks._maxtasks, orientation="h", size=(51, 10), key="progress_1"
            )
        ]
    ]
    outputwin = [[sg.Output(size=(50, 8))]]
    layout = [
        [sg.Frame("Progress", layout=progressbar)],
        [sg.Frame("Output", layout=outputwin)],
    ]

    main_window = sg.Window("Program running...", layout, finalize=True)
    main_window["progress_1"].update(tasknum)

    window, event, values = sg.read_all_windows()
    print(f"event: {event}, value: {values[event]}")

    # threading.Thread(
    #     target=update_progress, args=(main_window, tasks := tasks), daemon=True
    # ).start()

    while True:
        window, event, values = sg.read_all_windows()
        print(f"event: {event}, value: {values[event]}")
        if event == "Exit":
            break
        if event.startswith("update_"):
            print(f"event: {event}, value: {values[event]}")
            key_to_update = event[len("update_") :]
            window[key_to_update].update(values[event])
            window.refresh()
            continue
    window.close()


def update_progress(window, tasks):
    tasknum, maxtasks, message = tasks.get_current_vals()
    window.write_event_value("update_progress_1", tasknum)
    # print(message)
    while tasknum < maxtasks:
        print(message)
        # window.write_event_value('update_progress_1', tasknum)
        time.sleep(2)
        update_progress(window, tasks := tasks)


# if __name__ == '__main__':
#     print("fuck")
#     bar = Tasks(1, 1, "starting")
