import unittest
from unittest import mock
import pandas as pd
import os
import xlrd

import config
from dataunit.commands import load_sheet_to_table as ls


class LoadSheetToTableTestCommand(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.join(config.PATH, "tests", "data")

        #self.db_client = database_connector.DatabaseConnector(self.connection_string)

    @mock.patch("dataunit.commands.load_sheet_to_table.LoadSheetToTableCommand._execute_sql")
    @mock.patch("dataunit.commands.load_sheet_to_table.LoadSheetToTableCommand._insert_statement"
        , new_callable=mock.PropertyMock)
    @mock.patch("dataunit.commands.load_sheet_to_table.LoadSheetToTableCommand._truncate_statements"
        , new_callable=mock.PropertyMock)
    def test_run(self, mock_truncate, mock_insert, mock_execute):
        """
        Tests that the run method calls the correct methods with the correct arguments

        :return:
        """
        # Inputs
        schema = "dbo"
        table = "Diet_Log"
        connection_string = "${DB_CONNECTION}"
        workbook = xlrd.open_workbook(os.path.join(self.test_dir, "test_load_sheet_to_table.xlsx"))
        command = ls.LoadSheetToTableCommand(
            os.path.join(self.test_dir, "test_load_sheet_to_table.xlsx")
            , workbook
            , {"DB_CONNECTION": "DRIVER={SQL Server};SERVER=localhost;DATABASE=FakeDB;Trusted_Connection=yes;"}
            , "Diet_Log_1", "{}.{}".format(schema, table), connection_string
        )
        columns = "Diet_Log_Id,Profile_Id,Log_Date,Meal,Food_Name,Calorie_Per_Unit,Quantity"
        values = [
            [41, 1, '2018-03-15', 'Snack', 'Fiber Bar', 140, 1]
            , [42, 2, '2018-03-15', 'Snack', 'Carrots and Dip', 5, 20]
            , [43, 1, '2018-03-15', 'Meal', 'Spaghetti and Meatballs', 800, 1]
        ]
        context = {"_dict": {}, "parent": None}
        mock_truncate.return_value = ["TRUNCATE TABLE " + schema + "." + table + ";"]
        mock_insert.return_value = "INSERT INTO " + schema + "." + table + " (" + columns + ") " \
                                    "VALUES (?,?,?,?,?,?,?);"
        mock_execute.return_value = mock.MagicMock()

        # Actual
        command.run(context)

        mock_truncate.assert_called_with()
        mock_insert.assert_called_with()
        mock_execute.assert_has_calls([
            mock.call(mock_truncate.return_value)
            , mock.call([mock_insert.return_value], values)
        ])

    def test_drop_and_create_statements(self):
        """
        Tests that the drop_and_create_statements property returns the expected DROP TABLE and CREATE TABLE statements
        based on test data input

        :return:
        """
        # Inputs
        schema = "dbo"
        table = "Diet_Log"
        connection_string = "${DB_CONNECTION}"
        workbook = xlrd.open_workbook(os.path.join(self.test_dir, "test_load_sheet_to_table.xlsx"))
        command = ls.LoadSheetToTableCommand(
            os.path.join(self.test_dir, "test_load_sheet_to_table.xlsx")
            , workbook
            , {"DB_CONNECTION": "DRIVER={SQL Server};SERVER=localhost;DATABASE=FakeDB;Trusted_Connection=yes;"}
            , "Diet_Log_1", "{}.{}".format(schema, table), connection_string
        )

        # Actual
        actual = command._drop_and_create_statements

        # Expected
        sql_drop = "DROP TABLE IF EXISTS " + schema + "." + table + ";"
        sql_create = "CREATE TABLE " + schema + "." + table + " ( " \
                        "Diet_Log_Id int NULL" \
                        ",Profile_Id int NULL" \
                        ",Log_Date varchar(10) NULL" \
                        ",Meal varchar(5) NULL" \
                        ",Food_Name varchar(23) NULL" \
                        ",Calorie_Per_Unit int NULL" \
                        ",Quantity int NULL );"
        expected = [sql_drop, sql_create]

        self.assertEqual(expected, actual)

    def test_truncate_statements(self):
        """
        Tests that the truncate_statements property returns the expected TRUNCATE TABLE SQL based on test data input

        :return:
        """
        # Inputs
        schema = "dbo"
        table = "Diet_Log"
        connection_string = "${DB_CONNECTION}"
        workbook = xlrd.open_workbook(os.path.join(self.test_dir, "test_load_sheet_to_table.xlsx"))
        command = ls.LoadSheetToTableCommand(
            os.path.join(self.test_dir, "test_load_sheet_to_table.xlsx")
            , workbook
            , {"DB_CONNECTION": "DRIVER={SQL Server};SERVER=localhost;DATABASE=FakeDB;Trusted_Connection=yes;"}
            , "Diet_Log_1", "{}.{}".format(schema, table), connection_string
        )

        # Actual
        actual = command._truncate_statements

        # Expected
        expected = ["TRUNCATE TABLE " + schema + "." + table + ";"]

        self.assertEqual(expected, actual)

    def test_insert_statement(self):
        """
        Tests that the insert_statement property returns the expected INSERT SQL based on test data input

        :return:
        """
        # Inputs
        schema = "dbo"
        table = "Diet_Log"
        connection_string = "${DB_CONNECTION}"
        workbook = xlrd.open_workbook(os.path.join(self.test_dir, "test_load_sheet_to_table.xlsx"))
        command = ls.LoadSheetToTableCommand(
            os.path.join(self.test_dir, "test_load_sheet_to_table.xlsx")
            , workbook
            , {"DB_CONNECTION": "DRIVER={SQL Server};SERVER=localhost;DATABASE=FakeDB;Trusted_Connection=yes;"}
            , "Diet_Log_1", "{}.{}".format(schema, table), connection_string
        )
        columns = "Diet_Log_Id,Profile_Id,Log_Date,Meal,Food_Name,Calorie_Per_Unit,Quantity"

        # Actual
        actual = command._insert_statement

        # Expected
        expected = "INSERT INTO [" + schema + "].[" + table + "] (" + columns + ") VALUES (?,?,?,?,?,?,?);"

        self.assertEqual(expected, actual)

    @mock.patch('pyodbc.connect')
    def test_execute_sql_without_data(self,mock_pyodbc):
        """
        Tests that the _execute_sql method calls the method responsible for running DDL/DML SQL statements with
        the expected arguments

        :return:
        """
        # Inputs
        connection_string = "${DB_CONNECTION}"
        workbook = xlrd.open_workbook(os.path.join(self.test_dir, "test_load_sheet_to_table.xlsx"))
        command = ls.LoadSheetToTableCommand(
            os.path.join(self.test_dir, "test_load_sheet_to_table.xlsx")
            , workbook
            , {"DB_CONNECTION": "DRIVER={SQL Server};SERVER=localhost;DATABASE=FakeDB;Trusted_Connection=yes;"}
            , "Diet_Log_1", "dbo.Diet_Log", connection_string
        )
        statements = ["TRUNCATE TABLE FakeSchema.FakeTable;"]
        #mock_database_connector.return_value = mock.MagicMock()
        #mock_database_connector().execute_sql_no_result.return_value = mock.MagicMock()
        #mock_execute_sql_no_result.return_value = mock.MagicMock()
        mock_pyodbc.return_value = mock.MagicMock()

        # Actual
        command._execute_sql(statements)

        # Expected
        mock_pyodbc().cursor().execute.assert_has_calls([
            mock.call(statements[0])
        ])

    @mock.patch('pyodbc.connect')
    def test_execute_sql_with_data(self,mock_pyodbc):
        """
        Tests that the _execute_sql method calls the method responsible for running SELECT SQL statements with
        the expected arguments

        :return:
        """
        # Inputs
        connection_string = "${DB_CONNECTION}"
        workbook = xlrd.open_workbook(os.path.join(self.test_dir, "test_load_sheet_to_table.xlsx"))
        command = ls.LoadSheetToTableCommand(
            os.path.join(self.test_dir, "test_load_sheet_to_table.xlsx")
            , workbook
            , {"DB_CONNECTION": "DRIVER={SQL Server};SERVER=localhost;DATABASE=FakeDB;Trusted_Connection=yes;"}
            , "Diet_Log_1", "dbo.Diet_Log", connection_string
        )
        statements = ["INSERT INTO FakeSchema.FakeTable (Column1, Column2) VALUES (?,?)"]
        data = [["r1v1","r1v2"], ["r2v1","r2v2"]]
        #mock_database_connector.return_value = mock.MagicMock()
        #mock_database_connector().execute_sql_no_result.return_value = mock.MagicMock()
        #mock_execute_sql_no_result.return_value = mock.MagicMock()
        mock_pyodbc.return_value = mock.MagicMock()

        # Actual
        command._execute_sql(statements, data)

        # Expected
        mock_pyodbc().cursor().execute.assert_has_calls([
            mock.call(statements[0], data[0])
            ,mock.call(statements[0], data[1])
        ])
