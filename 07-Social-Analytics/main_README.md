

```python
import tweepy
import time
import datetime
from datetime import *
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
import matplotlib.pyplot as plt
import pandas as pd
import os
import seaborn

consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```


```python
source_account=[]
tweet_text=[]
tweet_date=[]
compound_list=[]
pos_list=[]
neu_list=[]
neg_list=[]

target_term=['@bbc','@abc','@cnn','@RT_com','@foxnews']
```


```python
for target in target_term:

    public_tweets=api.user_timeline(target, count=100, result_type='recent')

    for tweet in public_tweets:
        
        source_acc=tweet['user']['name']
        source_account.append(source_acc)

        text_acc=tweet['text']
        tweet_text.append(text_acc)

        created_acc=tweet['created_at']
        tweet_date.append(created_acc)

        scores=analyzer.polarity_scores(text_acc)
        compound=scores['compound']
        pos=scores['pos']
        neu=scores['neu']
        neg=scores['neg']

        compound_list.append(compound)
        pos_list.append(pos)
        neu_list.append(neu)
        neg_list.append(neg)
```


```python
tweet_df=pd.DataFrame({'Source Account':source_account,
'Text':tweet_text,'Date':tweet_date,'Compound':compound_list,
'Positive':pos_list,'Neutral':neu_list,"Negative":neg_list})
tweet_df=tweet_df[['Source Account', 'Date','Text','Negative','Neutral','Positive','Compound']]
tweet_df.head(10)
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
      <th>Source Account</th>
      <th>Date</th>
      <th>Text</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Compound</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BBC</td>
      <td>Thu Dec 07 18:00:02 +0000 2017</td>
      <td>Well, the intention was there. 😂\nVia @BBCTheS...</td>
      <td>0.000</td>
      <td>0.769</td>
      <td>0.231</td>
      <td>0.2732</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BBC</td>
      <td>Thu Dec 07 17:30:10 +0000 2017</td>
      <td>The first Scrooge: How the world’s best-known ...</td>
      <td>0.177</td>
      <td>0.823</td>
      <td>0.000</td>
      <td>-0.4215</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BBC</td>
      <td>Thu Dec 07 17:00:06 +0000 2017</td>
      <td>🏂 These prosthetic feet are designed specifica...</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BBC</td>
      <td>Thu Dec 07 16:00:04 +0000 2017</td>
      <td>🎤😍 Still can't get over @RitaOra's #SLFN perfo...</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BBC</td>
      <td>Thu Dec 07 14:00:08 +0000 2017</td>
      <td>Embracing me-time, onesie-wearing and cheeky s...</td>
      <td>0.000</td>
      <td>0.781</td>
      <td>0.219</td>
      <td>0.6369</td>
    </tr>
    <tr>
      <th>5</th>
      <td>BBC</td>
      <td>Thu Dec 07 13:39:52 +0000 2017</td>
      <td>RT @BBCTwo: This is why you should NEVER mess ...</td>
      <td>0.143</td>
      <td>0.857</td>
      <td>0.000</td>
      <td>-0.3612</td>
    </tr>
    <tr>
      <th>6</th>
      <td>BBC</td>
      <td>Thu Dec 07 13:30:01 +0000 2017</td>
      <td>Can an employer demand that you go to work nak...</td>
      <td>0.089</td>
      <td>0.911</td>
      <td>0.000</td>
      <td>-0.2168</td>
    </tr>
    <tr>
      <th>7</th>
      <td>BBC</td>
      <td>Thu Dec 07 13:00:07 +0000 2017</td>
      <td>Passers-by in this Belgian town have been aski...</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>BBC</td>
      <td>Thu Dec 07 12:30:06 +0000 2017</td>
      <td>🎄🍿 A snack to bring a little joy to your world...</td>
      <td>0.000</td>
      <td>0.788</td>
      <td>0.212</td>
      <td>0.5434</td>
    </tr>
    <tr>
      <th>9</th>
      <td>BBC</td>
      <td>Thu Dec 07 12:00:08 +0000 2017</td>
      <td>Why I’m not going to any Christmas parties thi...</td>
      <td>0.000</td>
      <td>0.816</td>
      <td>0.184</td>
      <td>0.4019</td>
    </tr>
  </tbody>
</table>
</div>




```python

t1=tweet_df.iloc[1,1]
t2 = datetime.strptime(t1,'%a %b %d %H:%M:%S +0000 %Y')
year=str(t2.year)
month=str(t2.month)
day=str(t2.day)
```


```python
BBC_df=tweet_df.loc[tweet_df['Source Account']=='BBC']
ABC_df=tweet_df.loc[tweet_df['Source Account']=='ABC News']
CNN_df=tweet_df.loc[tweet_df['Source Account']=='CNN']
RT_df=tweet_df.loc[tweet_df['Source Account']=='RT']
Fox_df=tweet_df.loc[tweet_df['Source Account']=='Fox News']

plt.grid(True,color='white')

plt.scatter(BBC_df.index,BBC_df['Compound'] ,
            marker='o',facecolors='green',alpha=0.75,edgecolors='blue',s=50)
plt.scatter(ABC_df.index-100,ABC_df['Compound'] ,
            marker='o',facecolors='blue',alpha=0.75,edgecolors='blue',s=50)
plt.scatter(CNN_df.index-200,CNN_df['Compound'] ,
            marker='o',facecolors='red',alpha=0.75,edgecolors='blue',s=50)
plt.scatter(RT_df.index-300,RT_df['Compound'] ,
            marker='o',facecolors='green',alpha=0.75,edgecolors='blue',s=50)
plt.scatter(Fox_df.index-400,Fox_df['Compound'] ,
            marker='o',facecolors='yellow',alpha=0.75,edgecolors='blue',s=50)

plt.title('Sentiment Analysis of Media Tweets'+' ('+month+'/'+day+'/'+year+')')
plt.xlabel('Tweets Ago')
plt.ylabel('Tweet Polarity')
plt.xlim(110,-50)
plt.ylim(-1.2,1.2)
legend_var=tweet_df['Source Account'].unique()
plt.legend(legend_var,loc='best')
ax=plt.gca()
ax.set_facecolor('lightgray')
plt.savefig('Tweet_Sentiment_Scatter.png')
plt.show()
```


![png](output_5_0.png)



```python
bbc_mean=round(BBC_df['Compound'].mean(),3)
abc_mean=round(ABC_df['Compound'].mean(),3)
cnn_mean=round(CNN_df['Compound'].mean(),3)
rt_mean=round(RT_df['Compound'].mean(),3)
fox_mean=round(Fox_df['Compound'].mean(),3)

mean_df=pd.DataFrame({'BBC':bbc_mean,
'ABC':abc_mean,'CNN':cnn_mean,'RT':rt_mean,'Fox News':fox_mean},index=[0])

mean_df.plot(kind='bar',alpha=0.65)
plt.title('Overall Media Sentiment based on Twitter'+' ('+month+'/'+day+'/'+year+')')
plt.ylabel('Tweet Polarity')
plt.xlabel(mean_df)
plt.tight_layout()
plt.savefig('Overall_Sentiment_Bar.png')
plt.show()

```


![png](output_6_0.png)



```python
new_path=os.path.join('Tweet_Sentiment.csv')
tweet_df.to_csv(new_path,encoding='utf-8',index=False,header=True)
```
