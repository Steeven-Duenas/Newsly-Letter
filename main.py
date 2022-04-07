import streamlit as st
import pandas as pd
import requests

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

def get_Country_News(country_select, country_name):
    api_key = "f9e5f0c7d52342c1a1aa5129684953c3"
    url = "https://newsapi.org/v2/top-headlines?country={0}&category=business&apiKey={1}".format(country_select,
                                                                                                 api_key)
    news = requests.get(url).json()

    articles = news["articles"]
    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    results = news["totalResults"]
    st.subheader("There are " + str(results) + " news articles in *"
                 + country_name + "* , how many would you like to see?")

    if results < 10:
        display = results
    else:
        display = 10

    for i in range(display):
        my_news = my_news + str(i+1) + ". " + my_articles[i] + "\n"
    st.write(my_news)


def get_Country(country_of_the_world):
    country_selected = st.selectbox("Select a country", options=countries_of_the_world)
    if country_selected:
        return country_selected


def get_country_code(country_selected):
    country_code = 'blank'
    if 'blank':
        st.write("You have selected: " + country_selected)
        country_code = countries_of_the_world[country_selected]
        return country_code


country = get_Country(countries_of_the_world)

if country != "Select a country":
    countrycode = get_country_code(country)
    st.title(country + " *News!*")
    get_Country_News(countrycode, country)


