import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
json_key = json.load(open('creds.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
file = gspread.authorize(credentials)
sheet = file.open("SmashRecord").sheet1

def getFile():
    return sheet
