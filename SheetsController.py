import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('falconpunchCreds.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open_by_url("https://docs.google.com/spreadsheets/d/1JJ9Gd9GgS5LQ6mJV2dD0pBfdCkOtY9QLkeWbiOOswn8/edit#gid=0")

def getSheet():
    return wks
