#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = "Yogesh Rane"
__email__ = "yrane@us.ibm.com"
__date__ = "07/27/2015"
__version__ = "1.0"

import requests
import sys, json
import urllib2, urllib

#later should be accepted as a parameter from user for authentication purposes
APPID = '355e806e0c6b3aa9c5c24c36144d073b'

class WeatherAPI(object):
# Get the current weather as per the city OR zip code values
    def current(self,city, zip, unit="metric"):
        if city != "":
            city = urllib.quote(city)
            url = "http://api.openweathermap.org/data/2.5/weather?q="
            url += city
        elif zip != "":
            url = "http://api.openweathermap.org/data/2.5/weather?zip="
            url += zip

        if unit == "metric":
            url += "&units=metric"
        elif unit == "imp":
            url += "&units=imperial"

        if APPID:
            url += "&APPID=" + APPID

        try:
            response = urllib2.urlopen(url)
            contents = response.read()
        except urllib2.HTTPError, error:
            contents = error.read()

        response.close()
        #return JSON response
        return contents
