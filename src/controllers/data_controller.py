import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))

from src.models import parse_data
from src.controllers import output_controller

def get_and_convert_data(datapath):
    raw_csv = parse_data.excel_to_csv(datapath)
    raw_dataframe = parse_data.csv_to_df(raw_csv)
    interim_dataframe = parse_data.remove_dash(raw_dataframe)
    processed_dataframe = parse_data.convert_datetime(interim_dataframe)
    parse_data.df_to_csv(processed_dataframe)
    
    output_controller.generate_results(processed_dataframe)





