from dataunit.commands.base import DataUnitCommand
from dataunit.context import Context
from utils.database_connector import DatabaseConnector

import pandas as pd


class LoadSheetToTableCommand(DataUnitCommand):
    """
    Class for the command that loads test data from the workbook to a database table
    """
    command_name = 'Load Sheet to Table'

    def __init__(self, workbook_path, workbook, settings, dataset_name, table_name=None, connection_string=None):
        self.workbook_path = workbook_path
        self.workbook = workbook
        self.settings = settings
        self.dataset_name = dataset_name
        self.data_source_connection_string = self.settings[connection_string.strip('${}')]
        self.data = pd.read_excel(self.workbook, sheet_name=self.dataset_name)

        # Assume table_name is in the form of <schema>.<table>
        try:
            self.schema_name = table_name.split('.')[0].strip('[]')
            self.table_name = table_name.split('.')[1].strip('[]')
        except Exception as e:
            raise e

    def run(self, context: Context):
        """
        Truncates the database table associated with the test command and loads it with test data

        :param context:
        :return:
        """
        # Make SQL statements to truncate the table
        #table_statements = self._drop_and_create_statements(self.data.columns)
        table_statements = self._truncate_statements
        self._execute_sql(table_statements)

        # Make SQL statements to load the table
        insert_statement = self._insert_statement
        self._execute_sql([insert_statement], self.data.values.tolist()) # Pass in INSERT SQL statement and data rows

    # def run_xlrd(self, context: Context):
    #     """Not yet implemented. Please update this docstring when this command is implemented.
    #     """
    #     print(self.workbook_path)
    #
    #     data = self.workbook.sheet_by_name(self.dataset_name)
    #     print(type(data))
    #
    #     insert_rows = []
    #     rows = [row for row in data.get_rows() if row[0].value != '']
    #     for row in rows:
    #         print(row)
    #     for row_idx in range(len(rows)):
    #         if row_idx > 0:
    #             rows2 = []
    #             for val in rows[row_idx]:
    #                 rows2.append(val.value)
    #             #rows.remove(rows[row_idx])
    #             #rows.insert(row_idx, rows2)
    #             insert_rows.append(rows2)
    #
    #     #rows = [rows[row_idx].value for row_idx in range(len(rows))]
    #     #rows = data.get_rows()
    #     print(rows)
    #     print(insert_rows)
    #
    #     # Make SQL statements to drop and create table
    #     #table_statements = self._get_ddl(rows[0], rows[1:])
    #     #self._execute_sql(table_statements)
    #
    #     # Make SQL statements to load table
    #     insert_statement = self._insert_statement(rows[0]) # Pass in column names only
    #     self._execute_sql_insert(insert_statement, rows[1:]) # Pass in data rows only

    @property
    def _drop_and_create_statements(self):
        """
        Based on dataset worksheet, builds and returns DROP TABLE and CREATE TABLE statements to execute as part
        of the test command

        :return: (list)
        """
        data_type_mappings = {"int64": "int", "int32": "int", "int16": "int", "object": "varchar"}
        sql_drop = "DROP TABLE IF EXISTS {}.{};".format(self.schema_name, self.table_name)

        col_types = []
        for column_name in self.data.columns:
            data_type = self.data[column_name].dtype.__str__()
            if data_type.startswith('int'):
                col_types.append(column_name + " " + data_type_mappings[data_type] + " NULL")
            elif data_type == "object":
                max_len = pd.eval("self.data." + column_name).map(len).max()
                col_types.append(column_name + " " + data_type_mappings[data_type] + "({})".format(max_len) + " NULL")

        sql_create = "CREATE TABLE {}.{} ( {} );".format(
            self.schema_name
            , self.table_name
            , ",".join(column for column in col_types)
        )

        return [sql_drop, sql_create]

    @property
    def _truncate_statements(self):
        """
        Based on dataset worksheet, creates TRUNCATE TABLE statements to execute as part of the test command

        :return: (list)
        """
        return ["TRUNCATE TABLE {}.{};".format(self.schema_name, self.table_name)]

    @property
    def _insert_statement(self):
        """
        Based on dataset worksheet, creates parameterized INSERT statement to execute with the associated data rows
        as part of the test command

        :param columns: (list)
        :return: insert_statement: (str)
        """
        columns = self.data.columns
        insert_statement = "INSERT INTO [{}].[{}] ({}) VALUES ({});"

        try:
            insert_statement = insert_statement.format(
                    self.schema_name
                    , self.table_name
                    , ",".join(column for column in columns)
                    , ",".join("?" for column in columns)
                )
        except Exception as e:
            #logger.error("Unable to parse SQL INSERT statements.", exc_info=True)
            raise (e)

        return insert_statement

    def _execute_sql(self, statements: list, data: list=None):
        """
        Runs one or more SQL statements passed in as a list, returning nothing

        :param statements: (list)
        :param data:
        :return:
        """
        # Connect to database and execute statements
        try:
            db_connector = DatabaseConnector(connection_string=self.data_source_connection_string)

            # For INSERT statements, use parameterized option, executing the parameterized statement with data rows
            if data is not None:
                for row in data:
                    print(statements[0])
                    print(row)
                    db_connector.execute_sql_no_result(statements[0], row)
            # For non-INSERTs, execute just the statement
            else:
                for statement in statements:
                    db_connector.execute_sql_no_result(statement)
        except Exception as e:
            #logger.error("Unable to store data on SQL Server.", exc_info=True)
            raise(e)