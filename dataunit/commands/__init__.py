from dataunit.commands.dummy import DummyCommand
from dataunit.commands.load_sheet_to_table import LoadSheetToTableCommand
from dataunit.commands.execute_sql import ExecuteSQLCommand
from dataunit.commands.execute_shell_command import ExecuteShellCommand
from dataunit.commands.execute_sql_with_resultset import ExecuteSQLWithResultsetCommand
from dataunit.commands.assert_datasets_equal import AssertDatasetsEqualCommand

commands = {
    DummyCommand.command_name: DummyCommand,
    LoadSheetToTableCommand.command_name: LoadSheetToTableCommand,
    ExecuteSQLCommand.command_name: ExecuteSQLCommand,
    ExecuteShellCommand.command_name: ExecuteShellCommand,
    ExecuteSQLWithResultsetCommand.command_name: ExecuteSQLWithResultsetCommand,
    AssertDatasetsEqualCommand.command_name: AssertDatasetsEqualCommand
}
