import pandas as pd
import pickle
import os
from glob import glob
from styleframe import StyleFrame
from pathlib import Path
from datetime import date
from src.models import Save


class Vars:
    pass


_v = Vars()
_v.TODAY = str(date.today())
_v.BASEPATH = Path.cwd()
_v.OUTDIR = os.path.dirname(_v.BASEPATH)
_v.LDAP = f"{_v.OUTDIR}/H&S Incomplete Courses/.ldap_users"


# def not_completed(course_data):
#     return course_data[course_data["Completed"] == "N"]


def get_faculties_list(not_completed):
    """ Returns all unique faculty names in spreadsheet """

    return not_completed["Faculty Name"].unique()


def results_by_faculty(facs, not_completed):
    """ Returns dict of faculty: dataframe by unique faculty name """
    results = {}
    for f in facs:
        _filter = not_completed["Faculty Name"] == f
        results[f] = not_completed[_filter]

    return results


def process_outputs(results_by_faculty, spreadsheet_name):
    """For each faculty, finds all unique departments
    Calls get_final_results()
    Calls generate_csv_files()
    If processing Training Records spreadsheet:
            calls get_DSE_over_40() to generate 'DSE greater than 40' spreadsheets
    """
    for faculty_name, faculty_df in results_by_faculty.items():
        deps_in_faculty = results_by_faculty[faculty_name]["Department Name"].unique()
        results_dict = get_final_results(faculty_name, faculty_df, deps_in_faculty)
        generate_csv_files(faculty_name, results_dict, spreadsheet_name)

        if spreadsheet_name == "-TRAINING-RECORD-":
            dse_over_40 = get_DSE_over_40(results_dict)
            generate_csv_files(faculty_name, dse_over_40, "-DSE-GREATER-THAN-40%-")


def get_DSE_over_40(results_dict):
    """ Filters out instances of individuals self assment of DSE being >= 40% """
    dse_over_40 = {}

    for department, dataframe in results_dict.items():
        new_cols = [
            "Last Name",
            "First Name",
            "ID",
            "User Type",
            "Faculty Name",
            "Department Name",
            "Display Screen Equipment -  User Self Assessment",
        ]
        new_df = dataframe[new_cols]

        dse = ["Display Screen Equipment -  User Self Assessment"]
        pd.options.mode.chained_assignment = None
        new_df[dse] = new_df[dse].apply(pd.to_numeric, errors="coerce")
        over_40_df = new_df[new_df[dse].values >= 40]

        dse_over_40[department] = over_40_df

    return dse_over_40


def get_final_results(faculty, fac_df, deps_in_faculty):
    """ Generates dicts of department: dataframe """
    results = {}
    for dep in deps_in_faculty:
        _filter = fac_df["Department Name"] == dep
        results[dep] = fac_df[_filter]

    return results


def generate_csv_files(faculty_name, results_dict, spreadsheet_name):
    """ Produce 'Non-Completed', 'Training Records', 'DSE over 40' spreadsheets  """
    fac_path = Save.check_facultyfolder_exists(faculty_name)

    for department, dataframe in results_dict.items():
        dep_path = Save.check_dir(f"{fac_path}/{department}")
        filepath = f"{dep_path}/{department}{spreadsheet_name}{_v.TODAY}.xlsx"
        Save.save_to_excel(dataframe, filepath)
