from dataunit.commands.base import DataUnitCommand
from dataunit.context import Context
from utils.database_connector import DatabaseConnector
import constants

import pandas as pd


class ExecuteSQLWithResultsetCommand(DataUnitCommand):
    """
    Class for the command that executes a specified SQL statement with a return value; meant to be used for 
    SELECT statements
    """
    command_name = "Execute SQL With Resultset"

    def __init__(self, workbook_path, workbook, settings, sql_statement, connection_string=None, result_variable_name=constants.RESULT_VARIABLE_NAME):
        self.workbook_path = workbook_path
        self.workbook = workbook
        self.settings = settings
        self.sql_statement = sql_statement
        self.data_source_connection_string = self.settings[connection_string.strip('${}')]
        self.result_variable_name = result_variable_name

    def run(self, context: Context):
        """
        Executes the SQL statement specified in the workbook for the test command with return value

        :param context:
        :return:
        """
        # Validate SQL statement

        # Execute SQL statement
        db_con = DatabaseConnector(self.data_source_connection_string)
        context[self.result_variable_name] = db_con.execute_sql_with_result(sql_query_text=self.sql_statement)

    def validate_sql(self):
        """
        Make sure the statement is valid SQL

        :return:
        """
        pass
    