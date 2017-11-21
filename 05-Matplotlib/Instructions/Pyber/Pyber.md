

```python
#Analysis:
#Observed Trend #1: Rural rides, unsurprisingly, have less rides per city data available, and the greatest range of average fare cost.

#Observed Trend #2: While about 78% of drivers are urban drivers, about 68% of rides were urban rides, meaning some urban drivers could be driving in suburban areas.

#Observed Trend #3: The median average fare for an urban ride is about $25, or about $5 cheaper than the average fare of about $30 for suburban rides.
```


```python
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
```


```python
file_one = os.path.join('raw_data', 'ride_data.csv')
file_two = os.path.join('raw_data', 'city_data.csv')
```


```python
file_one_df = pd.read_csv(file_one)
file_two_df = pd.read_csv(file_two)
```


```python
file_one_df = pd.read_csv(file_one, encoding="utf-8")
file_two_df = pd.read_csv(file_two, encoding="utf-8")
```


```python
merge_table = pd.merge(file_one_df, file_two_df,on="city")
merge_table=merge_table.sort_values('city',ascending=True)
merge_table.count()
```




    city            2407
    date            2407
    fare            2407
    ride_id         2407
    driver_count    2407
    type            2407
    dtype: int64




```python
merge_table_rural=merge_table.loc[merge_table['type']=='Rural',:]
merge_table_suburban=merge_table.loc[(merge_table['type']=='Suburban')]
merge_table_urban=merge_table.loc[(merge_table['type']=='Urban')]
```


```python
unique_rural=merge_table_rural['city'].unique()
unique_suburban=merge_table_suburban['city'].unique()
unique_urban=merge_table_urban['city'].unique()
```


```python
driver_count_rural=file_two_df.loc[file_two_df['type']=='Rural',:]
driver_count_rural=ride_count_xyz.sort_values(['city'],ascending=True)

driver_count_suburban=file_two_df.loc[file_two_df['type']=='Suburban',:]
driver_count_suburban=ride_count_xyz.sort_values(['city'],ascending=True)

driver_count_urban=file_two_df.loc[file_two_df['type']=='Urban',:]
driver_count_urban=ride_count_xyz.sort_values(['city'],ascending=True)
```


```python
city_rural=merge_table_rural.groupby('city')
ride_count_rural=city_rural['fare'].count()
city_suburban=merge_table_suburban.groupby('city')
ride_count_suburban=city_suburban['fare'].count()
city_urban=merge_table_urban.groupby('city')
ride_count_urban=city_urban['fare'].count()
```


```python
rural_df=pd.DataFrame(ride_count_rural)
rural_df['try this']=''
rural_df['driver city']=unique_rural
rural_df['total fare']=''
rural_df['driver count']=''

rural_fare_sum=city_rural['fare'].sum()
rural_df['total fare']=rural_fare_sum
average_rural=rural_fare_sum/ride_count_rural
rural_df['try this']=average_rural
```


```python
suburban_df=pd.DataFrame(ride_count_suburban)
suburban_df['try this']=''
rural_df['driver count']=''
rural_df['total fare']=''

suburban_fare_sum=city_suburban['fare'].sum()
suburban_df['total fare']=suburban_fare_sum
average_sub=suburban_fare_sum/ride_count_suburban
suburban_df['try this']=average_sub
```


```python
urban_df=pd.DataFrame(ride_count_urban)
urban_df['try this']=''
rural_df['driver count']=''
rural_df['total fare']=''

urban_fare_sum=city_urban['fare'].sum()
average_urban=urban_fare_sum/ride_count_urban
urban_df['try this']=average_urban
```


```python
plt.hlines(10,50,100,alpha=1)

plt.scatter(rural_df['fare'], rural_df['try this'], marker="o", facecolor="gold",edgecolors='black',sizes=driver_count_rural['driver_count']*25,alpha=0.75, linewidth=1)
plt.scatter(ride_count_suburban, average_sub, marker="o", facecolor="#87CEFA",edgecolors='black',sizes=driver_count_suburban['driver_count']*25,alpha=0.75, linewidth=1)
plt.scatter(ride_count_urban, average_urban, marker="o", facecolor="#F08080",edgecolors='black',sizes=driver_count_urban['driver_count']*25,alpha=0.75, linewidth=1)

plt.ylim(15,55)
plt.xlim(0,70)
plt.title("Pyber Ride Sharing Data (2016)")
plt.xlabel("Total Number of Rides (Per City)")
plt.ylabel("Average Fare ($)")

plt.text(72,35,'Note:')
plt.text(72,32,'Circle size correlates to driver count per city.')
plt.legend()
plt.rcParams['axes.facecolor'] = 'lightgray'

plt.grid()
plt.show()
```


![png](output_13_0.png)



```python
#break
```


```python
merge_table_rural=merge_table.loc[(merge_table['type']=='Rural')]
merge_table_suburban=merge_table.loc[(merge_table['type']=='Suburban')]
merge_table_urban=merge_table.loc[(merge_table['type']=='Urban')]

rural_sum=merge_table_rural['fare'].sum()
suburban_sum=merge_table_suburban['fare'].sum()
urban_sum=merge_table_urban['fare'].sum()
total_sum=merge_table['fare'].sum()
```


```python
sizes_fare=[rural_sum/total_sum,suburban_sum/total_sum,urban_sum/total_sum]
```


```python
labels = ['Rural','Suburban','Urban']
plt.title('% of Total Fares by City Type')
colors=['Gold', '#87CEFA', '#F08080']
explode=[0,0,0.1]
plt.pie(sizes_fare,labels=labels,colors=colors,explode=explode,autopct='{0:1.1f}%'.format,shadow=True,startangle=140)
```




    ([<matplotlib.patches.Wedge at 0x121680940>,
      <matplotlib.patches.Wedge at 0x121688da0>,
      <matplotlib.patches.Wedge at 0x1216842b0>],
     [<matplotlib.text.Text at 0x121680748>,
      <matplotlib.text.Text at 0x12168dfd0>,
      <matplotlib.text.Text at 0x1216850b8>],
     [<matplotlib.text.Text at 0x121688400>,
      <matplotlib.text.Text at 0x12168d588>,
      <matplotlib.text.Text at 0x1216855f8>])




```python
plt.show()
```


![png](output_18_0.png)



```python
#break
```


```python
rural_sum_ride=merge_table_rural['ride_id'].sum()
suburban_sum_ride=merge_table_suburban['ride_id'].sum()
urban_sum_ride=merge_table_urban['ride_id'].sum()
total_sum_ride=merge_table['ride_id'].sum()
```


```python
sizes_ride=[rural_sum_ride/total_sum_ride,suburban_sum_ride/total_sum_ride,urban_sum_ride/total_sum_ride]
```


```python
labels = ['Rural','Suburban','Urban']
plt.title('% of Total Rides by City Type')
size_rural=int(city_type_count_df.loc['Rural'])
size_suburban=int(city_type_count_df.loc['Suburban'])
size_urban=int(city_type_count_df.loc['Urban'])
sizes=[sizes_fare_ride,size_suburban,size_urban]
colors=['Gold', '#87CEFA', '#F08080']
explode=[0,0,0.1]
plt.pie(sizes_ride,labels=labels,colors=colors,explode=explode,autopct='{0:1.1f}%'.format,shadow=True,startangle=140)
```




    ([<matplotlib.patches.Wedge at 0x121153a58>,
      <matplotlib.patches.Wedge at 0x12116e2e8>,
      <matplotlib.patches.Wedge at 0x121154a58>],
     [<matplotlib.text.Text at 0x12116d7f0>,
      <matplotlib.text.Text at 0x12116ef60>,
      <matplotlib.text.Text at 0x121184860>],
     [<matplotlib.text.Text at 0x12116dd30>,
      <matplotlib.text.Text at 0x1211544e0>,
      <matplotlib.text.Text at 0x121184da0>])




```python
plt.show()
```


![png](output_23_0.png)



```python
#break
```


```python
city_table_rural=file_two_df.loc[(file_two_df['type']=='Rural')]
city_table_suburban=file_two_df.loc[(file_two_df['type']=='Suburban')]
city_table_urban=file_two_df.loc[(file_two_df['type']=='Urban')]

rural_driver=city_table_rural['driver_count'].sum()
suburban_driver=city_table_suburban['driver_count'].sum()
urban_driver=city_table_urban['driver_count'].sum()
total_driver=file_two_df['driver_count'].sum()
```


```python
sizes_driver=[rural_driver/total_driver,suburban_driver/total_driver,urban_driver/total_driver]
```


```python
labels = ['Rural','Suburban','Urban']
plt.title('% of Total Drivers by City Type')
colors=['Gold', '#87CEFA', '#F08080']
explode=[0,0,0.1]
plt.pie(sizes_driver,labels=labels,colors=colors,explode=explode,autopct='{0:1.1f}%'.format,shadow=True,startangle=140)
```




    ([<matplotlib.patches.Wedge at 0x121084518>,
      <matplotlib.patches.Wedge at 0x121063dd8>,
      <matplotlib.patches.Wedge at 0x1210736d8>],
     [<matplotlib.text.Text at 0x121063320>,
      <matplotlib.text.Text at 0x121064be0>,
      <matplotlib.text.Text at 0x12106c4e0>],
     [<matplotlib.text.Text at 0x121063860>,
      <matplotlib.text.Text at 0x121073160>,
      <matplotlib.text.Text at 0x12106ca20>])




```python
plt.show()
```


![png](output_28_0.png)

