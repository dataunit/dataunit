import pyodbc
import pandas as pd

class DatabaseConnector():
    """
    Class used for interfacing with an ODBC database
    """
    def __init__(self, connection_string=None, server_name=None, database_name=None, server_port="1433"
                 , database_driver="SQL Server"):
        # Allow either full connection string to be passed in or server and database
        if connection_string is not None:
            self.connection_string = connection_string
        elif server_name is not None and database_name is not None:
            self.server_name = server_name
            self.database_name = database_name
            self.connection_string = "DRIVER={" + database_driver + "}" + ";SERVER={server_name},{server_port};" \
                    "DATABASE={database_name};Trusted_Connection=yes;"\
                    .format(server_name=server_name, server_port=server_port
                    , database_name=database_name)
        else:
            raise(RuntimeError('Must pass full either connection string or server and database to open database connection.'))

    @property
    def _connection(self):
        """
        Property that returns the pyodbc connection object using the DatabaseConnector connection_string attribute

        :param
        :return:
        """
        try:
            connection = pyodbc.connect(self.connection_string, autocommit=True)
            return connection
        except pyodbc.Error as pyodbc_error:
            raise pyodbc_error

    def execute_sql_no_result(self, sql_query_text, data=None):
        """
        Method that executes SQL statements without results (e.g., INSERT, UPDATE, DELETE)

        :param sql_query_text:
        :param data:
        :return:
        """
        connection = self._connection

        try:
            cursor = connection.cursor()
            if data is not None:
                cursor.execute(sql_query_text, data)
            else:
                cursor.execute(sql_query_text)
        except pyodbc.Error as pyodbc_error:
            raise pyodbc_error
        finally:
            cursor.commit()
            cursor.close()
            connection.close()

    def execute_sql_with_result(self, sql_query_text):
        """
        Method that executes SQL statements with results (e.g., SELECT), returning those results in a pandas DataFrame

        :param sql_query_text:
        :return:
        """
        connection = self._connection

        try:
            dataframe = pd.read_sql(sql_query_text, connection).astype(str)
        except Exception as e:
            raise e
        finally:
            connection.close()

        return dataframe