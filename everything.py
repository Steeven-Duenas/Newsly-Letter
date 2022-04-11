class everything:

    def __init__(self, newsJson):
        self.newsJson = newsJson

    def get_total_results(self):
        total = self.newsJson["totalResults"]
        return total

    def get_articles_everything(self):
        articles = self.newsJson["articles"]
        my_articles = []
        for article in articles:
            my_articles.append(article["title"])
        return my_articles

    def show_article_of_everything(self, headline_number):
        my_articles = self.get_articles_everything()
        my_news = ""
        display = 0
        if headline_number >= 20:
            display = 20
        elif headline_number < 20:
            display = headline_number
        for i in range(display):
            my_news = my_news + str(i + 1) + ". " + my_articles[i] + "\n"
        return my_news
