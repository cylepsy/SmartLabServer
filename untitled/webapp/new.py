import json
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET


# Create your views here.

@csrf_exempt
@require_POST
def receive(request):
    jsondata = request.body
    data = json.loads(jsondata)
    newtime = rfcToGen(data['time'])


    if data['datatype'] == 'Motion':
        motiondata = data['motion']
        file_handler = open ("motion.txt", 'a')
        file_handler.write(motiondata + ' ' + newtime + '\n')
        file_handler.close()
        return HttpResponse(status=200)

    if data['key'] == '1':
        tempdata = {"c": [{"v": "Date(" + newtime + ")"}, {"v": data['temp']}, {}, {}]}
        lightdata = {"c": [{"v": "Date(" + newtime + ")"}, {"v": data['light']}, {}, {}]}
        humdata = {"c": [{"v": "Date(" + newtime + ")"}, {"v": data['humid']}, {}, {}]}

    if data['key'] == '2':
        tempdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {"v": data['temp']}, {}]}
        lightdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {"v": data['light']}, {}]}
        humdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {"v": data['humid']}, {}]}

    if data['key'] == '3':
        tempdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {}, {"v": data['temp']}]}
        lightdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {}, {"v": data['light']}]}
        humdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {}, {"v": data['humid']}]}

    with open('temp.json', 'a') as outfile:
        json.dump(data, outfile)

    with open('light.json', 'a') as outfile:
        json.dump(lightdata, outfile)
    with open('hum.json', 'a') as outfile:
        json.dump(humdata, outfile)
    file_handler = open('temp.json', 'a')
    file_handler.write(",")
    file_handler.close()
    file_handler = open('light.json', 'a')
    file_handler.write(",")
    file_handler.close()
    file_handler = open('hum.json', 'a')
    file_handler.write(",")
    file_handler.close()

    with open('webapp/static/webapp/data.json', 'rb+') as outfile:
        outfile.seek(-2, os.SEEK_END)
        outfile.truncate()
        outfile.close()
    with open('webapp/static/webapp/data.json', 'a') as outfile:
        json.dump(tempdata, outfile)
        outfile.write(', ]}')
        outfile.close()

    with open('webapp/static/webapp/humidity.json', 'rb+') as outfile:
        outfile.seek(-2, os.SEEK_END)
        outfile.truncate()
        outfile.close()
    with open('webapp/static/webapp/humidity.json', 'a') as outfile:
        json.dump(humdata, outfile)
        outfile.write(', ]}')
        outfile.close()

    with open('webapp/static/webapp/light.json', 'rb+') as outfile:
        outfile.seek(-2, os.SEEK_END)
        outfile.truncate()
        outfile.close()
    with open('webapp/static/webapp/light.json', 'a') as outfile:
        json.dump(lightdata, outfile)
        outfile.write(', ]}')
        outfile.close()

    return HttpResponse(status=200)

@require_GET
def getmotion(request):
    to_json = {
        "key1": "value1",
        "key2": "value2"}
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')


@require_GET
def gethum(request):
    with open('webapp/static/webapp/humidity.json') as json_data:
        return HttpResponse(json_data)

@require_GET
def gettemp(request):
    with open('webapp/static/webapp/data.json') as json_data:
        return HttpResponse(json_data)

@require_GET
def getlight(request):
    with open('webapp/static/webapp/light.json') as json_data:
        return HttpResponse(json_data)


@csrf_exempt
@require_POST
def sendMotion(request):
    message = request.body.decode('UTF-8')
    with open('newmotion.txt','a') as newfile:
        newfile.write(message)
        newfile.close
        return HttpResponse(status=200)

@csrf_exempt
@require_GET
def getWeather(request):
    with open('weathertest.txt') as weather:
        return HttpResponse(weather)


    

@csrf_exempt
@require_POST
def sendWeather(request):
    message = request.body.decode('UTF-8')
    data = message.split(',')
    timestr = data[4]
    elements  = timestr.split('-')
    newtime = ""
    for ele in elements:
        newtime = newtime + ele + ',' 
    newtime = newtime[:-1]
    with open('www.txt','a') as nfile:
        for temp in data:
            nfile.write(temp)
            nfile.write(",")
        nfile.write(newtime)
        nfile.write("\n")
        nfile.close
    if data[3] == '1':
        tempdata = {"c": [{"v": "Date(" + newtime + ")"}, {"v": data[0]}, {}, {}]}
        lightdata = {"c": [{"v": "Date(" + newtime + ")"}, {"v": data[1]}, {}, {}]}
        humdata = {"c": [{"v": "Date(" + newtime + ")"}, {"v": data[2]}, {}, {}]}

    if data[3] == '2':
        tempdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {"v": data[0]}, {}]}
        lightdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {"v": data[1]}, {}]}
        humdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {"v": data[2]}, {}]}

    if data[3] == '3':
        tempdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {}, {"v": data[0]}]}
        lightdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {}, {"v": data[1]}]}
        humdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {}, {"v": data[2]}]}

    with open('webapp/static/webapp/data.json', 'rb+') as outfile:
        outfile.seek(-2, os.SEEK_END)
        outfile.truncate()
        outfile.close()
    with open('webapp/static/webapp/data.json', 'a') as outfile:
        json.dump(tempdata, outfile)
        outfile.write(', ]}')
        outfile.close()

    with open('webapp/static/webapp/humidity.json', 'rb+') as outfile:
        outfile.seek(-2, os.SEEK_END)
        outfile.truncate()
        outfile.close()
    with open('webapp/static/webapp/humidity.json', 'a') as outfile:
        json.dump(humdata, outfile)
        outfile.write(', ]}')
        outfile.close()

    with open('webapp/static/webapp/light.json', 'rb+') as outfile:
        outfile.seek(-2, os.SEEK_END)
        outfile.truncate()
        outfile.close()
    with open('webapp/static/webapp/light.json', 'a') as outfile:
        json.dump(lightdata, outfile)
        outfile.write(', ]}')
        outfile.close()





    
    with open('weathertest.txt','a') as newfile:
        for temp in data:
            newfile.write(temp)
            newfile.write(",")
        newfile.write("\n")
        newfile.close
        return HttpResponse(status=200)
# Convert RFC timestamp to General
def append(data):
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sht = client.open('SCC330data')
    tempsheet = sht.worksheet('Temp')
    humsheet = sht.worksheet('Humidity')
    lightsheet = sht.worksheet('Light')

    newtime = rfcToGen(data['time'])
    if data['key'] == '3':
        row = [newtime, '', '' , data['temp']]
        row2 = [newtime, '', '' , data['humid']]
        row3 = [newtime, '', '' , data['light']]
    if data['key'] == '2':
        row = [newtime, '', data['temp']]
        row2 = [newtime, '', data['humid']]
        row3 = [newtime, '', data['light']]
    if data['key'] == '1':
        row = [newtime, data['temp']]
        row2 = [newtime, data['humid']]
        row3 = [newtime,  data['light']]

    tempsheet.append_row(row)
    humsheet.append_row(row2)
    lightsheet.append_row(row3)

def chart(request):
    return render(request,'webapp/show.html')


def index(request):
    return render(request,'webapp/index.html')

def about(request):
    return render(request,'webapp/about.html')
def get(request):
    count = 0
    Liste = []
    for line in reversed(list(open("motion.txt"))):
        count = count + 1
        line1 = line.rstrip()
        Liste.append(line1)
        if count > 5:
            break
    jsonfile = json.dumps(Liste)
    return render(request,'webapp/get.html',{'line1':Liste(0),'line2':Liste(1),'line3':Liste(2)}) 

def rfcToGen(rfc):
    rfc3399 = rfc
    date = rfc3399.split('T')
    year = date[0].split('-')[0]

    month = date[0].split('-')[1]
    day = date[0].split('-')[2]
    hour = date[1].split(':')[0]
    minute = date[1].split(':')[1]
    second = date[1].split(':')[2].split('.')[0]
    new = year + "," + month + "," + day + "," + hour + ',' + minute + ',' + second
    return new
