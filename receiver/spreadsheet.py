import gspread
from oauth2client.service_account import ServiceAccountCredentials
 
 
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
 
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("scc330 test").sheet1
sheet.resize(1)

row = ["test","test","test"]
sheet.append_row(row)





list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
