import requests
import streamlit as st

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


options = st.sidebar.radio(
    "Select News",
    ('Search by Keyword', 'World News', 'Top Headlines', 'Search by Source', 'Cryptocurrency'))

if options == "World News":
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
elif options == "Top Headlines":
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
elif options == "Search by Source":
    source_files = request_sources_news_api()
    source_name = st.selectbox('Select the Source of News', options=source_files)
    if source_name != 'Select a Source':
        source_id = source_files[source_name]
        st.title(source_name)
        source_headlines = request_headlines_source_news_api(source_id)
        source_object_1 = topheadlines(source_headlines)
        counter = 1
        data = source_object_1.dictionary_of_title_and_description_and_links()
        for dictionary in data:
            expander = st.expander(str(counter) + ". " + str(dictionary['articles']))
            expander.write('Link: ' + str(dictionary['url']))
            counter = counter + 1
    else:
        st.warning("Please select a source")
elif options == "Search by Keyword":
    keyword = st.text_input('Enter keyword', 'bitcoin')
    if st.button('Search'):
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
        st.warning("Please press the search button to search")
elif options == "Cryptocurrency":
    st.write("Cryptocurrency")

else:
    st.warning("Please Choose a Category")
