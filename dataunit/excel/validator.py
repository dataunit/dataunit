import xlrd

from dataunit.excel.constants import REQUIRED_COLUMNS, REQUIRED_SHEETS

def validate_workbook(workbook_name):
    # validates a test workbook for the correct sheets and sheet contents

    book = xlrd.open_workbook(workbook_name)

    # check for required sheets
    for sheet_name in REQUIRED_SHEETS:
        if sheet_name not in book.sheet_names():
            raise AssertionError('Required sheet "' + sheet_name + '" not found in workbook "' + workbook_name + '"')

        sheet = book.sheet_by_name(sheet_name)

        for column_name in REQUIRED_COLUMNS.get(sheet_name):
            if column_name not in sheet.row_values(0):
                raise AssertionError('Required column name "' + column_name +
                                        '" not found in workbook "' + workbook_name +'"'+
                                        ' in sheet "' + sheet_name + '"')


def main():
    validate_workbook('test_workbook.xlsx')



if __name__ == '__main__':
    main()
