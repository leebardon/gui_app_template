import pandas as pd
import pickle
import os
from styleframe import StyleFrame
from pathlib import Path
from datetime import date

global today, basepath
today = str(date.today())
basepath = Path.cwd()
outdir = os.path.dirname(basepath)


def not_completed(course_data):
    return course_data[course_data["Completed"] == "N"]


def get_faculties_list(not_completed):
    return not_completed["Faculty Name"].unique()


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
    fac_path = check_facultyfolder_exists(faculty_name)

    for department, dataframe in results_dict.items():
        dep_path = check_dir(f"{fac_path}/{department}")
        filepath = f"{dep_path}/{today}.xlsx"
        save_to_excel(dataframe, filepath)


def check_facultyfolder_exists(faculty_name):
    parent = check_dir(f"{outdir}/H&S Incomplete Courses/")
    fac_path = check_dir(f"{parent}/{faculty_name}")
    return fac_path


def check_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def save_to_excel(df, filepath):
    columns = df.columns.values.tolist()
    excel_writer = StyleFrame.ExcelWriter(filepath)
    sf = StyleFrame(df)
    sf.set_column_width(columns, width=17)
    sf.to_excel(excel_writer=excel_writer,)
    excel_writer.save()


# if __name__ == '__main__':
#     basepath = Path.cwd()
#     outdir = os.path.dirname(basepath)
#     save_to_excel("", "")
