import requests


class everything:
    API_KEY = "f9e5f0c7d52342c1a1aa5129684953c3"
    q = ""
    search_In = ""
    sources = ""
    domains = ""
    exclude_Domains = ""
    from_date = ""
    to_date = ""
    language = ""
    sortBy = ""
    pageSize = 0
    page = 1
    total_results = 0
    everything_news = ""
    show_article_number = 0

    def __init__(self, language, q):
        language = language
        q = q

    def get_everything_api_request(self):
        url = "https://newsapi.org/v2/everything?q={0}&apiKey={1}".format(self.q, self.API_KEY)
        everything_news = requests.get(url).json()
        self.everything_news = everything_news

    def set_total_results(self, everything_news):
        total = everything_news["totalResults"]
        self.total_results = total

    def get_articles_everything(self, everything_news):
        news = everything_news
        articles = news["articles"]
        my_articles = []
        for article in articles:
            my_articles.append(article["title"])
        return my_articles

    def sef_article_number(self, article_number):
        self.show_article_number = article_number

    def show_article(self):
        my_articles = self.get_articles_everything()
        my_news = " "
        for i in range(self.show_article_number):
            my_news = my_news + str(i + 1) + ". " + my_articles[i] + "\n"
        return my_news
