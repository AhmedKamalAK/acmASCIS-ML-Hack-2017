def clear_sheet_range(spreadsheet_id, sheet_range, rows, cols, service):
    body = {
        'values': [['' for j in range(cols)] for i in range(rows)]
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=sheet_range,
        valueInputOption='USER_ENTERED', body=body).execute()


def fetch_submissions(spreadsheet_id, sheet_range, service, clear_sheet=True):
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=sheet_range).execute()
    values = result.get('values', [])
    if values and clear_sheet is True:
        rows = len(values)
        cols = len(values[0])
        clear_sheet_range(spreadsheet_id, sheet_range, rows, cols, service)
    return values
