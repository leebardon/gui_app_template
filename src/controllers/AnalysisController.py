
from src.models import ParseData
from src.models import ParseData, GenerateResults, Save


def main(datapath):

    raw_csv = ParseData.excel_to_csv(datapath)

    raw_dataframe = ParseData.csv_to_df(raw_csv)
    breakpoint()
    interim_dataframe = ParseData.remove_dash(raw_dataframe)

    ParseData.df_to_csv(interim_dataframe)

    incomplete_all = GenerateResults.not_completed(interim_dataframe)

    active_users = GenerateResults.get_ldap_users_list()

    not_completed = GenerateResults.remove_inactive(incomplete_all, active_users)

    faculties = GenerateResults.get_faculties_list(not_completed)

    faculty_results = GenerateResults.results_by_faculty(faculties, not_completed)

    Save.save_faculties_dataframes(faculty_results)

    GenerateResults.results_by_department(faculty_results)




# if __name__ == "__main__":
#     main_analysis(datapath)