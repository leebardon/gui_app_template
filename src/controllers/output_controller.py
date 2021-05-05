from pathlib import Path
import pandas as pd
from xlsx2csv import Xlsx2csv

from src.models import collect_results

basepath = Path.cwd()

course_data = f"{basepath}/data/interim_data/healthandsafety.csv"

not_completed = collect_results.not_completed(course_data)

departments = collect_results.get_departments(not_completed)

department_results = collect_results.results_per_department(departments, not_completed)