from dataunit.commands.dummy import DummyCommand
from dataunit.commands.load_sheet_to_table import LoadSheetToTableCommand
from dataunit.commands.execute_sql import ExecuteSQLCommand
from dataunit.commands.execute_shell_command import ExecuteShellCommand

commands = {
    DummyCommand.command_name: DummyCommand,
    LoadSheetToTableCommand.command_name: LoadSheetToTableCommand,
    ExecuteSQLCommand.command_name: ExecuteSQLCommand,
    ExecuteShellCommand.command_name: ExecuteShellCommand
}
