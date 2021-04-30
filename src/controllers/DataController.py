import pandas as pd
from pathlib import Path
from xlsx2csv import Xlsx2csv

basepath = Path.cwd()

data_xls = f"{basepath}/data/healthandsafety.xlsx"
data_csv = f"{basepath}/data/healthandsafety.csv"
Xlsx2csv(data_xls, outputencoding="utf-8").convert(data_csv)

# create funtion in parse_data.py to do this ?
course_data = pd.read_csv(
    data_csv,
    dtype={
        "Name": str,
        "Last Name": str,
        "First Name": str,
        "Username": str,
        "ID": str,
        "User Type": str,
        "Faculty Name": str,
        "Department Name": str,
        "Date Subscribed": str,
        "Course Quiz Item": str,
        "Highest Score": str,
        "Date Started": str,
        "Highest Score Date": str,
        "Last Score": str,
        "Last Score Date": str,
        "Completed": str,
    },
)
