from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credentials.json'


class GoogleSpreadsheets:
    """_summary_

    Returns:
        _type_: _description_
    """
    def __init__(self, spreadsheet_id:str):

        self.creds = None
        self.creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # The ID and range of a sample spreadsheet.
        self.spreadsheet_id = spreadsheet_id

        service = build('sheets', 'v4', credentials=self.creds)

# Call the Sheets API
        self.sheet = service.spreadsheets()

        #read
    def read(self, data_range:str):
        result = self.sheet.values().get(spreadsheetId=self.spreadsheet_id,
                                    range=data_range).execute()

        values = result.get('values', [])

        return values

    def write(self, data_range:str, values_list:list):
        self.sheet.values().update(spreadsheetId=self.spreadsheet_id, range=data_range,
                                valueInputOption="USER_ENTERED", body={"values":values_list}
                                ).execute()

    def append(self, data_range:str, values_list:list):
        self.sheet.values().append(spreadsheetId=self.spreadsheet_id,
                                        range=data_range,
                                        valueInputOption="USER_ENTERED",
                                        insertDataOption="INSERT_ROWS",
                                        body={"values":values_list}
                                        ).execute()
