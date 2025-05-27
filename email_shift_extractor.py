
import os
import re

if not os.path.exists('credentials.json'):
    print("Error: 'credentials.json' file is missing. Please ensure it is present in the working directory.")
    sys.exit(1)

# Existing code follows...
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def fetch_shift_emails():
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', q='shift OR duty', maxResults=30).execute()
    messages = results.get('messages', [])
    shifts = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        snippet = msg_data['snippet']
        if re.search(r'(Date|Time|Shift|Duty)', snippet, re.IGNORECASE):
            shifts.append(snippet)
    return shifts

if __name__ == '__main__':
    shifts = fetch_shift_emails()
    for shift in shifts:
        print(shift)
