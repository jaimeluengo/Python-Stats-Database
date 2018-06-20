'''This library is used to interface raspberry pi with our own google sheet'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class WKS:
    def __init__(self,sp_name,ws_name):
        scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name('Visualization-ee1403d96de7.json', scope)
        self.spreadsheet_name = sp_name
        self.worksheet_name = ws_name
        self._refresh_auth()

    def _refresh_auth(self):
        gc = gspread.authorize(self.credentials)
        sp = gc.open(self.spreadsheet_name)
        try:
            self.wks = sp.worksheet(self.worksheet_name)
        except gspread.exceptions.WorksheetNotFound: #if the worksheet is not created
            #Copy row from a given worksheet to the new one
            first_row = sp.worksheet("iko6").row_values(1,"UNFORMATTED_VALUE")
            print(str(first_row))
            self.wks = sp.add_worksheet(self.worksheet_name,rows=10000, cols = 20)
            self.wks.insert_row(first_row,index=1)

    def _decorate(self, method):
        def safe_method(*args, **kwargs):
            try:
                method(*args, **kwargs)
            except gspread.exceptions.HTTPError as e:
                # getattr is needed to get a new instance of self.wks
                getattr(self.wks, method.__name__)(*args, **kwargs)
        return safe_method

    def __getattr__(self, attr):  # doesn't shadow _refresh_auth and _decorate
        return self._decorate(getattr(self.wks, attr))



'''Creates a new spreadsheet called <name> and shares it with <jaime.iko.dev@gmail.com>'''
def new_spreadsheet(name):
    name = str(name) #avoid not serialized json: https://stackoverflow.com/questions/24581098/typeerror-built-in-function-id-is-not-json-serializable
    sp = gc.create(name) #creates it in the service account, cannot be viewed
    sp.share('jaime.iko.dev@gmail.com', perm_type='user', role='writer') #need to share it to view it
    
'''Opens the given spreadsheet and adds a new worksheet.'''
def new_worksheet(sp_name,name):
    nrows = 10000
    ncolums = 20
    wks = gc.open(sp_name)
    return wks.add_worksheet(name,nrows,ncolums)
    
'''Inserts a row at a given index in a worksheet inside a spreadsheet. If the worksheet
does not exists, creates a new one and imports first row from a given one'''   
def insert_row(sp_name,worksheet_name,row_index,row):
   wks = WKS(sp_name,worksheet_name)
   wks.insert_row(row,row_index)


    




