'''This library is used to interface raspberry pi with our own google sheet'''


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
    return wks.add_worksheet(name,nrows,ncolums)
    
'''Inserts a row at a given index in a worksheet inside a spreadsheet. If the worksheet
does not exists, creates a new one and imports first row from a given one'''   
def insert_row(sp_name,worksheet_name,row_index,row):
   sp = gc.open(sp_name)
   try:
       wks = sp.worksheet(worksheet_name)
   except gspread.exceptions.WorksheetNotFound: #if the worksheet is not created
       #Copy row from a given worksheet to the new one
       first_row = sp.worksheet("iko6").row_values(1,"UNFORMATTED_VALUE")
       print str(first_row)
       wks = new_worksheet(sp_name,worksheet_name)
       insert_row(sp_name,worksheet_name,1,first_row)
   wks.insert_row(row,row_index)


    




