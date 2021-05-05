# data from excel is converted to into and date where relevant 
# bulk data from blackboard is parsed to extract id details
import pandas as pd

def csv_to_df(csv_path):

    return pd.read_csv(
        csv_path,
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
    } )   

def remove_dash(course_str_data):
    return course_str_data.replace({'-': None}, inplace=True)


def convert_datetime(course_data):
    cols_to_convert = ["Date Subscribed", "Date Started", "Last Score Date"]
    return convert_cols(cols_to_convert, course_data)


def convert_cols(cols_to_convert, course_data):
    for col in cols_to_convert:
        course_data[col] = course_data[col].apply(pd.to_datetime, errors='coerce')
    return course_data