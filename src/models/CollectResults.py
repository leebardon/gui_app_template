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


def not_completed(course_data):
    return course_data[course_data["Completed"] == "N"]


def get_ldap_users_list():
    users = glob(os.path.join(f"{_v.LDAP}/", "*.out"))[0]
    return pd.read_csv(users, names=["Username"])


def remove_inactive(incomplete_all, active_users):
    return incomplete_all[incomplete_all["Username"].isin(active_users["Username"])]


def get_faculties_list(not_completed):
    return not_completed["Faculty Name"].unique()


def results_by_faculty(facs, not_completed):
    results = {}
    for f in facs:
        _filter = not_completed["Faculty Name"] == f
        results[f] = not_completed[_filter]
    return results


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
    fac_path = Save.check_facultyfolder_exists(faculty_name)

    for department, dataframe in results_dict.items():
        dep_path = Save.check_dir(f"{fac_path}/{department}")
        filepath = f"{dep_path}/{_v.TODAY}.xlsx"
        Save.save_to_excel(dataframe, filepath)
