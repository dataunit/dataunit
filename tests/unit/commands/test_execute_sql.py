import unittest
from unittest import mock
import pandas as pd
import os
import xlrd

import config
from dataunit.commands import execute_sql as esql


class TestExecuteSQLCommand(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.join(config.PATH, "tests", "data")

        #self.db_client = database_connector.DatabaseConnector(self.connection_string)

    # @mock.patch("dataunit.commands.execute_sql.ExecuteSQLCommand._insert_statement"
    #     , new_callable=mock.PropertyMock)
    # @mock.patch("dataunit.commands.execute_sql.ExecuteSQLCommand._truncate_statements"
    #     , new_callable=mock.PropertyMock)
    # @mock.patch("utils.database_connector.DatabaseConnector")
    @mock.patch('pyodbc.connect')
    def test_run(self, mock_pyodbc_connect):
        """
        Tests that the run method calls the correct methods with the correct arguments

        :return:
        """
        # Inputs
        sql_text = "DELETE FROM dbo.Diet_Log_1"
        connection_string = "${DB_CONNECTION}"
        workbook = xlrd.open_workbook(os.path.join(self.test_dir, "test_execute_sql.xlsx"))
        command = esql.ExecuteSQLCommand(
            os.path.join(self.test_dir, "test_execute_sql.xlsx")
            , workbook
            , {"DB_CONNECTION": "DRIVER={SQL Server};SERVER=localhost;DATABASE=FakeDB;Trusted_Connection=yes;"}
            , sql_text
            , connection_string
        )
        context = {"_dict": {}, "parent": None}
        # mock_db.return_value = mock.Mock(
        #         execute_sql_no_result=mock.Mock(
        #             return_value=None
        #         )
        # )
        mock_pyodbc_connect.return_value = mock.MagicMock()

        # Actual
        command.run(context)

        mock_pyodbc_connect().cursor().execute.assert_has_calls([
            mock.call(command.sql_statement)
        ])
        # .assert_called_with(command.data_source_connection_string)
        # mock_db.return_value.assert_called_with(sql_query_text=command.sql_statement)
