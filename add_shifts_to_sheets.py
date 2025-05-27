import gspread
from google.oauth2.service_account import Credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'service_account.json'
SPREADSHEET_ID = '1sqOp9pOBGbSvyp9xQyMeX7fBYlWs6p7pHYCO6SuM1Fo'
SHEET_NAME = 'Sheet1'

def add_shifts_to_sheet(shifts):
    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)
    for shift in shifts:
        sheet.append_row([shift])

if __name__ == '__main__':
    shifts = ['Sample shift 1', 'Sample shift 2']  # Replace with actual data
    add_shifts_to_sheet(shifts)
