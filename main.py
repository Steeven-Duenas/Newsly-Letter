import requests
import pandas as pd
import streamlit as st
import time

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
    from streamlit_folium import folium_static
    import folium
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
    news_Name_List = ['Select a Source']
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


# Radio Button
options = st.sidebar.radio(
    "Select News",
    ('Search by Keyword', 'World News', 'Top Headlines by Categories', 'Top Headlines by Source', 'Country Information',
     'Testing'))

if options == "World News":
    # Select box
    country = st.selectbox(
        'Select the country which you want news', options=countries_of_the_world)

    if country != '':
        st.title(country + " *News*!")
        country_code = countries_of_the_world[country]
        news = request_country_news_api(country_code)
        top_headlines_1 = topheadlines(news)
        counter = 1
        data = top_headlines_1.dictionary_of_title_and_description_and_links()
        for dictionary in data:
            expander = st.expander(str(counter) + ". " + str(dictionary['articles']))
            expander.write('Description: ' + str(dictionary['summary']))
            expander.write('Link: ' + str(dictionary['url']))
            counter = counter + 1
    else:
        st.warning("You have not selected a country")
elif options == "Top Headlines by Categories":
    choice = st.selectbox(
        'Please select the category of news: ',
        ('', 'Business', 'Entertainment', 'General', 'Health', 'Science', 'Sports', 'Technology'))
    if choice != '':
        st.title(choice)
        news = request_topheadlines_news_api(choice)
        top_headlines_2 = topheadlines(news)
        top_headline_and_summary = top_headlines_2.dictionary_of_title_and_description_and_links()
        counter = 1
        data = top_headlines_2.dictionary_of_title_and_description_and_links()
        for dictionary in data:
            expander = st.expander(str(counter) + ". " + str(dictionary['articles']))
            expander.write('Description: ' + str(dictionary['summary']))
            expander.write('Link: ' + str(dictionary['url']))
            counter = counter + 1
    else:
        st.warning("Please select a subject")
elif options == "Top Headlines by Source":
    source_files = request_sources_news_api()
    # Select box
    source_name = st.selectbox('Select the Source of News', options=source_files)
    if source_name != 'Select a Source':
        source_id = source_files[source_name]
        st.title(source_name)
        source_headlines = request_headlines_source_news_api(source_id)
        source_object_1 = topheadlines(source_headlines)
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
            counter = 1
            data = key_word_search_1.dictionary_of_title_and_description_and_links()
            for dictionary in data:
                expander = st.expander(str(counter) + ". " + str(dictionary['articles']))
                expander.write('Description: ' + str(dictionary['summary']))
                expander.write('Link: ' + str(dictionary['url']))
                counter = counter + 1
        else:
            st.warning("Please do not leave the box blank")
elif options == "Testing":
    st.write("Testing")
elif options == "Country Information":
    dataframe = pd.read_csv("world_country_and_usa_states_latitude_and_longitude_values.csv")
    with st.form("Map_and_table"):
        st.write("Map & Table")
        map_box = st.checkbox("Show World Map",)
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
else:
    st.warning("Please Choose a Category")
