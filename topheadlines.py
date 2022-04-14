class topheadlines:

    def __init__(self, newsJson):
        self.newsJson = newsJson

    def get_total_results(self):
        total = self.newsJson["totalResults"]
        return total

    def get_articles_world(self):
        articles = self.newsJson["articles"]
        my_articles = []
        final_list = []
        for article in articles:
            my_articles.append(article["title"])

        if self.get_total_results() < 20:
            for i in range(self.get_total_results()):
                final_list.append(my_articles[i])
        elif self.get_total_results() > 20:
            for i in range(20):
                final_list.append(my_articles[i])
        return final_list

    def get_summary_of_articles(self):
        summary_articles = self.newsJson["articles"]
        summary_list = []
        final_list = []
        for article in summary_articles:
            summary_list.append(article["description"])

        if self.get_total_results() < 20:
            for i in range(self.get_total_results()):
                final_list.append(summary_list[i])
        elif self.get_total_results() > 20:
            for i in range(20):
                final_list.append(summary_list[i])
        return final_list

    def show_article(self, headline_number):
        my_articles = self.get_articles_world()
        my_news = ""
        display = headline_number
        for i in range(display):
            my_news = my_news + str(i + 1) + ". " + my_articles[i] + "\n"
        return my_news

    def dictionary_of_title_and_description(self):
        summary = self.get_summary_of_articles()
        articles = self.get_articles_world()
        dictionary = dict(zip(articles, summary))
        return dictionary
