from dataunit.commands.base import DataUnitCommand
from dataunit.context import Context


class DummyCommand(DataUnitCommand):
    command_name = 'dummy'

    def run(self, context: Context):
        pass
