import unittest
from unittest import mock
import os
import xlrd

import config
from dataunit.commands import execute_shell_command as esc


class TestExecuteShellCommand(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.join(config.PATH, "tests", "data")

        #self.db_client = database_connector.DatabaseConnector(self.connection_string)

    # @mock.patch("dataunit.commands.execute_shell_command.ExecuteShellCommand.subprocess")
    def test_run(self):
        """
        Tests that the run method returns the expected value when an echo command is run

        :return:
        """
        # Inputs
        workbook = xlrd.open_workbook(os.path.join(self.test_dir, "test_execute_shell_command.xlsx"))
        command = esc.ExecuteShellCommand(
            os.path.join(self.test_dir, "test_execute_shell_command.xlsx")
            , workbook
            , {}
            , "echo This is a test shell command."
        )
        context = {"_dict": {}, "parent": None}

        # Expected
        expected = "This is a test shell command.\r\n"

        # Actual
        actual = command.run(context)

        self.assertEqual(actual, expected)
