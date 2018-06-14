'''This library is used to interface raspberry pi with our own data sheet'''


import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds',
     'https://www.googleapis.com/auth/drive']

#IMPORTANT: Have json file in same folder as this python file
credentials = ServiceAccountCredentials.from_json_keyfile_name('Visualization-ee1403d96de7.json', scope)

gc = gspread.authorize(credentials)

'''Creates a new spreadsheet called <name> and shares it with <jaime.iko.dev@gmail.com>'''
def new_spreadsheet(name):
    name = str(name) #avoid not serialized json: https://stackoverflow.com/questions/24581098/typeerror-built-in-function-id-is-not-json-serializable
    wks = gc.create(name) #creates it in the service account, cannot be viewed
    wks.share('jaime.iko.dev@gmail.com', perm_type='user', role='writer') #need to share it to view it

'''Opens the given spreadsheet and adds a new worksheet.'''
def new_worksheet(sp_name,name):
    nrows = 10000
    ncolums = 20
    wks = gc.open(sp_name)
    wks.add_worksheet(name,nrows,ncolums)







