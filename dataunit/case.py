import unittest

from dataunit.context import Context, get_global_context


class DataUnitTestCase(unittest.TestCase):
    """A class defining a single DataUnit tests case.

    This class is designed to be instantiated with a
    list of TestCommand instances which define the
    behavior of this tests case.

    :note: This class will be executed as a test case by PyCharm. It should pass
    due to an empty test_command list default.

    :param test_commands: List of TestCommand instances used to execute
        the tests case.
    """

    # noinspection PyPep8Naming
    def __init__(self, methodName='runTest', test_commands: list=[], global_context: Context=None):
        # Validate Params
        if test_commands is None:
            raise ValueError('Parameter test_commands must not be None.')
        for command in test_commands:
            if not hasattr(command, 'run'):
                raise ValueError('Parameter test_commands must be list of runnable objects')

        # Call unittest.TestCase.__init__() to setup default behavior.
        super().__init__(methodName)

        # Set attributes on self.
        self.test_commands = test_commands
        self.global_context = global_context

    def runTest(self):
        """Execute the actual tests case
        """
        test_context = Context(parent=self.global_context)
        for cmd in self.test_commands:
            cmd.run(test_context)
