from pathlib import Path
import pandas as pd
from xlsx2csv import Xlsx2csv

from src.models import parse_data

basepath = Path.cwd()
xlsx_path = f"{basepath}/data/healthandsafety.xlsx"
csv_save = f"{basepath}/data/healthandsafety.csv"
Xlsx2csv(xlsx_path, outputencoding="utf-8").convert(csv_save)


course_str_data = pd.read_csv(f"{basepath}/data/healthandsafety.csv")
course_data_no_dash = parse_data.remove_dash(course_str_data)
course_data = parse_data.convert_datetime(course_data_no_dash)



# course_data = parse_data.convert_dates(course_str_data)





