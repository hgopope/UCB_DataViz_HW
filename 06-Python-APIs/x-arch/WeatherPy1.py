import json
import requests as req
from citipy import citipy
import numpy.random as random
import matplotlib.pyplot as plt
import pandas as pd

apikey='cc8028c62f0742cf38eef5a866d89c64'

url = 'https://api.openweathermap.org/data/2.5/weather?q='

city_name = 'london'

my_request = req.get(url+city_name+'&APPID='+apikey)

response = my_request.json()

#print(json.dumps(response,indent=4, sort_keys=True))

print(type(response))

cities = []
citi_list=[]
info_list=[]

n_requests = 1
long_random = random.randint(-180, 180, size=n_requests)
lat_random= random.randint(-90,90, size=n_requests)

zipped=zip(long_random,lat_random)

for lat,lon in zipped:
    city=citipy.nearest_city(lat,lon)
    info_list.append(req.get(url + str(city) + '&APPID='+ apikey).json())

    print(city)

