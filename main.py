import streamlit as st
import pandas as pd
import requests

from topheadlines import topheadlines

countries_of_the_world = {'Select a country': 'none',
                          'Argentina': 'ar',
                          'Australia': 'au',
                          'Austria': 'at',
                          'Belgium': 'be',
                          'Brazil': 'br',
                          'Bulgaria': 'bg',
                          'Canada': 'ca',
                          'China': 'cn',
                          'Colombia': 'co',
                          'Cuba': 'cu',
                          'Czech Republic': 'cz',
                          'Egypt': 'eg',
                          'France': 'fr',
                          'Germany': 'de',
                          'Greece': 'gr',
                          'Hong Kong': 'hk',
                          'Hungary': 'hu',
                          'India': 'in',
                          'Indonesia': 'id',
                          'Ireland': 'ie',
                          'Israel': 'il',
                          'Italy': 'it',
                          'Japan': 'jp',
                          'Korea, Republic of': 'kr',
                          'Latvia': 'lv',
                          'Lithuania': 'lt',
                          'Malaysia': 'my',
                          'Mexico': 'mx',
                          'Morocco': 'ma',
                          'Netherlands': 'nl',
                          'New Zealand': 'nz',
                          'Nigeria': 'ng',
                          'Norway': 'no',
                          'Philippines': 'ph',
                          'Poland': 'pl',
                          'Portugal': 'pt',
                          'Romania': 'ro',
                          'Russian Federation': 'ru',
                          'Saudi Arabia': 'sa',
                          'Serbia': 'rs',
                          'Singapore': 'sg',
                          'Slovakia': 'sk',
                          'Slovenia': 'si',
                          'South Africa': 'za',
                          'Sweden': 'se',
                          'Switzerland': 'ch',
                          'Taiwan, Province of China': 'tw',
                          'Thailand': 'th',
                          'Turkey': 'tr',
                          'Ukraine': 'ua',
                          'United Arab Emirates': 'ae',
                          'United Kingdom': 'gb',
                          'United States': 'us',
                          'Venezuela, Bolivarian Republic of': 've'}


# API KEY =  f9e5f0c7d52342c1a1aa5129684953c3

def request_country_news_api(country_select):
    api_key = "f9e5f0c7d52342c1a1aa5129684953c3"
    url = "https://newsapi.org/v2/top-headlines?country={0}&category=business&apiKey={1}".format(country_select,
                                                                                                 api_key)
    news = requests.get(url).json()

    articles = news["articles"]
    my_articles = []

    for article in articles:
        my_articles.append(article["title"])

    return my_articles


country = st.selectbox(
    'Select the country which you want news', options=countries_of_the_world)

country_code = countries_of_the_world[country]

articles = request_country_news_api(country_code)

top_headlines_1 = topheadlines(articles)




