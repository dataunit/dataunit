from dataunit.commands.base import DataUnitCommand
from dataunit.context import Context

import subprocess


class ExecuteShellCommand(DataUnitCommand):
    """
    Class for the command that executes a specified shell statement without a return value; used to show a 
    working dataunit command without any dependencies
    """
    command_name = "Execute Shell Command"

    def __init__(self, workbook_path, workbook, settings, command):
        self.workbook_path = workbook_path
        self.workbook = workbook
        self.settings = settings
        self.command = command.split()
        # self.data_source_connection_string = self.settings[connection_string.strip('${}')]

    def run(self, context: Context) -> str:
        """
        Executes the shell statement specified in the workbook for the test command with no return value

        :param context:
        :return:
        """
        # Validate shell command

        # Execute shell command
        output = subprocess.run(self.command, shell=True, check=True, capture_output=True).stdout.decode("utf-8")
        print(output)

        return output

    def validate_shell(self):
        """
        Make sure the statement is valid shell command

        :return:
        """

        pass