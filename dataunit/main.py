from argparse import ArgumentParser
from unittest.runner import TextTestRunner

from dataunit.excel.loader import ExcelTestLoader


def parse_args(argv: list):
    parser = ArgumentParser()
    parser.add_argument('workbook', help='The excel workbook from which to load tests.')
    args = parser.parse_args(argv)
    return args


def main(excel_workbook_name):
    loader = ExcelTestLoader()
    tests = loader.load_tests_from_workbook(excel_workbook_name)
    test_runner = TextTestRunner(verbosity=1,
                                 failfast=None,
                                 buffer=None,
                                 warnings=None,
                                 tb_locals=False)
    result = test_runner.run(tests)
    return not result.wasSuccessful()
