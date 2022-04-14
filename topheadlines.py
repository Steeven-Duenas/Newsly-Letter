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

    def get_link_of_articles(self):
        url_articles = self.newsJson["articles"]
        url_list = []
        final_list = []
        for article in url_articles:
            url_list.append(article["url"])
        if self.get_total_results() < 20:
            for i in range(self.get_total_results()):
                final_list.append(url_list[i])
        elif self.get_total_results() > 20:
            for i in range(20):
                final_list.append(url_list[i])
        return final_list

    def dictionary_of_title_and_description_and_links(self):
        summary = self.get_summary_of_articles()
        articles = self.get_articles_world()
        url = self.get_link_of_articles()
        data = [{'articles': art, 'summary': sum, 'url': url} for art, sum, url in
                zip(articles, summary, url)]
        return data
