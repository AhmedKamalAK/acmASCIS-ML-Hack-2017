def submit_assignment(submitted_params, spreadsheet_id, sheet_range, service):
    values = [
        submitted_params
    ]
    body = {
        'values': values
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range=sheet_range,
        valueInputOption='USER_ENTERED', body=body).execute()
