#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = "Yogesh Rane"
__email__ = "yrane@us.ibm.com"
__date__ = "07/27/2015"
__version__ = "1.0"

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from pprint import pprint
from weathersdk import WeatherAPI
import urllib2
import urllib
import json

def result(request):
    vals = request.GET

    if vals['city'] == "" and vals['zip'] == "":
        return HttpResponse("You have not entered anything! Please enter City or ZipCode. \
        <br><a href='../'>go back</a> ")

    if vals['city'] != "" and vals['zip'] != "":
        return HttpResponse("please enter only one of city or zipcode \
        <br><a href='../'>go back</a> ")
    curr = WeatherAPI()
    json_str = curr.current(vals['city'], vals['zip'], vals['unit'])
    data = json.loads(json_str)

    if str(data['cod']) != '200':
        return HttpResponse(str(data['message']) + "<br><a href='../'>go back</a> ")
    print data
    if vals['unit'] == 'metric':
        units = '°C'
    else:
        units = '°F'
    temp_min = str(data['main']['temp_min']) + " " + units
    temp_max = str(data['main']['temp_max']) + " " + units
    lat = data['coord']['lat']
    lon = data['coord']['lon']
    icon = "http://openweathermap.org/img/w/" + str(data['weather'][0]['icon']) + ".png"
    return render(request, 'current/result.html', {'lat': lat , 'lon' : lon, 'weather': data['weather'][0]['description'], 'temp_min' : temp_min,'temp_max' : temp_max,  'name' : data['name'], 'icon' : icon})
