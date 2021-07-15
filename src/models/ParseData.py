import pandas as pd
import os
from pathlib import Path
from xlsx2csv import Xlsx2csv
from datetime import date


class Vars:
    pass


_v = Vars()
_v.TODAY = str(date.today())
_v.BASEPATH = Path.cwd()


class StringConverter(dict):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return str

    def get(self, default=None):
        return str


def excel_to_csv(datapath):
    csv = f"{_v.BASEPATH}/data/interim_data/raw-incomplete-courses-{_v.TODAY}.csv"
    if not os.path.exists(csv):
        Xlsx2csv(datapath, outputencoding="utf-8").convert(csv)
    return csv


def csv_to_df(csv_path):
    return pd.read_csv(csv_path, converters=StringConverter())


def remove_dash(course_str_data):
    course_str_data.replace({"-": None}, inplace=True)
    return course_str_data


def convert_datetime(course_data):
    cols_to_convert = ["Date Subscribed", "Date Started", "Last Score Date"]
    return convert_cols(cols_to_convert, course_data)


def convert_cols(cols_to_convert, course_data):
    for col in cols_to_convert:
        course_data[col] = course_data[col].apply(pd.to_datetime, errors="coerce")
    return course_data


def df_to_csv(processed_dataframe):
    processed_dataframe.to_csv(
        f"{_v.BASEPATH}/data/processed_data/all/incomplete-courses-{_v.TODAY}.csv"
    )


def return_dataframe():
    return pd.read_csv(
        f"{_v.BASEPATH}/data/processed_data/all/incomplete-courses-{_v.TODAY}.csv"
    )
