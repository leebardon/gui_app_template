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
    TR_csv = f"{_v.BASEPATH}/data/interim_data/interim-training-records-{_v.TODAY}.csv"
    NC_csv = f"{_v.BASEPATH}/data/interim_data/interim-incomplete-courses-{_v.TODAY}.csv"

    for csv in [TR_csv, NC_csv]:
        for data in [T_RECORDS_PATH, NOT_COMPLETED_PATH]:
            if not os.path.exists(csv):
                Xlsx2csv(data, outputencoding="utf-8").convert(csv)

    return TR_csv, NC_csv



def csv_to_df(TR_csv, NC_csv):
    return map(lambda x: pd.read_csv(x, converters=StringConverter()), [TR_csv, NC_csv])


def remove_dash(*dfs):
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
    tr_interim.to_csv(
        f"{_v.BASEPATH}/data/processed_data/all/training-records-{_v.TODAY}.csv"
    )
    nc_interim.to_csv(
        f"{_v.BASEPATH}/data/processed_data/all/incomplete-courses-{_v.TODAY}.csv"
    )

# def return_dataframe():
#     return pd.read_csv(
#         f"{_v.BASEPATH}/data/processed_data/all/incomplete-courses-{_v.TODAY}.csv"
#     )
