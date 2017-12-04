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
citi_list={}
info_list=[]

n_requests = 1
long_random = random.randint(-180, 180, size=n_requests)
lat_random= random.randint(-90,90, size=n_requests)

zipped=zip(long_random,lat_random)

for lat,lon in zipped:
    cities.append(citipy.nearest_city(lat,lon))
   
    citi_list['stuff']=[]
    for city in cities:
        #name = city.city_name
        citi_list['stuff'].append(city.city_name)
    print(citi_list)

    # for names in name:
        #info_list.append(req.get(url + str(names) + '&APPID='+ apikey).json())
    #     info_list.append(names)
    # print(info_list)

    #print(req.get(url + str(name) + '&APPID='+ apikey).json())


    for citi in citi_list:
        info_list.append(req.get(url + citi + '&APPID='+ apikey).json())
        #print(citi['coord']
print(type(info_list))

# info_list_df=pd.DataFrame(info_list)
# print(info_list)

