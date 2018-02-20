import requests
from bs4 import BeautifulSoup as bs
import os
import pymongo
from splinter import Browser
import pandas as pd


def scrape():

    mars = {}
    browser = Browser('chrome')

# news - title

    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    title_list = []
    news_title = soup.find_all('div', class_='content_title')
    for paragraph in news_title:
        title_list.append(paragraph.text)
    title=title_list[0]

# news - facts

    para_list = []
    news_p = soup.find_all('div',class_='image_and_description_container')
    for paragraph in news_p:
        para_list.append(paragraph.text)
    facts=para_list[0]

# images

    browser = Browser('chrome', headless=False)
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    html2 = browser.html
    soup2 = bs(html2, 'html.parser')

    featured_image = soup2.find_all('div', class_='carousel_items')
    featured_image_url = "https://www.jpl.nasa.gov/" + str(featured_image).split("url('/")[1].split("');")[0]

# weather tweet

    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    html3 = browser.html
    soup3 = bs(html3, "html.parser")

    weather_list=[]
    results_weather=soup3.find_all('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    for weather_tweet in results_weather:
        weather_list.append((weather_tweet))
    mars_weather = weather_list[0]
    tweet_mars=mars_weather.text.strip()

# facts

    url_t='http://space-facts.com/mars/'
    table_facts = pd.read_html(url_t)
    dataframe=table_facts[0]
    print(table_facts[0].to_html('mars_facts.html', header=False))

# hemishperes

    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)
    html4 = browser.html
    soup4 = bs(html4, "html.parser")

    hemi_list=[]
    results_hemisphere = soup4.find_all('div',class_="description")

    for hemi in results_hemisphere:
        hemi_list.append('https://astrogeology.usgs.gov' + str(hemi).split('href="')[1].split('"><h3>')[0])

    hemisphere_image_urls = []

    for sphere in hemi_list:
        browser = Browser('chrome', headless=False)
        sphere_url = sphere
        browser.visit(sphere_url)
        html5 = browser.html
        soup5 = bs(html5, 'html.parser')
        hemis = soup5.findAll("div", class_="content")
        hemisphere_image_urls.append({
                "title" : str(hemis).split('"title">')[1].split(' Enhanced<')[0],
                "img_url" : str(hemis).split('Filename</dt><dd><a href="')[1].split('">')[0]
            })

    mars = {"news_title":title, "news_text":facts, "weather_tweet":tweet_mars, 
    "facts":dataframe, "hemisphere_images":hemisphere_image_urls}

    return mars

scrape