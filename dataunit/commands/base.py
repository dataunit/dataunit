import abc

from dataunit.context import Context


class DataUnitCommand(metaclass=abc.ABCMeta):
    """Abstract Base Class defining methods required to implement a DataUnit Command class.

    Note: `metaclass=abc.ABCMeta is an explicit way of defining this class as an Abstract Base Class.
        All abstract methods must be implemented in order to successfully define a subclass of this class.

    Note: All subclasses must define the command_name property in order to perform dynamic loading of the command class.
    """

    @abc.abstractmethod
    def run(self, context: Context):
        """Run this command with the given context.
        """
        raise NotImplementedError()
