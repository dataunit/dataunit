import xlrd
import xlrd.sheet
from unittest import TestSuite

from dataunit.case import DataUnitTestCase
from dataunit import commands
from dataunit import context


class ExcelTestLoader(object):
    """This class is responsible for loading all tests and
    data from a DataUnit Excel workbook.
    and colton rocks
    """

    def __init__(self):
        super().__init__()

    def load_tests_from_workbook(self, workbook_name: str) -> TestSuite:
        """Load all tests from a dataunit workbook and return as a unittest TestSuite

        :param workbook_name: The name of the workbook from which to load the tests definitions
        :returns: A TestSuite containing all tests defined in the provided workbook.
        """
        workbook = xlrd.open_workbook(workbook_name)

        # Set workbook variable in global context
        global_context = context.get_global_context()
        global_context['workbook'] = workbook

        tests_sheet = workbook.sheet_by_name('Tests')
        if tests_sheet.nrows <= 1:
            # We have no tests defined. return empty suite.
            return TestSuite()
        # Start with second row, first row is header
        tests = [test for test in tests_sheet.get_rows()][1:]
        test_cases = []
        for test in tests:
            name = test[0].value
            active = test[1].value
            description = test[2].value
            commands_sheet_name = test[3].value
            commands_sheet = workbook.sheet_by_name(commands_sheet_name)

            test_commands = self._load_commands_from_worksheet(commands_sheet, workbook_name, workbook)
            test_case = DataUnitTestCase(test_commands=test_commands, global_context=global_context)
            test_cases.append(test_case)

        test_suite = TestSuite(test_cases)
        return test_suite

    def _load_commands_from_worksheet(self, sheet: xlrd.sheet.Sheet = [], workbook_name='', workbook=None) -> list:
        """Load all commands from the provided worksheet and return them in a list.

        Args:
            sheet: The sheet containing all test commands.

        Returns:
            The list of all TestCommand instances defined in the sheet.
        """
        # TODO - Load TestCommand instances from worksheet
        test_commands = []

        test_commands_from_sheet = [row for row in sheet.get_rows() if row[2].value != ''][1:]  # Skip row 0 for header
        for command_row in test_commands_from_sheet:
            active = command_row[0].value
            command_description = command_row[1].value
            command = command_row[2].value

            command_class = commands.commands[command]

            # Get parameters from Settings sheet
            settings = self._load_settings_from_worksheet(workbook.sheet_by_name('Settings'))
            workbook_dict = {'workbook_path': workbook_name, 'workbook': workbook, 'settings': settings}

            # Get parameters from Test Commands sheet
            params_from_sheet = [cell.value for cell in command_row[3:]]
            params = self._parse_params(params_from_sheet)
            params = {**workbook_dict, **params}

            # Call new method to find "Sheet Name" parameter value in params dictionary and load that sheet to a DataFrame,
                # which gets passed to the command?
            # OR load the sheet within the LoadSheetToTable command class to DF using the "Sheet Name"

            command = command_class(**params)
            test_commands.append(command)

        return test_commands

    def _load_settings_from_worksheet(self, sheet: xlrd.sheet.Sheet = []) -> dict:
        """Load all commands from the provided worksheet and return them in a list.

        Args:
            sheet: The sheet containing all settings.

        Returns:
            The dictionary of all Settings rows defined in the sheet.
        """
        # TODO - Load TestCommand instances from worksheet
        settings = {}

        settings_from_sheet = [row for row in sheet.get_rows() if row[2].value != ''][1:]  # Skip row 0 for header
        for settings_row in settings_from_sheet:
            settings[settings_row[0].value] = settings_row[1].value

        return settings

    def _parse_params(self, params_from_sheet: list) -> dict:
        """Parse all named params from the command worksheet row and return as a dict

        Args:
            params_from_sheet: The slice of the worksheet row containing all named parameters.

        Returns:
            A dictionary containing all named parameters defined for the command.

        """
        params = {}
        for i in range(0, len(params_from_sheet), 2):
            if params_from_sheet[i] == '':
                break
            params[params_from_sheet[i]] = params_from_sheet[i + 1]

        return params
