import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import time as t
from src.models import CollectResults, Save
from src.views import ProgressGui as pbar

import pandas as pd


def generate_results(course_data):
    tasks = 8
    window, bar = pbar.progress_gui(tasks, "Generating Results...")

    pbar.update(window, bar, 1, tasks, task_list(1))
    incomplete_all = CollectResults.not_completed(course_data)
    t.sleep(2)

    pbar.update(window, bar, 2, tasks, task_list(2))
    active_users = CollectResults.get_ldap_users_list()
    t.sleep(2)

    pbar.update(window, bar, 3, tasks, task_list(2))
    not_completed = CollectResults.remove_inactive(incomplete_all, active_users)
    t.sleep(2)

    pbar.update(window, bar, 4, tasks, task_list(2))
    faculties = CollectResults.get_faculties_list(not_completed)
    t.sleep(2)

    pbar.update(window, bar, 5, tasks, task_list(3))
    faculty_results = CollectResults.results_by_faculty(faculties, not_completed)
    t.sleep(2)

    pbar.update(window, bar, 6, tasks, task_list(4))
    Save.save_faculties_dataframes(faculty_results)
    t.sleep(2)

    pbar.update(window, bar, 7, tasks, task_list(5))
    CollectResults.results_by_department(faculty_results)
    t.sleep(2)

    pbar.update(window, bar, 8, tasks, task_list(6))


def task_list(i):
    task_list = [
        " >> Gathering non-completed course data...  ",
        " >> Gathering currently active users list... ",
        " >> Removing inactive users from course data... ",
        " >> Obtaining Faculty & Dept. data...  ",
        " >> Organising results by Faculty & Dept...  ",
        " >> Generating spreadsheets...  ",
        " >> Saving results...  ",
        " -------------------- DONE ---------------------- ",
    ]
    return task_list[i - 1]
