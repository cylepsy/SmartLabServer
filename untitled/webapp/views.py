import json
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from .twitter import Twfuncs


# used to determine whether or not to turn light on (easier than scanning a 10000 lines of a text file)
# 1,2,3 correspond to lab zones
global lightLevel1
global lightLevel2
global lightLevel3

lightLevel1 = 3.0
lightLevel2 = 3.0
lightLevel3 = 3.0
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
def sendPer(request):
    message = request.body.decode('UTF-8')
    with open('per.txt','w') as newfile:
        newfile.write(message)
        newfile.close
        return HttpResponse(status=200)
@csrf_exempt
@require_POST
def sendDoor(request):
    message = request.body.decode('UTF-8')
    if message == '-reset':
        with open('door.txt','w') as door:
            door.write(str(0))
            door.close
            return HttpResponse('reset done')

    with open('doorhistory.txt','a') as history:
        history.write(message + '\n')
        history.close

    with open('door.txt') as current:
        status  = str(message.split(',')[0])
        f = current.read().rstrip().split(',')[0]
        if status == 'ENTERING':
            now = int(f) + 1
        if status == 'LEAVING':
            now = int(f) - 1
        if now < 0:
            now = 0
        current.close
    with open('door.txt','w') as door:
        door.write(str(now))
        return HttpResponse(status=200)
@require_GET
def getDoor(request):
    with open('door.txt') as newfile:
        return HttpResponse(newfile)


@require_GET
def getPer(request):
    with open('per.txt') as newfile:
        return HttpResponse(newfile)


# gets called when sound/motion are detected
@csrf_exempt
@require_POST
def sendMotion(request):
    message = request.body.decode('UTF-8')
    with open('newmotion.txt','a') as newfile:
        newfile.write(message)
        newfile.close
    with open('motionupdate.txt','w') as mu:
        mu.write(message)
        mu.close
    # turn light on where motion/sound was detected if light level below certain threshold (3 in this case,
    # decided to hard code it as it is easier to adjust and gives us more control)
    print("Turning lights on")
    zone = message[(message.find('zone')+5)]  # figure out what zone activity was detected in
    print(zone)
    lightOn(zone)

    return HttpResponse(status=200)

@csrf_exempt
@require_GET
def getWeather(request):
    with open('weathertest.txt') as weather:
        return HttpResponse(weather)

@csrf_exempt
@require_GET
def getWeatherUp(request):
    with open('weatherupdate.txt') as weatheru:
        return HttpResponse(weatheru)

@csrf_exempt
@require_POST
def sendZone(request):
    message = request.body.decode('UTF-8')
    with open('zone.txt','w') as zone:
        zone.write(message)
        zone.close
        return HttpResponse(status=200)

@csrf_exempt
@require_GET
def getZone(request):
    with open('zone.txt') as zone:
        return HttpResponse(zone)
@csrf_exempt
@require_GET
def getKettle(request):
    with open('kettle.txt') as kettle:
        return HttpResponse(kettle)


@csrf_exempt
@require_POST
def sendKettle(request):
    message = request.body.decode('UTF-8')
    num = message.split(',')[0]
    with open('kettle.txt','w') as kettle:
        kettle.write(message)
        kettle.close
        return HttpResponse(status=200)

@csrf_exempt
@require_GET
def getMotion(request):
    with open('motionupdate.txt') as motion:
        return HttpResponse(motion)

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
        lightdata = {"c": [{"v": "Date(" + newtime + ")"}, {"v": data[2]}, {}, {}]}
        humdata = {"c": [{"v": "Date(" + newtime + ")"}, {"v": data[1]}, {}, {}]}

        global lightLevel1
        lightLevel1 = data[2]
        print(data[2])

    if data[3] == '2':
        tempdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {"v": data[0]}, {}]}
        lightdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {"v": data[2]}, {}]}
        humdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {"v": data[1]}, {}]}

        global lightLevel2
        lightLevel2 = data[2]
        print(data[2])

    if data[3] == '3':
        tempdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {}, {"v": data[0]}]}
        lightdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {}, {"v": data[2]}]}
        humdata = {"c": [{"v": "Date(" + newtime + ")"}, {}, {}, {"v": data[1]}]}

        global lightLevel3
        lightLevel3 = data[2]
        print(data[2])

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
        newfile.write(data[0])
        newfile.write(",")
        newfile.write(data[1])
        newfile.write(",")
        newfile.write(data[2])
        newfile.write(",")
        newfile.write(data[3])
        newfile.write(",")
        newfile.write(data[5])
        newfile.write(",")
        newfile.write("\n")
        newfile.close
    with open('weatherupdate.txt','w') as up:
        up.write(message)
        up.close
    tw = Twfuncs()
    tw.update('weather updates! ' + message)
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
def zone(request):
    return render(request,'webapp/zone.html')
def activity(request):
    return render(request,'webapp/activity.html')

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

#Control lights
import socket


def lightOn(zone):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('178.62.58.245', 38899)
    s.connect(server_address)

    prefix = b"APP#AC:CF:23:28:C0:20#CMD#"
    if  zone == '3' and float(lightLevel3) < 3:
        print("light level " + str(lightLevel3))
        s.send(prefix + b"490\n")
        s.send(prefix + b"c90\n")

    if zone == '2' and float(lightLevel2) < 3:
        print("light level " + str(lightLevel2))
        s.send(prefix + b"470\n")
        s.send(prefix + b"c70\n")

    if zone == '1' and float(lightLevel1) < 3:
        print("light level " + str(lightLevel1))
        s.send(prefix + b"450\n")
        s.send(prefix + b"c50\n")

    s.close()

def lightOff(zone):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('178.62.58.245', 38899)
    s.connect(server_address)

    prefix = b"APP#AC:CF:23:28:C0:20#CMD#"
    if zone == 3:
        s.send(prefix + b"4a0\n")

    if zone == 2:
        s.send(prefix + b"480\n")

    if zone == 1:
        s.send(prefix + b"460\n")

    s.close()

def allOn():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('178.62.58.245', 38899)
    s.connect(server_address)

    prefix = b"APP#AC:CF:23:28:C0:20#CMD#"
    s.send(prefix + b"420\n")

    s.close()

def allOff():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('178.62.58.245', 38899)
    s.connect(server_address)

    prefix = b"APP#AC:CF:23:28:C0:20#CMD#"

    s.send(prefix + b"410\n")

    s.close()
