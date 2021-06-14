import unittest
from unittest import mock
import pandas as pd
import os
import xlrd

import config
from dataunit.commands import assert_recordcounts_equal as arce
from dataunit.context import Context


class TestAssertRecordCountsEqualCommand(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.join(config.PATH, "tests", "data")

    # @mock.patch('pyodbc.connect')
    def test_run(self):
        """
        Tests that the run method calls the correct methods with the correct arguments

        :return:
        """
        # Inputs
        expected_record_count = 3
        actual_dataset = "TestRecordCount"
        actual_dataset_type = "RESULTSET"
        workbook = xlrd.open_workbook(os.path.join(self.test_dir, "test_workbook_recordcount.xlsx"))
        command = arce.AssertRecordCountsEqualCommand(
            workbook_path=os.path.join(self.test_dir, "test_workbook_recordcount.xlsx")
            , workbook=workbook
            , settings={"DB_CONNECTION": "DRIVER={SQL Server};SERVER=localhost;DATABASE=FakeDB;Trusted_Connection=yes;"}
            , expected_record_count=expected_record_count
            , actual_dataset=actual_dataset
            , actual_dataset_type=actual_dataset_type
        )
        df = pd.DataFrame([["a"],["b"],["c"]],columns=["col1"])
        context = Context()
        context[actual_dataset] = df
        # print(context)
        # print(context[actual_dataset])

        # Actual
        command.run(context)
