import requests


class topheadlines:

    def __init__(self, articleList):
        self.articlesList = articleList

    def set_country(self, country):
        self.selected_country = country

    def set_total_results(self, world_news):
        total = world_news["totalResults"]
        self.total_results = total

    def get_articles_world(self):
        news = self.get_world_api_request()
        articles = news["articles"]
        my_articles = []
        for article in articles:
            my_articles.append(article["title"])
        return my_articles

    def set_article_number(self, article_number):
        self.show_article_number = article_number

    def show_article(self):
        my_articles = self.get_articles_world()
        my_news = ""
        for i in range(1):
            my_news = my_news + str(i + 1) + ". " + my_articles[i] + "\n"
        return my_news

