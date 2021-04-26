import pandas as pd

def get_dataframe_from_worksheet(workbook, worksheet_name):
    """returns a pandas dataframe from an excel worksheet"""
    return pd.read_excel(workbook, sheet_name=worksheet_name, dtype=str)
    


if __name__ == "__main__":
    #TODO Load workbook as xlrd
    workbook = None
    worksheet_name = "TEST_DATASET_1"
    get_dataframe_from_worksheet(workbook, worksheet_name)