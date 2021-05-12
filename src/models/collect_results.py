import pandas as pd
import pickle
import os
from pathlib import Path
from datetime import date

global today, basepath
today = str(date.today())
basepath = Path.cwd()
outdir = os.path.dirname(basepath)


def not_completed(course_data):
    return course_data[course_data["Completed"] == "N"]


def get_facs_depts(not_completed):
    return (
        not_completed["Faculty Name"].unique(),
        not_completed["Department Name"].unique(),
    )


def results_by_faculty(facs, not_completed):
    results = {}
    for f in facs:
        _filter = not_completed["Faculty Name"] == f
        results[f] = not_completed[_filter]
    return results


def save_faculties_dataframes(faculty_results):
    with open(
        f"{basepath}/data/processed_data/by_faculty/all_faculties_{today}.pkl", "wb"
    ) as handle:
        pickle.dump(faculty_results, handle, protocol=pickle.HIGHEST_PROTOCOL)


def results_by_department(results_by_faculty):
    for fac_name, fac_df in results_by_faculty.items():
        deps_per_fac = results_by_faculty[fac_name]["Department Name"].unique()
        get_final_results(fac_name, fac_df, deps_per_fac)


def get_final_results(faculty, fac_df, deps_per_fac):
    results = {}
    for d in deps_per_fac:
        _filter = fac_df["Department Name"] == d
        results[d] = fac_df[_filter]
    generate_outputs(faculty, results)


def generate_outputs(faculty_name, results_dict):
    folderpath = check_facultyfolder_exists(faculty_name)
    for department, dataframe in results_dict.items():
        dataframe.to_excel(f"{folderpath}/{department}_{today}.xlsx")


def check_facultyfolder_exists(faculty_name):
    facultyfolder = f"{outdir}/H&S Incomplete Courses/{faculty_name}"
    if not os.path.exists(facultyfolder):
        os.mkdir(facultyfolder)
    return facultyfolder


# def check_facultyfolder_exists(path):
#     if not os.path.exists(path):
#         os.mkdir(path)
