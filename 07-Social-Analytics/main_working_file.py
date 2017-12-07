# Dependencies
import tweepy
import time
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
import matplotlib.pyplot as plt
import pandas as pd

# Twitter API Keys
consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"

# Twitter Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

source_account=[]
tweet_text=[]
tweet_date=[]
compound_list=[]
pos_list=[]
neu_list=[]
neg_list=[]

target_term=['@bbc','@abc','@sputnikInt','@cnn','@RT_com','@foxnews']

for target in target_term:

    public_tweets=api.user_timeline(target, count=1, result_type='recent')

    for tweet in public_tweets:
        
        source_acc=tweet['user']['name']
        source_account.append(source_acc)

        text_acc=tweet['text']
        tweet_text.append(text_acc)

        created_acc=tweet['created_at']
        tweet_date.append(tweet)

        scores=analyzer.polarity_scores(text_acc)
        compound=scores['compound']
        pos=scores['pos']
        neu=scores['neu']
        neg=scores['neg']

        compound_list.append(compound)
        pos_list.append(pos)
        neu_list.append(neu)
        neg_list.append(neg)

tweet_df=pd.DataFrame({'Source Account':source_account,
'Text':tweet_text,'Date':tweet_date,'Compound':compound_list,
'Positive':pos_list,'Neutral':neu_list,"Negative":neg_list})
print(tweet_df)


# * Pull last 100 tweets from each outlet.
# * Perform a sentiment analysis with the compound, positive, neutral, and negative scoring for each tweet. 
# * Pull into a DataFrame the tweet's source acount, its text, its date, and its compound, positive, neutral, and negative sentiment scores.
# * Export the data in the DataFrame into a CSV file.
# * Save PNG images for each plot.


# sentiments_df.columns=['scores_1']
# sentiments_df.reset_index(level=0,inplace=True)

# print(sentiments_df)
# sentiments_df.plot(kind='scatter',x='index',y='scores_1')
# plt.axhline(y=0)

# plt.show()