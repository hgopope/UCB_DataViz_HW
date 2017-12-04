import json
import requests as req
from citipy import citipy
import numpy.random as random
import matplotlib.pyplot as plt
import pandas as pd
#import openweathermapy.core as ow
import csv
import kdtree
import os

class City:
    '''
    City wraps up the info about a city, including its name, coordinates,
    and belonging country.
    '''
    def __init__(self, city_name, country_code):
        self.city_name = city_name
        self.country_code = country_code

# load the city data up
#_current_dir, _current_filename = os.path.split(__file__)
_world_cities_csv_path = os.path.join('worldcities.csv')
_world_cities_kdtree = kdtree.create(dimensions=2)
WORLD_CITIES_DICT = {}

with open(_world_cities_csv_path, 'r') as csv_file:
    cities = csv.reader(csv_file)

    # discard the headers
    cities.__next__()

    # populate geo points into kdtree
    for city in cities:
        city_coordinate_key = (float(city[2]), float(city[3]))
        _world_cities_kdtree.add(city_coordinate_key)
        c = City(city[1], city[0])
        WORLD_CITIES_DICT[city_coordinate_key] = c

def nearest_city(latitude, longitude):
    nearest_city_coordinate = _world_cities_kdtree.search_nn((latitude, longitude, ))
    return WORLD_CITIES_DICT[nearest_city_coordinate[0].data]

apikey='cc8028c62f0742cf38eef5a866d89c64'
url = 'https://api.openweathermap.org/data/2.5/weather?q='

city_list=[]
cloudiness_list=[]
country_list=[]
date_list=[]
humidity_list=[]
lat_list=[]
long_list=[]
max_temp_list=[]
wind_speed_list=[]

n_requests = 10
long_random = random.randint(-180, 180, size=n_requests)
lat_random= random.randint(-90,90, size=n_requests)

zipped=zip(lat_random,long_random)

for lat,lon in zipped:

    city=nearest_city(lat,lon)
    city__name=city.city_name
    print(city__name)
    city_list.append(city__name)

    #params={'appid':apikey,'q':'city__name','units':'imperial'}

    #response1=ow.get_current(city__name,units='imperial',appid=apikey)
    
    # response_1=req.get(url,params=params)
    # print(type(response_1))
    # print(json.dumps(response_1, indent=4))
    # response=response_1.json()
    # print(response)
    
    response=req.get(url + city__name +'&units=imperial'+'&APPID=' + apikey).json()
    #print(json.dumps(response, indent=4))
    
    try:

        temps=response['main']['temp_max']
        max_temp_list.append(temps)

        humidity=response['main']['humidity']
        humidity_list.append(humidity)

        cloudiness=response['clouds']['all']
        cloudiness_list.append(cloudiness)

        wind=response['wind']['speed']
        wind_speed_list.append(wind)

        lat_list.append(lat)
    
    except:

        KeyError: 'main'
        KeyError: 'clouds'
        KeyError:  'wind'

city_df=pd.DataFrame({'City':city_list,'Max Temp':max_temp_list,'Humidity':humidity_list,'Cloudiness':cloudiness_list,'Wind Speed':wind_speed_list,'Latitude':lat_list})
print(city_df)
# city_df.plot(kind='scatter',x='Latitiude',y='Max Temp')
# plt.axhline(y=0)

# plt.show()

