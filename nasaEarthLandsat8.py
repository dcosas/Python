#Usage: Call getImages(), optional: specify start date, longitude, latitude and noOfDaysToIncrement
#Result: Received images will be saved for each available data in the following format: timestamp.jpg (e.g. 2015-11-01T22-55-05)
#Limitations: Landsat8 sattelite is operational since april 2013, data before might not be available. New data is received each 16 days.
#KnownIssues: if any command fails, there is no retry or error handling

nasaApiKey = 'DEMO_KEY'

import urllib.request
import json
import time
import datetime
from datetime import date

urlRequest = 'https://api.nasa.gov/planetary/earth/imagery?lon=21.245113&lat=45.732711&date=2015-08-01&cloud_score=False&api_key=DEMO_KEY'
longitude = 21.245113
latitude = 45.732711
dateYear = 2015
dateMonth = 11
dateDay = 1
currentDate = date(2015, 1, 1)


def setStartDate(cYear, cMonth, cDay):
    global currentDate
    currentDate = date(cYear, cMonth, cDay)
    

def dateIncrement(daysToIncrement):
    global currentDate
    currentDate = currentDate + datetime.timedelta(daysToIncrement)

def test(cycles=100):
    
    for i in range(cycles):
        dateIncrement(30)
        print(currentDate)

def buildUrlForEarthAPI(_date, longitude, latitude):
    global urlRequest    
    urlRequest = 'https://api.nasa.gov/planetary/earth/imagery?lon=' + longitude + '&lat=' + latitude + '&date=' + str(_date) + '&cloud_score=False&api_key='+ nasaApiKey
    print(urlRequest)

def requestUrl(req):
    ret = urllib.request.urlopen(req)
    stringRet = ret.read().decode('utf-8')
    print(stringRet)
    parsedJson = json.loads(stringRet)
    imgurl = parsedJson['url']
    img = urllib.request.urlopen(imgurl)
    dateString = parsedJson['date']
    dateString = dateString.replace(':','-')
    output = open(dateString+'.jpg',"wb")
    output.write(img.read())
    output.close()

def getImages(year=2014, month=11, day=1, lon='21.245113', lat='45.732711', noOfDaysToIncrement=16, maxNoOfImages=100):
    global currentDate
    global urlRequest
    setStartDate(year,month,day)
    for i in range(maxNoOfImages):
        buildUrlForEarthAPI(currentDate, lon, lat);
        requestUrl(urlRequest)
        dateIncrement(noOfDaysToIncrement)
        


    
