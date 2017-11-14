

```python
import os
import json
import pandas as pd
```


```python
df=pd.read_json("purchase_data.json",orient="records")

```


```python
total_players = df['SN'].count()
player_count=pd.DataFrame({'Total Players':[total_players]})


count =len(df["Item Name"].value_counts())
average = df["Price"].mean()
total_purchases = df['Price'].count()
total_revenue=df['Price'].sum()

player_count.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>780</td>
    </tr>
  </tbody>
</table>
</div>




```python
def round2(number):
    # Rounds the number
    rounded_number = round(number, 2)
    # Creates a string
    string = str(rounded_number)
    # Returns the string
    return string
```


```python
def dollar_round2(number):
    # Creates a string of rounded number using previously defined function
    string_round2 = round2(number)
    # Add dollar sign
    string = '$'+string_round2
    return string
```


```python
purchase_analysis=pd.DataFrame({'Number of Unique Items':[count],'Average Price':[average],'Number of Purchases':[total_purchases],'Total Revenue':[total_revenue]})
purchase_analysis['Total Revenue']=purchase_analysis['Total Revenue'].map(dollar_round2)
purchase_analysis['Average Price']=purchase_analysis['Average Price'].map(dollar_round2)
o_purchase_analysis=purchase_analysis[['Number of Unique Items','Average Price','Number of Purchases',"Total Revenue"]]

o_purchase_analysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
sex=df["Gender"].value_counts()
sex
sexy=pd.DataFrame(sex)
sexy
sexy1=sexy["Gender"]*100/total_players
sexy['Percentage of Players']=sexy1

renamed_sexy=sexy.rename(columns={'Gender':'Total Count'})

organized=renamed_sexy[['Percentage of Players',"Total Count"]]
organized['Percentage of Players']=organized['Percentage of Players'].map(round2)
organized.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15</td>
      <td>633</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.44</td>
      <td>136</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.41</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
male_stat = df.loc[df["Gender"] == str('Male'),["Gender", "Price"]]
malemax=male_stat['Gender'].count()
maleaverage=male_stat['Price'].mean()
total_purchase_value = male_stat['Price'].sum()
male_stat.head()
norm=total_purchase_value/malemax

female_stat = df.loc[df["Gender"] == str('Female'),["Gender", "Price"]]
femalemax=female_stat['Gender'].count()
femaleaverage=female_stat['Price'].mean()
f_total_purchase_value = female_stat['Price'].sum()
female_stat.head()
norm_f=f_total_purchase_value/femalemax

imale_stat = df.loc[df["Gender"] == str('Other / Non-Disclosed'),["Gender", "Price"]]
imalemax=imale_stat['Gender'].count()
imaleaverage=imale_stat['Price'].mean()
i_total_purchase_value = imale_stat['Price'].sum()
norm_i=i_total_purchase_value/imalemax

```


```python
purchase_analysis_gender=pd.DataFrame({'':['Gender','Female','Male','Other/Non-Disclosed'],'Purchase Count':['',femalemax,malemax,imalemax],'Average Purchase Price':['',femaleaverage,maleaverage,imaleaverage],'Total Purchase Price':['',f_total_purchase_value,total_purchase_value,i_total_purchase_value],'Normalized totals':['',norm_f,norm,norm_i]})
purchase_analysis_gender.head()

o_purchase_analysis_gender=purchase_analysis_gender[['','Purchase Count','Average Purchase Price','Total Purchase Price','Normalized totals']]
o_purchase_analysis_gender

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Price</th>
      <th>Normalized totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Gender</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>Female</td>
      <td>136</td>
      <td>2.81551</td>
      <td>382.91</td>
      <td>2.81551</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Male</td>
      <td>633</td>
      <td>2.95052</td>
      <td>1867.68</td>
      <td>2.95052</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Other/Non-Disclosed</td>
      <td>11</td>
      <td>3.24909</td>
      <td>35.74</td>
      <td>3.24909</td>
    </tr>
  </tbody>
</table>
</div>




```python
bins=[0,10,14,19,24,29,34,39,100]
group_labels = ["<10", "10-14", "15-19",
                "20-24", "25-29", "30-34",
                "35-39","40+"]
```


```python
df['Total Count']=pd.cut(df["Age"],bins,labels=group_labels)
sex2=df["Total Count"].value_counts()
sex2
sexy2=pd.DataFrame(sex2)

count1=sexy2['Total Count'].sum()
count1
sexy1=sexy2["Total Count"]*100/count1
sexy2['Percentage of Players']=sexy1
sexy2['Percentage of Players']=sexy2['Percentage of Players'].map(round2)

sexy2
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>43.08</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>17.05</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>16.03</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>8.21</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42</td>
      <td>5.38</td>
    </tr>
    <tr>
      <th>&lt;10</th>
      <td>32</td>
      <td>4.1</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>31</td>
      <td>3.97</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>2.18</td>
    </tr>
  </tbody>
</table>
</div>




```python
male_stat_10_14 = df.loc[df["Total Count"] == str('10-14'),["Total Count", "Price"]]
male_10_14_count=male_stat_10_14['Price'].count()
male_10_14_mean=male_stat_10_14['Price'].mean()
male_10_14_sum=male_stat_10_14['Price'].sum()
norm_10_14=male_10_14_sum/male_10_14_count

male_stat_15_19 = df.loc[df["Total Count"] == str('15-19'),["Total Count", "Price"]]
male_15_19_count=male_stat_15_19['Price'].count()
male_15_19_mean=male_stat_15_19['Price'].mean()
male_15_19_sum=male_stat_15_19['Price'].sum()
norm_15_19=male_15_19_sum/male_15_19_count

male_stat_20_24 = df.loc[df["Total Count"] == str('20-24'),["Total Count", "Price"]]
male_20_24_count=male_stat_20_24['Price'].count()
male_20_24_mean=male_stat_20_24['Price'].mean()
male_20_24_sum=male_stat_20_24['Price'].sum()
norm_20_24=male_20_24_sum/male_20_24_count

male_stat_25_29 = df.loc[df["Total Count"] == str('25-29'),["Total Count", "Price"]]
male_25_29_count=male_stat_25_29['Price'].count()
male_25_29_mean=male_stat_25_29['Price'].mean()
male_25_29_sum=male_stat_25_29['Price'].sum()
norm_25_29=male_15_19_sum/male_25_29_count

male_stat_30_34 = df.loc[df["Total Count"] == str('30-34'),["Total Count", "Price"]]
male_30_34_count=male_stat_30_34['Price'].count()
male_30_34_mean=male_stat_30_34['Price'].mean()
male_30_34_sum=male_stat_30_34['Price'].sum()
norm_30_34=male_30_34_sum/male_30_34_count

male_stat_35_39 = df.loc[df["Total Count"] == str('35-39'),["Total Count", "Price"]]
male_35_39_count=male_stat_35_39['Price'].count()
male_35_39_mean=male_stat_35_39['Price'].mean()
male_35_39_sum=male_stat_35_39['Price'].sum()
norm_35_39=male_35_39_sum/male_15_19_count

male_stat_40 = df.loc[df["Total Count"] == str('40+'),["Total Count", "Price"]]
male_40_count=male_stat_40['Price'].count()
male_40_mean=male_stat_40['Price'].mean()
male_40_sum=male_stat_40['Price'].sum()
norm_40=male_40_sum/male_40_count

male_stat_10 = df.loc[df["Total Count"] == str('<10'),["Total Count", "Price"]]
male_10_count=male_stat_10['Price'].count()
male_10_mean=male_stat_10['Price'].mean()
male_10_sum=male_stat_10['Price'].sum()
norm_10=male_10_sum/male_10_count


```


```python
purchase_analysis_age=pd.DataFrame({'':['10-14','15-19','20-24','25-29','30-34','35-39','40+','<10'],'Purchase Count':[male_10_14_count,male_15_19_count,male_20_24_count,male_25_29_count,male_30_34_count,male_35_39_count,male_40_count,male_10_count],'Average Purchase Price':[male_10_14_mean,male_15_19_mean,male_20_24_mean,male_25_29_mean,male_30_34_mean,male_35_39_mean,male_40_mean,male_10_mean],'Total Purchase Price':[male_10_14_sum,male_15_19_sum,male_20_24_sum,male_25_29_sum,male_30_34_sum,male_35_39_sum,male_40_sum,male_10_sum],'Normalized totals':[norm_10_14,norm_15_19,norm_20_24,norm_25_29,norm_30_34,norm_35_39,norm_40,norm_10]})
purchase_analysis_age.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Average Purchase Price</th>
      <th>Normalized totals</th>
      <th>Purchase Count</th>
      <th>Total Purchase Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10-14</td>
      <td>2.702903</td>
      <td>2.702903</td>
      <td>31</td>
      <td>83.79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15-19</td>
      <td>2.905414</td>
      <td>2.905414</td>
      <td>133</td>
      <td>386.42</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20-24</td>
      <td>2.913006</td>
      <td>2.913006</td>
      <td>336</td>
      <td>978.77</td>
    </tr>
    <tr>
      <th>3</th>
      <td>25-29</td>
      <td>2.962640</td>
      <td>3.091360</td>
      <td>125</td>
      <td>370.33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>30-34</td>
      <td>3.082031</td>
      <td>3.082031</td>
      <td>64</td>
      <td>197.25</td>
    </tr>
    <tr>
      <th>5</th>
      <td>35-39</td>
      <td>2.842857</td>
      <td>0.897744</td>
      <td>42</td>
      <td>119.40</td>
    </tr>
    <tr>
      <th>6</th>
      <td>40+</td>
      <td>3.161765</td>
      <td>3.161765</td>
      <td>17</td>
      <td>53.75</td>
    </tr>
    <tr>
      <th>7</th>
      <td>&lt;10</td>
      <td>3.019375</td>
      <td>3.019375</td>
      <td>32</td>
      <td>96.62</td>
    </tr>
  </tbody>
</table>
</div>




```python
top_spender=df['SN'].value_counts()
top_spender.head(5)
```




    Undirrala66    5
    Mindimnya67    4
    Saedue76       4
    Sondastan54    4
    Qarwen67       4
    Name: SN, dtype: int64




```python
grouped=df.groupby('SN')
```


```python
top_spender_sum=grouped['Price'].sum()
```


```python
top_spender_table=pd.DataFrame({"Purchase Count":top_spender,"Average Purchase Price":top_spender_sum/top_spender,"Total Purchase Value":top_spender_sum})

top_spender_table['Average Purchase Price']=top_spender_table['Average Purchase Price'].map(dollar_round2)
top_spender_table['Total Purchase Value']=top_spender_table['Total Purchase Value'].map(dollar_round2)
o_top_spender_table=top_spender_table[['Purchase Count','Average Purchase Price','Total Purchase Value']]

o_top_spender_table.sort_values('Total Purchase Value',ascending=False).head(5)

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Qarwen67</th>
      <td>4</td>
      <td>$2.49</td>
      <td>$9.97</td>
    </tr>
    <tr>
      <th>Sondim43</th>
      <td>3</td>
      <td>$3.13</td>
      <td>$9.38</td>
    </tr>
    <tr>
      <th>Tillyrin30</th>
      <td>3</td>
      <td>$3.06</td>
      <td>$9.19</td>
    </tr>
    <tr>
      <th>Lisistaya47</th>
      <td>3</td>
      <td>$3.06</td>
      <td>$9.19</td>
    </tr>
    <tr>
      <th>Tyisriphos58</th>
      <td>2</td>
      <td>$4.59</td>
      <td>$9.18</td>
    </tr>
  </tbody>
</table>
</div>




```python
top_item=df['Item Name'].value_counts()
grouped1=df.groupby('Item Name')
top_item_sum=grouped1['Price'].sum()

top_item_table=pd.DataFrame({"Purchase Count":top_item,"Item Price":top_item_sum/top_item,"Total Purchase Value":top_item_sum})
top_item_table['Item Price']=top_item_table['Item Price'].map(dollar_round2)
top_item_table['Total Purchase Value']=top_item_table['Total Purchase Value'].map(dollar_round2)

o_top_item_table=top_item_table[['Purchase Count','Item Price','Total Purchase Value']]

o_top_item_table.sort_values('Purchase Count',ascending=False).head(5)


```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Final Critic</th>
      <td>14</td>
      <td>$2.76</td>
      <td>$38.6</td>
    </tr>
    <tr>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>$2.23</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>Stormcaller</th>
      <td>10</td>
      <td>$3.46</td>
      <td>$34.65</td>
    </tr>
    <tr>
      <th>Woeful Adamantite Claymore</th>
      <td>9</td>
      <td>$1.24</td>
      <td>$11.16</td>
    </tr>
  </tbody>
</table>
</div>




```python
most_profitable=o_top_item_table
most_profitable.sort_values('Total Purchase Value',ascending=False).head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Shadowsteel</th>
      <td>5</td>
      <td>$1.98</td>
      <td>$9.9</td>
    </tr>
    <tr>
      <th>Souleater</th>
      <td>3</td>
      <td>$3.27</td>
      <td>$9.81</td>
    </tr>
    <tr>
      <th>Shadow Strike, Glory of Ending Hope</th>
      <td>5</td>
      <td>$1.93</td>
      <td>$9.65</td>
    </tr>
    <tr>
      <th>Heartseeker, Reaver of Souls</th>
      <td>3</td>
      <td>$3.21</td>
      <td>$9.63</td>
    </tr>
    <tr>
      <th>Agatha</th>
      <td>5</td>
      <td>$1.91</td>
      <td>$9.55</td>
    </tr>
  </tbody>
</table>
</div>


