from dataunit.commands.base import DataUnitCommand
from dataunit.context import Context
from dataunit.excel.dataframe_utils import get_dataframe_from_worksheet
import pandas as pd

class AssertRecordCountsEqualCommand(DataUnitCommand):
    """
    Class for the command that asserts two datasets are equal, 
    should raise an exception if they are not equal
    """
    command_name = "Assert Record Counts Equal"

    def __init__(self, workbook_path, workbook, settings, expected_record_count, actual_dataset, actual_dataset_type):
        self.workbook_path = workbook_path
        self.workbook = workbook
        self.settings = settings
        self.expected_record_count = expected_record_count
        self.actual_dataset = actual_dataset
        self.actual_dataset_type = actual_dataset_type

    
    def run(self, context: Context) -> str:
        """
        Runs the command to compare the two datasets

        :param context:
        :return:
        """
        # Set expected count
        expected = int(self.expected_record_count)

        # get the actual dataset from the context as pandas df
        if self.actual_dataset_type.upper() == "WORKSHEET":
            actual_df = get_dataframe_from_worksheet(self.workbook, self.actual_dataset)
        elif self.actual_dataset_type.upper() == "RESULTSET":
            actual_df = context[self.actual_dataset]
        actual = len(actual_df.index)

        result = expected == actual
        if not result:
            print(f"Expected Count: {expected}")
            print(f"Actual Count: {actual_df}")
            assert result, f"Expected dataset count {expected} does not match actual dataset count {actual}."

     
        