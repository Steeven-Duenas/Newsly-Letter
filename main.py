import time

import folium
import pandas as pd
import requests
import streamlit as st
from streamlit_folium import folium_static

from topheadlines import topheadlines

countries_of_the_world = {'': '',
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

api_key = "f9e5f0c7d52342c1a1aa5129684953c3"


def map_creator():
    df = pd.read_csv("world_country_and_usa_states_latitude_and_longitude_values.csv")
    # center on the station
    m = folium.Map(location=[13.13, 16.10], zoom_start=1.9)
    # add marker for the station
    city = df.loc[0]
    for _, country in df.iterrows():
        folium.Marker(
            location=[country['latitude'], country['longitude']], popup="Country Code: " + country['country_code'],
            tooltip=country['country']
        ).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)


def request_country_news_api(country_select):
    url = "https://newsapi.org/v2/top-headlines?country={0}&apiKey={1}".format(country_select, api_key)
    json_File = requests.get(url).json()
    return json_File


def request_topheadlines_news_api(topic_name):
    url = "https://newsapi.org/v2/top-headlines?country=us&category={0}&apiKey={1}".format(topic_name,
                                                                                           api_key)
    json_File = requests.get(url).json()

    return json_File


def request_sources_news_api():
    url = "https://newsapi.org/v2/top-headlines/sources?apiKey={0}".format(api_key)
    news_ID_List = []
    news_Name_List = ['']
    news_ID_List.append('none')
    # Send Request
    json_File = requests.get(url).json()
    for x in json_File["sources"]:
        news_Name_List.append(x["name"])
        news_ID_List.append(x["id"])

    dictionary_Of_Sources = dict(zip(news_Name_List, news_ID_List))

    return dictionary_Of_Sources


def request_headlines_source_news_api(source_id_api):
    url = "https://newsapi.org/v2/top-headlines?sources={0}&apiKey={1}".format(source_id_api, api_key)
    json_File = requests.get(url).json()

    return json_File


def request_keyword_news_api(key_word):
    url = "https://newsapi.org/v2/everything?q={0}&apiKey={1}".format(key_word, api_key)
    json_file = requests.get(url).json()

    return json_file


def get_source_news(x, articles):
    st.title(x)
    news = request_topheadlines_news_api(x)
    top_headlines_2 = topheadlines(news)
    top_headlines_2.set_show_articles(articles)
    top_headline_and_summary = top_headlines_2.dictionary_of_title_and_description_and_links()
    counter = 1
    data = top_headlines_2.dictionary_of_title_and_description_and_links()
    for dictionary in data:
        expander = st.expander(str(counter) + ". " + str(dictionary['articles']))
        expander.write('Description: ' + str(dictionary['summary']))
        expander.write('Link: ' + str(dictionary['url']))
        counter = counter + 1
    return top_headlines_2


def get_array_of_population():
    df = pd.read_csv("population_by_country_2020.csv")
    population = []
    for _, l in df.iterrows():
        population.append([l['Population (2020)']])
    return population


def get_array_of_name():
    df = pd.read_csv("population_by_country_2020.csv")
    name = []
    for _, p in df.iterrows():
        name.append([p['Country (or dependency)']])
    return name


st.set_page_config(
    page_title="Newsly Letter",
    layout="wide",
    initial_sidebar_state="expanded",
)
# Radio Button
options = st.sidebar.radio(
    "Select News",
    ('Welcome', 'Search by Keyword', 'World News', 'Top Headlines by Categories', 'Top Headlines by Source',
     'Country Information', "Global Statistics"))

if options == "World News":
    # Select box
    country = st.selectbox(
        'Select the country which you want news', options=countries_of_the_world)

    if country != '':
        st.title(country + " *News*!")
        country_code = countries_of_the_world[country]
        news = request_country_news_api(country_code)
        top_headlines_1 = topheadlines(news)
        with st.sidebar:
            articles = st.sidebar.slider('How old are you?', 0, top_headlines_1.check_if_limit(), 4)
        st.sidebar.write("You have selected: " + str(articles))
        top_headlines_1.set_show_articles(articles)
        number = top_headlines_1.get_show_articles()
        counter = 1
        data = top_headlines_1.dictionary_of_title_and_description_and_links()
        for dictionary in data:
            expander = st.expander(str(counter) + ". " + str(dictionary['articles']))
            expander.write('Description: ' + str(dictionary['summary']))
            expander.write('Link: ' + str(dictionary['url']))
            counter = counter + 1
    else:
        st.warning("You have not selected a country")
elif options == "Top Headlines by Source":
    source_files = request_sources_news_api()
    # Select box
    source_name = st.selectbox('Select a News Station', options=source_files)
    if source_name != '':
        source_id = source_files[source_name]
        st.title(source_name)
        source_headlines = request_headlines_source_news_api(source_id)
        source_object_1 = topheadlines(source_headlines)
        with st.sidebar:
            articles = st.sidebar.slider('How old are you?', 0, source_object_1.check_if_limit(), 4)
        st.sidebar.write("You have selected: " + str(articles))
        source_object_1.set_show_articles(articles)
        number = source_object_1.get_show_articles()
        data = source_object_1.dictionary_of_title_and_description_and_links()
        counter = 1

        for dictionary in data:
            expander = st.expander(str(counter) + ". " + str(dictionary['articles']))
            expander.write('Link: ' + str(dictionary['url']))
            counter = counter + 1
    else:
        st.warning("Please select a source")
elif options == "Search by Keyword":
    with st.form("my_form", clear_on_submit=True):
        # Text Input
        keyword = st.text_input('Search for news', '')
        # Submit Button
        submitted = st.form_submit_button("Submit")
        if keyword != '':
            st.title(keyword.capitalize())
            jsonFile = request_keyword_news_api(keyword)
            key_word_search_1 = topheadlines(jsonFile)
            with st.sidebar:
                articles = st.sidebar.slider('How old are you?', 1, key_word_search_1.check_if_limit(), 4)
            st.sidebar.write("You have selected: " + str(articles) + " articles")
            key_word_search_1.set_show_articles(articles)
            number = key_word_search_1.get_show_articles()
            counter = 1
            data = key_word_search_1.dictionary_of_title_and_description_and_links()
            for dictionary in data:
                expander = st.expander(str(counter) + ". " + str(dictionary['articles']))
                expander.write('Description: ' + str(dictionary['summary']))
                expander.write('Link: ' + str(dictionary['url']))
                counter = counter + 1
        else:
            st.warning("Please do not leave the box blank")
elif options == "Country Information":
    dataframe = pd.read_csv("world_country_and_usa_states_latitude_and_longitude_values.csv")
    with st.form("Map_and_table"):
        st.write("Map & Table")
        map_box = st.checkbox("Show countries with available news", )
        coordinates_box = st.checkbox("Show Country Coordinates")
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            # Displays Table
            if coordinates_box:
                my_bar = st.progress(0)
                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1)
                if percent_complete == 99:
                    st.success("The table has loaded successfully")
                    st.write("Table of countries with supported news stations")
                    st.table(dataframe)
            # Displays Map
            if map_box:
                my_bar = st.progress(0)
                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1)
                if percent_complete == 99:
                    st.success("The map has loaded successfully")
                    st.write("Map Countries with supported news stations")
                    map_creator()

        # Interactive Table
elif options == "Top Headlines by Categories":
    st.write("Top Headlines by Categories")
    options = st.multiselect(
        'What are your favorite colors',
        ['Business', 'Entertainment', 'General', 'Health', 'Science', 'Sports', 'Technology'],
        ['Business'])
    with st.sidebar:
        articles = st.sidebar.slider('How old are you?', 0, 20, 4)
    st.sidebar.write("You have selected: " + str(articles) + " Articles")
    for x in options:
        if x == 'Business':
            get_source_news(x, articles)
        if x == 'Entertainment':
            get_source_news(x, articles)
        if x == 'General':
            get_source_news(x, articles)
        if x == 'Health':
            get_source_news(x, articles)
        if x == 'Science':
            get_source_news(x, articles)
        if x == 'Sports':
            get_source_news(x, articles)
        if x == 'Technology':
            get_source_news(x, articles)
elif options == "Welcome":
    st.title("Welcome to Newsly")
    st.subheader("This is an app that uses NEWSAPI to deliver you news")
    st.write("You will find different ways to search and look up news in the sidebar")
    st.write("Give us feedback by email: sduen011@fiu.edu")
elif options == "Global Statistics":
    bar_chart = st.checkbox('Press to show bar chart')
    line_chart = st.checkbox('Press to show area chart')
    population_data_frame = pd.read_csv("population_by_country_2020.csv")
    thing_one = get_array_of_population()
    thing_two = get_array_of_name()
    data = [{'name': nam, 'population': pop} for nam, pop, in zip(thing_two, thing_one)]
    chart_data = pd.DataFrame(
        [(data[0]["population"][0], 0), (data[1]["population"][0], 1), (data[2]["population"][0], 2),
         (data[3]["population"][0], 3)],
        columns=["World", ""])
    if bar_chart:
        # Bar Chart
        st.bar_chart(chart_data)
    if line_chart:
        # Line Chart
        st.line_chart(chart_data)
else:
    st.warning("Please Choose a Category")
