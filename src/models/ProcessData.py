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


def excel_to_csv(T_RECORDS_PATH, NOT_COMPLETED_PATH):
    """Converts excels spreadsheet to csv for improved processing speed
        Currently proceeds only if conversion has not been done for the current day...
    Args:
        T_RECORDS_PATH (path): To student_training_records.xlsx
        NOT_COMPLETED_PATH (path): To not_completed.xlsx
    Returns:
        [type]: [description]
    """
    TR_csv_path = (
        f"{_v.BASEPATH}/data/interim_data/interim-training-records-{_v.TODAY}.csv"
    )
    NC_csv_path = (
        f"{_v.BASEPATH}/data/interim_data/interim-incomplete-courses-{_v.TODAY}.csv"
    )

    for p in [TR_csv_path, NC_csv_path]:
        for data in [T_RECORDS_PATH, NOT_COMPLETED_PATH]:
            if not os.path.exists(p):
                Xlsx2csv(data, outputencoding="utf-8").convert(p)

    return TR_csv_path, NC_csv_path


def csv_to_df(TR_csv, NC_csv):
    """Converts csv to pandas dataframe for processing
    Args:
        TR_csv (csv file): Training records csv
        NC_csv (csv file): Non complete csv
    """
    return map(lambda x: pd.read_csv(x, converters=StringConverter()), [TR_csv, NC_csv])


def remove_dash(*dfs):
    """ Converts dash to Nonetype to enable further processing """
    out = []
    for df in dfs:
        df.replace({"-": None}, inplace=True)
        out.append(df)

    return [df for df in out]


# NOTE not sure if below functions needed anymore
# def convert_datetime(course_data):
#     cols_to_convert = ["Date Subscribed", "Date Started", "Last Score Date"]
#     return convert_cols(cols_to_convert, course_data)


# def convert_cols(cols_to_convert, course_data):
#     for col in cols_to_convert:
#         course_data[col] = course_data[col].apply(pd.to_datetime, errors="coerce")
#     return course_data


def df_to_csv(tr_interim, nc_interim):
    """Saves processed dataframes as interim csv files
    Args:
        tr_interim (pandas dataframe): Training records df
        nc_interim (pandas dataframe): Training records df
    """
    tr_interim.to_csv(
        f"{_v.BASEPATH}/data/processed_data/all/training-records-{_v.TODAY}.csv"
    )
    nc_interim.to_csv(
        f"{_v.BASEPATH}/data/processed_data/all/incomplete-courses-{_v.TODAY}.csv"
    )
