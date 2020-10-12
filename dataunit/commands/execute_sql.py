from dataunit.commands.base import DataUnitCommand
from dataunit.context import Context
from utils.database_connector import DatabaseConnector

import pandas as pd


class ExecuteSQLCommand(DataUnitCommand):
    """
    Class for the command that executes a specified SQL statement without a return value; meant to be used for DML
    and DDL like TRUNCATE TABLE, INSERT, UPDATE, etc.
    """
    command_name = "Execute SQL"

    def __init__(self, workbook_path, workbook, settings, sql_statement, connection_string=None):
        self.workbook_path = workbook_path
        self.workbook = workbook
        self.settings = settings
        self.sql_statement = sql_statement
        self.data_source_connection_string = self.settings[connection_string.strip('${}')]

    def run(self, context: Context):
        """
        Executes the SQL statement specified in the workbook for the test command with no return value

        :param context:
        :return:
        """
        # Validate SQL statement

        # Execute SQL statement
        db_con = DatabaseConnector(self.data_source_connection_string)
        db_con.execute_sql_no_result(sql_query_text=self.sql_statement)

    def validate_sql(self):
        """
        Make sure the statement is valid SQL

        :return:
        """
        pass
    