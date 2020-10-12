import unittest
from unittest import mock
import os
import pyodbc
import pandas as pd

from utils import database_connector


class TestDatabaseConnector(unittest.TestCase):

    def setUp(self):
        self.connection_string = "DRIVER={SQL Server};SERVER=%s,%s;DATABASE=%s;%s" % \
                ("SERVER","PORT","DATABASE","Trusted_Connection=yes")
        self.db_client = database_connector.DatabaseConnector(self.connection_string)

    @mock.patch('pyodbc.connect')
    def test_connection(self, mock_pyodbc_connect):
        """
        Tests that the correct SQL Server connection is made when instantiated with the connection string
        """
        # Call method
        conn = self.db_client._connection()

        self.assertIsNotNone(conn)
        mock_pyodbc_connect.assert_called_with(self.connection_string, autocommit=True)

    @mock.patch('pyodbc.connect')
    def test_connection_no_conn_string(self, mock_pyodbc_connect):
        """
        Tests that the correct SQL Server connection is made when instantiated with the server and database names,
        instead of the connecting string
        """
        # Inputs
        self.db_client = database_connector.DatabaseConnector(server_name="FakeServer", database_name="FakeDB")

        # Call method
        conn = self.db_client._connection()

        self.assertIsNotNone(conn)
        mock_pyodbc_connect.assert_called_with("DRIVER={SQL Server};SERVER=%s,%s;DATABASE=%s;%s;" % \
                ("FakeServer","1433","FakeDB","Trusted_Connection=yes"), autocommit=True)

    @mock.patch('pandas.read_sql')
    @mock.patch('utils.database_connector.DatabaseConnector._connection')
    def test_execute_sql_with_result(self, mock_get_sqlserver_connection, mock_pd_readsql):
        """
        Tests that the method that executes a SQL query with a result is called with the expected parameters
        and returns the expected DataFrame result
        """
        # Inputs
        query = "SELECT * FROM FakeSchema.FakeTable"
        mock_get_sqlserver_connection.return_value = self.db_client._connection
        mock_pd_readsql.return_value = pd.DataFrame({"Col1":["Val1","Val2"], "Col2": [1,2]})

        # Actual
        actual = self.db_client.execute_sql_with_result(query)

        # Expected
        expected = pd.DataFrame({"Col1":["Val1","Val2"], "Col2": ["1","2"]})

        mock_pd_readsql.assert_called_with(query, mock_get_sqlserver_connection.return_value)
        self.assertTrue(actual.equals(expected))

    @mock.patch('utils.database_connector.DatabaseConnector._connection')
    def test_execute_sql_no_result(self, mock_get_sqlserver_connection):
        """
        Tests that the method that executes a SQL command is called with the expected parameters
        """
        # Inputs
        query = "TRUNCATE TABLE FakeSchema.FakeTable"
        mock_get_sqlserver_connection.return_value = self.db_client._connection

        # Actual
        self.db_client.execute_sql_no_result(query)

        # Expected
        mock_get_sqlserver_connection().cursor().execute.assert_called_with(query)

    @mock.patch('utils.database_connector.DatabaseConnector._connection')
    def test_execute_sql_no_result_with_params(self, mock_get_sqlserver_connection):
        """
        Tests that the method that executes a SQL command is called with the expected parameters
        """
        # Inputs
        query = "INSERT INTO FakeSchema.FakeTable (Column1, Column2) VALUES (?,?)"
        data = ["r1v1","r1v2"]
        mock_get_sqlserver_connection.return_value = self.db_client._connection

        # Actual
        self.db_client.execute_sql_no_result(query, data)

        # Expected
        mock_get_sqlserver_connection().cursor().execute.assert_called_with(query, data)
