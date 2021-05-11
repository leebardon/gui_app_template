import pandas as pd
import pickle
from pathlib import Path
from datetime import date

global today, basepath
today = str(date.today())
basepath = Path.cwd()


def not_completed(course_data):
    return course_data[course_data["Completed"] == "N"]


def get_departments(not_completed):
    return not_completed["Department Name"].unique()


def results_per_department(departments, not_completed):
    department_results = {}
    for d in departments:
        department_results[d] = not_completed[not_completed["Department Name"] == d]
    return department_results


def save_all_dept_results(department_results):
    with open(f"{basepath}/results/all_dept_incomplete_{today}.pkl", "wb") as handle:
        pickle.dump(department_results, handle, protocol=pickle.HIGHEST_PROTOCOL)
