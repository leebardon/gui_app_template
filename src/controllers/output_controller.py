import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))
from src.models import collect_results


def generate_results(course_data):
    not_completed = collect_results.not_completed(course_data)
    departments = collect_results.get_departments(not_completed)
    department_results = collect_results.results_per_department(
        departments, not_completed
    )
    collect_results.save_all_dept_results(department_results)
