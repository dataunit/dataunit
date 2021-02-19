import unittest
from unittest import mock
import pandas as pd
import os
import xlrd
import docker
import time

import config
from dataunit.commands import execute_sql as esql

docker_client = docker.from_env()

class TestExecuteSQLCommand(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        Set up anything used by all tests, including ensuring Test SQL database Docker container is running
        """
        self.test_dir = os.path.join(config.PATH, "tests", "data")
        # Set up docker image and container, assuming Docker service is running on host
        if not docker_client.images.get("sqldb:1.0"):
            mssql_image = docker_client.images.build(path=os.path.join(config.PATH,"MyFitBot"),tag="sqldb:1.0")[0]
        mssql_container = docker_client.containers.get("mssql")
        # If container is not already running, then start it and wait for full startup (including DB script)
        if mssql_container.__getattribute__("status") != "running":
            mssql_container.start()
            time.sleep(33)
        # If container is already running, do not do anything (use it as-is)
        elif mssql_container:
            pass
        # If container has never been created before, create and run it and wait for full startup (including DB script)
        else:
            # mssql_container.remove(force=True)
            docker_client.containers.run("sqldb:1.0", name="mssql", ports={"1433/tcp": 1433}, detach=True)
            time.sleep(33)

    @classmethod
    def tearDownClass(self):
        pass
        #mssql_container = docker_client.containers.get("mssql")
        #mssql_container.kill()

    def test_run(self):
        """
        Tests that the run method calls the correct methods with the correct arguments

        :return:
        """
        print("Docker container started")

        # Inputs
        sql_text = "DELETE FROM dbo.Diet_Log WHERE 1=2"
        settings = {"DB_CONNECTION": "DRIVER={SQL Server};SERVER=localhost;DATABASE=MyFitBot;UID=SA;PWD=dataunitSQL2020!;"} #"${DB_CONNECTION}"
        workbook = xlrd.open_workbook(os.path.join(self.test_dir, "test_execute_sql.xlsx"))

        # Call DataUnit main method, instead of ExecuteSQLCommand, so that it takes just the Excel file as input
        # OR do both in separate tests
        command = esql.ExecuteSQLCommand(
            os.path.join(self.test_dir, "test_execute_sql.xlsx")
            , workbook
            , settings
            , sql_text
            , "${DB_CONNECTION}"
        )
        context = {"_dict": {}, "parent": None}
        # mock_db.return_value = mock.Mock(
        #         execute_sql_no_result=mock.Mock(
        #             return_value=None
        #         )
        # )
        #mock_pyodbc_connect.return_value = mock.MagicMock()

        # Actual
        command.run(context)

        print("Ran SQL command")
        # If it got here, means it ran the SQL successfully
        self.assertTrue(True)
