from assignments_submitter import submit_assignment
from submissions_fetcher import *
from sheets_service import get_sheets_service


def main():
    spreadsheet_id = '1O4nOl-UvVjGvuM_zrES3vvPcV4HEkzAl9PuuKen36uQ';
    sheet_range = 'TestSheet'
    params = ['a', 'str', 1];
    service = get_sheets_service()
    submit_assignment(params, spreadsheet_id, sheet_range, service)
    fetch_submissions(spreadsheet_id, sheet_range, service)

if __name__ == '__main__':
    main()
