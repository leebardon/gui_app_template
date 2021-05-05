import pandas as pd


def not_completed(course_data):
    return course_data[course_data["Completed"]=="N"]


def get_departments(not_completed):
    return not_completed["Department Name"].unique()


def results_per_department(departments, not_completed):
    department_results = {}
    for d in departments:    
        department_results[d] = not_completed[not_completed["Department Name"] == d]
    return department_results