import sys

from dataunit.main import main, parse_args

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    dataunit_excel_workbook = args.workbook
    sys.exit(main(dataunit_excel_workbook))
