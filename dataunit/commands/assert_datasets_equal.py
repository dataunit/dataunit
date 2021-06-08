from dataunit.commands.base import DataUnitCommand
from dataunit.context import Context
from dataunit.excel.dataframe_utils import get_dataframe_from_worksheet
import pandas as pd

class AssertDatasetsEqualCommand(DataUnitCommand):
    """
    Class for the command that asserts two datasets are equal, 
    should raise an exception if they are not equal
    """
    command_name = "Assert Datasets Equal"

    def __init__(self, workbook_path, workbook, settings, expected_dataset, expected_dataset_type, actual_dataset, actual_dataset_type):
        self.workbook_path = workbook_path
        self.workbook = workbook
        self.settings = settings
        self.expected_dataset = expected_dataset
        self.expected_dataset_type = expected_dataset_type
        self.actual_dataset = actual_dataset
        self.actual_dataset_type = actual_dataset_type

    
    def run(self, context: Context) -> str:
        """
        Runs the command to compare the two datasets

        :param context:
        :return:
        """
        
        # need to get the expected dataset based on its type as a pandas df
        if self.expected_dataset_type.upper() == "WORKSHEET":
            expected_df = get_dataframe_from_worksheet(self.workbook, self.expected_dataset)
        elif self.expected_dataset_type.upper() == "RESULTSET":
            expected_df = context[self.expected_dataset]
            
        # get the actual dataset from the context as pandas df
        if self.actual_dataset_type.upper() == "WORKSHEET":
            actual_df = get_dataframe_from_worksheet(self.workbook, self.actual_dataset)
        elif self.actual_dataset_type.upper() == "RESULTSET":
            actual_df = context[self.actual_dataset]

        result = expected_df.equals(actual_df)
        if not result:
            print(f"Expected Data: {expected_df}")
            print(f"Actual Data: {actual_df}")
            print(f"Expected Types: {expected_df.dtypes}")
            print(f"Actual Types: {actual_df.dtypes}")
            assert result, f"Expected dataset {self.expected_dataset} does not match actual dataset {self.actual_dataset}."
        