class topheadlines:

    def __init__(self, newsJson):
        self.show_articles = 4
        self.newsJson = newsJson

    def get_show_articles(self):
        return self.show_articles

    def set_show_articles(self, number):
        self.show_articles = number

    def get_total_results(self):
        total = self.newsJson["totalResults"]
        return total

    def check_if_limit(self):
        if self.get_total_results() < 20:
            return self.get_total_results()
        elif self.get_total_results() > 20:
            return 20

    def get_articles_world(self):
        articles = self.newsJson["articles"]
        my_articles = []
        final_list = []
        for article in articles:
            my_articles.append(article["title"])
        for i in range(self.get_show_articles()):
            final_list.append(my_articles[i])

        return final_list

    def get_summary_of_articles(self):
        summary_articles = self.newsJson["articles"]
        summary_list = []
        final_list = []
        for article in summary_articles:
            summary_list.append(article["description"])
        for i in range(self.get_show_articles()):
            final_list.append(summary_list[i])

        return final_list

    def get_link_of_articles(self):
        url_articles = self.newsJson["articles"]
        url_list = []
        final_list = []
        for article in url_articles:
            url_list.append(article["url"])
        for i in range(self.get_show_articles()):
            final_list.append(url_list[i])
        return final_list

    def dictionary_of_title_and_description_and_links(self):
        summary = self.get_summary_of_articles()
        articles = self.get_articles_world()
        url = self.get_link_of_articles()
        data = [{'articles': art, 'summary': sun, 'url': url} for art, sun, url in
                zip(articles, summary, url)]
        return data
