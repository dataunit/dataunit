import pandas as pd

def get_dataframe_from_worksheet(workbook, worksheet_name):
    """returns a pandas dataframe from an excel worksheet"""
    return pd.read_excel(workbook, sheet_name=worksheet_name)
    


if __name__ == "__main__":

    get_dataframe_from_worksheet()