import pandas as pd
import pickle
import sys, os
from styleframe import StyleFrame
from pathlib import Path
from datetime import date


class Vars:
    pass


_v = Vars()
_v.TODAY = str(date.today())
_v.BASEPATH = Path.cwd()
_v.OUTDIR = os.path.dirname(_v.BASEPATH)
_v.PARENT = f"{_v.OUTDIR}/H&S Incomplete Courses/"


def save_faculties_dataframes(faculty_results):
    with open(
        f"{_v.BASEPATH}/data/processed_data/by_faculty/all_faculties_{_v.TODAY}.pkl",
        "wb",
    ) as handle:
        pickle.dump(faculty_results, handle, protocol=pickle.HIGHEST_PROTOCOL)


def check_facultyfolder_exists(faculty_name):
    parent = check_dir(_v.PARENT)
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


def generate_users_list(users):
    parent = check_dir(_v.PARENT)
    outfolder = check_dir(f"{parent}/.ldap_users")
    print(outfolder)
    outfile = f"{outfolder}/active.users_{_v.TODAY}.out"
    try:
        with open(outfile, "w") as fp:
            for username in users:
                fp.write(f"{username}\n")
    except Exception as ex:
        sys.stderr.write("Unable to write to output file: " + str(ex) + "\n")
        sys.exit(2)
