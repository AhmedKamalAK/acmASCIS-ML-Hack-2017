def submit_assignment(submitted_params, spreadsheetId, rangeName, service):
    values = [
        submitted_params
    ]
    body = {
        'values': values
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheetId, range=rangeName,
        valueInputOption='USER_ENTERED', body=body).execute()
