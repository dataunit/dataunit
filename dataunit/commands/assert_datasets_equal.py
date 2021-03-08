from dataunit.commands.base import DataUnitCommand
from dataunit.context import Context

class AssertDatasetsEqualCommand(DataUnitCommand):
    """
    Class for the command that asserts two datasets are equal, 
    should raise an exception if they are not equal
    """
    command_name = "Assert Datasets Equal"

    def __init__(self, workbook_path, workbook, settings, expected_dataset, expected_dataset_type, actual_dataset, actual_dataset_type):
        self.workbook_path = workbook_path
        self.workbook = workbook
        self.settings = settings
        self.expected_dataset = expected_dataset
        self.expected_dataset_type = expected_dataset_type
        self.actual_dataset = actual_dataset
        self.actual_dataset_type = actual_dataset_type


    def run(self, context: Context) -> str:
        """
        Runs the command to compare the two datasets

        :param context:
        :return:
        """
        
        if self.expected_dataset_type.upper() == "WORKSHEET":

            #df = get_dataframe_from_worksheet(self.workbook, self.expected_dataset)
            pass
        else if self.expected_dataset_type.upper() == "RESULTSET":
            
            df = Context[self.expected_dataset]
            
        #TODO get the expected and actual datasets at pandas dataframes and then compare them using pandas equal
        #TODO will need a helper method to load the pandas from worksheet
        

    


