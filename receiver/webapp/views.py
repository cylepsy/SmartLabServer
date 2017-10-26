import json

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


# Create your views here.

@csrf_exempt
@require_POST
def hello(request):
    jsondata = request.body
    data = json.loads(jsondata)
    
# use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("newtest").get_worksheet(3)
    sheet2 = client.open("newtest").get_worksheet(1)
    sheet3 = client.open("newtest").get_worksheet(2)
    newtime = rfcToGen(data['time'])
    row = [newtime,data['temp']]
    row2 = [newtime,data['humid']]
    row3 = [newtime,data['light']]

    sheet.append_row(row)
    sheet2.append_row(row2)
    sheet3.append_row(row3)
    
    data = {"c":[{"v":newtime,"f":None},{"v":data['temp'],"f":None}]}


    with open('data.json', 'a') as outfile:
        json.dump(data, outfile)
    
    return HttpResponse(status=200)

@require_POST
def hello2(request):
    jsondata = request.body
    data = json.loads(jsondata)
    
    newtime = rfcToGen(data['time'])
    row = [newtime,data['temp'],data['humid'],data['light']]
    
    sheet.append_row(row)   
    
    


    with open('data.json', 'a') as outfile:
        json.dump(data, outfile)
    
    return HttpResponse(status=200)

def index(request):
    return render(request,'webapp/index.html')
def chart(request):
    return render(request,'webapp/show.html')

def nchart(request):
    return render(request,'webapp/show2.html')
def about(request):
    return render(request,'webapp/about.html')

def rfcToGen(rfc):
    rfc3399 = rfc
    date = rfc3399.split('T')
    year = date[0].split('-')[0]
    
    month = date[0].split('-')[1]
    day = date[0].split('-')[2]
    hour = date[1].split(':')[0]
    minute = date[1].split(':')[1]
    second = date[1].split(':')[2].split('.')[0]
    new = year + "/" + month + "/" + day + " " + date[1].split(".")[0]
    
    
    
    return new



