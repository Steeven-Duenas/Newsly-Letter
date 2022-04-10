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


def request_country_news_api(country_select):
    api_key = "f9e5f0c7d52342c1a1aa5129684953c3"
    url = "https://newsapi.org/v2/top-headlines?country={0}&apiKey={1}".format(country_select, api_key)

    jsonFile = requests.get(url).json()

    return jsonFile


def request_topheadlines_news_api(topic_name):
    api_key = "f9e5f0c7d52342c1a1aa5129684953c3"
    url = "https://newsapi.org/v2/top-headlines?country=us&category={0}&apiKey={1}".format(topic_name,
                                                                                           api_key)
    jsonFile = requests.get(url).json()

    return jsonFile


options = st.sidebar.radio(
    "Select News",
    ('None', 'World News', 'Top Headlines', 'Search by Source'))

if options == "World News":
    country = st.selectbox(
        'Select the country which you want news', options=countries_of_the_world)

    if country != "Select a country":
        st.write("You have selected: " + country)
        country_code = countries_of_the_world[country]
        news = request_country_news_api(country_code)
        top_headlines_1 = topheadlines(news)
        total_number_of_articles = top_headlines_1.get_total_results()
        bool_choose = True
        headline_number = 1
        if total_number_of_articles >= 20:
            headline_number = 20
        else:
            headline_number = top_headlines_1.get_total_results()
        headline_number = st.sidebar.slider("How many articles?", 1, headline_number)
        headlines = topheadlines(news).show_article(headline_number)
        st.write(headlines)
    else:
        st.write("You have not selected a country")

elif options == "Top Headlines":
    choice = st.selectbox(
        'Please select the category of news: ',
        ('', 'Business', 'Entertainment', 'General', 'Health', 'Science', 'Sports', 'Technology'))
    st.write("You have selected: " + choice)
    news = request_topheadlines_news_api(choice)
    top_headlines_2 = topheadlines(news)
    total_number_of_articles = top_headlines_2.get_total_results()
    bool_choose = True
    headline_number = 1
    if total_number_of_articles >= 20:
        headline_number = 20
    else:
        headline_number = top_headlines_2.get_total_results()
    headline_number = st.sidebar.slider("How many articles?", 1, headline_number)
    headlines = topheadlines(news).show_article(headline_number)
    st.write(headlines)
elif options == "Search by Source":
    st.write("You have selected Search by Source")
else:
    st.warning("Please Choose a Category")
