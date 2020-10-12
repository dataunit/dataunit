import unittest
import unittest.mock as mock

from dataunit import commands
from dataunit.case import DataUnitTestCase
from dataunit.context import get_global_context


@mock.patch('dataunit.case.Context', autospec=True)
class DataUnitTestCaseTestCase(unittest.TestCase):
    command_name = 'dummy'

    def test_runTest(self, mock_context):
        global_context = mock_context()
        command_class = commands.commands[self.command_name]
        test_commands = [mock.MagicMock(command_class), mock.MagicMock(command_class), mock.MagicMock(command_class)]
        test_case = DataUnitTestCase(test_commands=test_commands, global_context=global_context)
        test_case.run()

        mock_context.assert_called_with(parent=global_context)
        for command in test_commands:
            command.run.assert_called_with(mock_context())
