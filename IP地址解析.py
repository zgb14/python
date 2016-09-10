#-*- coding: utf-8 -*-
import json
from urllib.request import urlopen

#http://freegeoip.net/json/50.78.253.58 
#http://freegeoip.net/json/121.97.110.145 PH

def getIPaddress(IPaddress):
    html=urlopen('http://freegeoip.net/json/'+IPaddress).read().decode('utf8')
    responsejson=json.loads(html)
    return responsejson.get('country_name')

print(getIPaddress('211.100.57.47'))
