

```python
#Observed Trend 1: Max temperatures appear to increase moving away from the poles 
#toward the equator, thus showing "it gets hotter."

#Observed Trend 2: Max wind speeds tend to be most extreme in northern hemishpere.

#Observed Trend#3: Humidity is likely to increase moving north in the northern hemisphere.
```


```python
import json
import requests as req
from citipy import citipy
import numpy.random as random
import matplotlib.pyplot as plt
import pandas as pd
import csv
import kdtree
import os
import seaborn
```


```python
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
```


```python
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
request_list=[]
```


```python
print('Beginning Data Retrieval')

print('------------------------')


for x in range(25):

    n_requests = 25
    long_random = random.randint(-180, 180, size=n_requests)
    lat_random= random.randint(-60,80, size=n_requests)

    zipped=zip(lat_random,long_random)

    for lat,lon in zipped:

        city=nearest_city(lat,lon)
        city__name=city.city_name
        country__code=city.country_code.upper()

        response=req.get(url + city__name +'&units=imperial'+'&APPID=' + apikey).json()
            
        try:
            temps=response['main']['temp_max']
            max_temp_list.append(temps)

            humidity=response['main']['humidity']
            humidity_list.append(humidity)

            cloudiness=response['clouds']['all']
            cloudiness_list.append(cloudiness)

            wind=response['wind']['speed']
            wind_speed_list.append(wind)
            
            date=response['dt']
            date_list.append(date)

            lat_list.append(lat)
            long_list.append(lon)

            city_list.append(city__name)
            country_list.append(country__code)
            
            print(url + city__name +'&units=imperial'+'&APPID=' + apikey)

        except:
            KeyError: 'main'
            KeyError: 'clouds'
            KeyError:  'wind'
            KeyError: 'temp_max'
            KeyError: 'humidity'
            KeyError: 'all'
            KeyError:'speed'
            KeyError:'dt'
            
```

    Beginning Data Retrieval
    ------------------------
    https://api.openweathermap.org/data/2.5/weather?q=vaini&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=srednekolymsk&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=daru&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=husavik&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=mount isa&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=prince rupert&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=dingle&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=guerrero negro&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=jamestown&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=banda aceh&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hithadhoo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=sayyan&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tocopilla&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=puerto escondido&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=guozhen&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=punta arenas&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=sao jose da coroa grande&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=port hardy&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=natal&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=butaritari&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=provideniya&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bethel&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=pangnirtung&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=yar-sale&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bluff&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ushuaia&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=yar-sale&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kodiak&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=arraial do cabo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kamina&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=pitiquito&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=mitzic&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hamilton&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hilo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=maniitsoq&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=salinopolis&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=atuona&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=albany&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=carnarvon&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=pacific grove&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=terney&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=lyngdal&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=opuwo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=chumphon&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=talnakh&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=lebu&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=lebu&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=cape town&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=northam&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tiksi&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bure&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tiksi&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=clarence town&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=saint-augustin&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kaseda&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=carnarvon&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bredasdorp&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kolondieba&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=victoria&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tasiilaq&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=washim&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=weyburn&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tasiilaq&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=sinnamary&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=jamestown&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=opuwo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=plaridel&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=cockburn town&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=biltine&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=murgab&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=yulara&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hilo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tuatapere&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=butaritari&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ixtapa&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=canto do buriti&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=axim&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=benghazi&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=esperance&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=mount isa&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=nyurba&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=nanortalik&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=malumfashi&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=zhongshu&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rawson&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=puro&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=busselton&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=barrow&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=port lincoln&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=arraial do cabo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hilo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=khatanga&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=toora-khem&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bethel&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=roma&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=mana&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=constantine&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=foumban&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=alice springs&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hilo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ayan&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hilo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=mahebourg&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ostrovnoy&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ponta do sol&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=port elizabeth&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=leshukonskoye&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hilo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=castro&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=waddan&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bonnyville&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=vikulovo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ribeira grande&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=vila velha&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=gravdal&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=mackay&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=albany&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=sulangan&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=sorland&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=port alfred&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bredasdorp&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=inirida&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=yining&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=marawi&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=palmer&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ahipara&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=namibe&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=jamestown&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ouesso&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=busselton&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=norman wells&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=puerto ayora&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=castro&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=pevek&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=mandalgovi&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=cabo san lucas&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=reinosa&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=butaritari&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=waingapu&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=klaksvik&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=namibe&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tura&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=puerto ayora&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=khatanga&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=atuona&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=broken hill&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=pacific grove&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kizema&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=upata&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=opuwo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=trairi&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=carnarvon&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=saldanha&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=nokaneng&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ushuaia&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=maceio&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ikalamavony&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hovd&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=horsham&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=turukhansk&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=mahebourg&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hasaki&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bobrovka&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=busselton&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=saldanha&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ilulissat&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tuatapere&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rawson&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kedrovyy&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bredasdorp&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=atuona&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bethel&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ribeira grande&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=saldanha&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ngama&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=plettenberg bay&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=saint-philippe&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=young&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=porto santo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tasiilaq&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=pisco&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=temyasovo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=barrow&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=makakilo city&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=beidao&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=cape town&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kapaa&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tuatapere&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=saint-philippe&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=thompson&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hilo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kavieng&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=gallup&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=portland&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=souillac&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=touros&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rio gallegos&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=faanui&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bluff&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=avarua&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=mahebourg&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=maniitsoq&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=harper&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tomatlan&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=butaritari&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=galesong&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=port hedland&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kahului&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hobart&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=pizarro&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=katsuura&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kidal&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=muros&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=sorong&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kapaa&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=cape town&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=castro&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=avarua&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=fairbanks&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=vaini&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=atuona&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=lawrenceville&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=inhambane&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=whitehorse&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=provideniya&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ust-nera&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=nerchinskiy zavod&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kahului&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rio bravo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=cape town&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=purranque&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=gazanjyk&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=la paz&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tashtyp&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=chernyshevskiy&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=guerrero negro&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=sarangani&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=coquimbo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=chuy&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=manjacaze&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=maryville&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=norman wells&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=margate&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=lodja&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=santa cruz&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=provideniya&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hobyo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=karpogory&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bluff&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=svetlogorsk&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=sudak&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kapaa&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kapaa&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=port macquarie&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=iquitos&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=mehriz&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=namibe&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=lebu&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ambon&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=pacifica&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=new norfolk&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=cabo san lucas&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=carnarvon&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=aklavik&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kalanguy&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=coari&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=souillac&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=port elizabeth&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=mahebourg&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=halifax&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=komsomolskiy&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ixtapa&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=angouleme&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=castro&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=port hedland&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tete&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=arraial do cabo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=peniche&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=clyde river&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=yelovo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=geraldton&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tasiilaq&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=torbay&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hithadhoo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=sechenovo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kaabong&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tasiilaq&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=carnarvon&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hermanus&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=sete&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hami&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=punta arenas&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=canutama&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=necochea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=arraial do cabo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=luganville&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hithadhoo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=laguna&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=maua&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=holice&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=chapais&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=mahudha&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kapaa&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=pacific grove&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=omaruru&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=busselton&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=maniitsoq&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=nome&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hermanus&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ushuaia&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=dikson&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hithadhoo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=lakes entrance&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=panama city&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=birjand&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=puerto colombia&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=los llanos de aridane&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bambous virieux&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rio grande&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=taunton&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=santa cruz del sur&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=vardo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=port-gentil&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=arraial do cabo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ukiah&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ratnagiri&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bitung&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=vaini&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=georgetown&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=port-gentil&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=cabo san lucas&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=cape town&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=umm kaddadah&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=esperance&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=east london&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=chuy&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=victoria&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=porto belo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bethel&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=grand gaube&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hovd&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bluff&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kapaa&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=lata&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=solnechnyy&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=berbera&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=suileng&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=half moon bay&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=puerto ayora&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=georgetown&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=lorengau&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=iracoubo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kalmunai&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=sorland&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=jamestown&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=mar del plata&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=cerro cama&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=lorengau&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=trincomalee&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=vao&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=carbonia&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=santa rosa&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=souillac&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=jamestown&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=kodiak&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=atuona&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=grand gaube&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=albany&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=los llanos de aridane&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=sal rei&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=fortuna&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=college&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=havre-saint-pierre&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=lompoc&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=carnarvon&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=qaanaaq&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=fortuna&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hithadhoo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=sur&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bjornevatn&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ponta do sol&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ternate&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=norman wells&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=lebu&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ancud&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=tateyama&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=nakskov&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=shima&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=flinders&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=puerto del rosario&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hobart&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=zeya&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=new norfolk&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=katsuura&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=orcopampa&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=arraial do cabo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=marystown&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bethel&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=baiyin&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=west lake stevens&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=salalah&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=port blair&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hofn&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=groton&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=sioux lookout&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=vila franca do campo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=haines junction&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=busselton&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=katsuura&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=dalvik&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=san policarpo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ahipara&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=cape town&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=benguela&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=port alfred&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=isangel&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=dmitriyevka&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=san quintin&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=vaini&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hermanus&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=victor harbor&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=puerto ayora&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rikitea&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=homer&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ponta do sol&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ribeira grande&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=hermanus&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=do gonbadan&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=saskylakh&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=mtwara&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ushuaia&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=olinda&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=bluff&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=provideniya&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=victoria&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=naze&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=geraldton&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=mahebourg&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ballina&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=isangel&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=pangkalanbuun&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=butaritari&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=wageningen&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ilulissat&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=east london&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=miandrivazo&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ponta do sol&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=ingham&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=leningradskiy&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=rawson&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64
    https://api.openweathermap.org/data/2.5/weather?q=truro&units=imperial&APPID=cc8028c62f0742cf38eef5a866d89c64



```python
city_df=pd.DataFrame({'City':city_list,'Max Temp':max_temp_list,
                      'Humidity':humidity_list,
                      'Cloudiness':cloudiness_list,
                      'Wind Speed':wind_speed_list,
                      'Latitude':lat_list,
                      'Longitude':long_list,
                      'Country':country_list,
                     'Date':date_list})

city_df.count()
```


```python
city_df.head(10)
```


```python
plt.grid(True,color='white')
plt.scatter(city_df['Latitude'],city_df['Max Temp'],
            marker='o',facecolors='green',alpha=0.75,edgecolors='blue',s=10)

plt.title('City Latitude vs. Max Temperature')
plt.xlabel('Latitude')
plt.ylabel('Max Temperature(F)')
plt.xlim(-80,120)
plt.ylim(-60,120)

ax=plt.gca()
ax.set_facecolor('lightgray')

plt.show()
```


```python
print(len(lat_list))
```


```python
plt.grid(True,color='white')
plt.scatter(city_df['Latitude'],city_df['Humidity'],
            marker='o',facecolors='green',alpha=0.75,edgecolors='blue',s=10)

plt.title('City Latitude vs. Humidity(%)')
plt.xlabel('Latitude')
plt.ylabel('Humidity (%)')
plt.xlim(-100,100)
plt.ylim(0,120)

ax=plt.gca()
ax.set_facecolor('lightgray')

plt.show()
```


```python
plt.grid(True,color='white')
plt.scatter(city_df['Latitude'],city_df['Cloudiness'],
            marker='o',facecolors='green',alpha=0.75,edgecolors='blue',s=10)

plt.title('City Latitude vs. Cloudiness (%)')
plt.xlabel('Latitude')
plt.ylabel('Cloudiness (%)')
plt.xlim(-100,100)
plt.ylim(-10,120)

ax=plt.gca()
ax.set_facecolor('lightgray')

plt.show()
```


```python
plt.grid(True,color='white')
plt.scatter(city_df['Latitude'],city_df['Wind Speed'],
            marker='o',s=10,facecolors='green',alpha=0.75,edgecolors='blue')

plt.title('City Latitude vs. Wind Speed (mph)')
plt.xlabel('Latitude')
plt.ylabel('Wind Speed (mph)')
plt.xlim(-100,100)
plt.ylim(-10,50)

ax=plt.gca()
ax.set_facecolor('lightgray')

plt.show()
```
