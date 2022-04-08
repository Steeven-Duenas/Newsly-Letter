import requests


class topheadlines:
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
    API_KEY = "f9e5f0c7d52342c1a1aa5129684953c3"
    world_news = ""
    total_results = 0
    show_article_number = 0

    def __init__(self, language, q):
        language = language
        q = q

    def get_world_api_request(self, selected_country):
        url = "https://newsapi.org/v2/top-headlines?country={0}&apiKey={1}".format(selected_country, self.API_KEY)
        world_news_request = requests.get(url).json()
        self.world_news = world_news_request

    def set_total_results(self, world_news):
        total = world_news["totalResults"]
        self.total_results = total

    def get_articles_world(self, world_news):
        news = world_news
        articles = news["articles"]
        my_articles = []
        for article in articles:
            my_articles.append(article["title"])
        return my_articles

    def sef_article_number(self, article_number):
        self.show_article_number = article_number

    def show_article(self, get_articles_world):
        my_articles = get_articles_world()
        my_news = " "
        for i in range(self.show_article_number):
            my_news = my_news + str(i + 1) + ". " + my_articles[i] + "\n"
        return my_news
