import requests
from bs4 import BeautifulSoup
from Crawler import Crawler
from config import *

class Telegraph(Crawler):
    def __init__(self, url) -> None:
        super().__init__(url)
    def crawl_from_topic(self, url):
        """
        Get a list of links from the Telegraph website
        """
        lst = []
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        grid = soup.find("ul", class_ = "article-list__list grid")
        link = grid.find_all(attrs={"data-track-wrapper": "article-list "})
        for element in link:
            a = element.find("a")
            lst.append("https://www.telegraph.co.uk" + a["href"])
        return lst
    def crawl_all(self):
        """
        Crawl all the links of all tags, categories or topics
        """
        self.all_links['business'] = self.crawl_business()
        self.all_links['technology'] = self.crawl_technology()
        self.all_links['market'] = self.crawl_market()
        self.all_links['company'] = self.crawl_company()
        self.all_links['worlds_news'] = self.crawl_worlds_news()
        self.all_links['politic'] = self.crawl_politic()
        self.all_links['health'] = self.crawl_health()
        self.all_links['science'] = self.crawl_science()
        self.all_links['education'] = self.crawl_education()
        self.all_links['environment'] = self.crawl_environment()
        self.all_links['global_health'] = self.crawl_global_health()
        self.all_links['sport'] = self.crawl_sport()
        self.all_links['travel'] = self.crawl_travel()
        self.all_links['culture'] = self.crawl_culture()
        self.all_links['style'] = self.crawl_style()
        return self.all_links
    def start(self):
        self.crawl_all()
        self.dump_to_json('telegraph.json')
        
    # TOPIC CRAWLERS
    def crawl_business(self):
        for i in range(1,MAX_NUM_OF_PAGES):
            print(i)
            url = f"https://www.telegraph.co.uk/business/economy/page-{i}/"
            bussiness_lst = self.crawl_from_topic(url)
        return {'len': len(bussiness_lst), 'list': bussiness_lst}
    
    def crawl_technology(self):
        for i in range(1,MAX_NUM_OF_PAGES):
            print(i)
            url = f"https://www.telegraph.co.uk/technology/page-{i}/"
            technology_lst = self.crawl_from_topic(url)
        return {'len': len(technology_lst), 'list': technology_lst}
    def crawl_market(self):
        for i in range(1,MAX_NUM_OF_PAGES):
            print(i)
            url = f"https://www.telegraph.co.uk/business/markets/page-{i}/"
            market_lst = self.crawl_from_topic(url)
        return {'len': len(market_lst), 'list': market_lst}
    def crawl_company(self):
        for i in range(1,MAX_NUM_OF_PAGES):
            print(i)
            url = f"https://www.telegraph.co.uk/business/companies/page-{i}/"
            company_lst = self.crawl_from_topic(url)
        return {'len': len(company_lst), 'list': company_lst}
    def crawl_worlds_news(self):
        for i in range(1,MAX_NUM_OF_PAGES):
            print(i)
            url = f"https://www.telegraph.co.uk/world-news/page-{i}/"
            worlds_news_lst = self.crawl_from_topic(url)
        return {'len': len(worlds_news_lst), 'list': worlds_news_lst}
    def crawl_politic(self):
        for i in range(1,MAX_NUM_OF_PAGES):
            print(i)
            url = f"https://www.telegraph.co.uk/politics/page-{i}/"
            politic_lst = self.crawl_from_topic(url)
        return {'len': len(politic_lst), 'list': politic_lst}
    def crawl_health(self):
        for i in range(1,MAX_NUM_OF_PAGES):
            print(i)
            url = f"https://www.telegraph.co.uk/health/page-{i}/"
            health_lst = self.crawl_from_topic(url)
        return {'len': len(health_lst), 'list': health_lst}
    def crawl_science(self):
        for i in range(1,MAX_NUM_OF_PAGES):
            print(i)
            url = f"https://www.telegraph.co.uk/science/page-{i}/"
            science_lst = self.crawl_from_topic(url)
        return {'len': len(science_lst), 'list': science_lst}
    def crawl_education(self):
        for i in range(1,MAX_NUM_OF_PAGES):
            print(i)
            url = f"https://www.telegraph.co.uk/education/page-{i}/"
            education_lst = self.crawl_from_topic(url)
        return {'len': len(education_lst), 'list': education_lst}
    def crawl_environment(self):
        for i in range(1,MAX_NUM_OF_PAGES):
            print(i)
            url = f"https://www.telegraph.co.uk/environment/page-{i}/"
            environment_lst = self.crawl_from_topic(url)
        return {'len': len(environment_lst), 'list': environment_lst}
    def crawl_global_health(self):
        for i in range(1,MAX_NUM_OF_PAGES):
            print(i)
            url = f"https://www.telegraph.co.uk/global-health/page-{i}/"
            global_health_security_lst = self.crawl_from_topic(url)
        return {'len': len(global_health_security_lst), 'list': global_health_security_lst}
    def crawl_sport(self):
        for i in range(1,MAX_NUM_OF_PAGES):
            print(i)
            url = f"https://www.telegraph.co.uk/football/page-{i}/"
            sport_lst = self.crawl_from_topic(url)
        return {'len': len(sport_lst), 'list': sport_lst}
    def crawl_travel(self):
        for i in range(1,MAX_NUM_OF_PAGES):
            print(i)
            url = f"https://www.telegraph.co.uk/travel/page-{i}/"
            travel_lst = self.crawl_from_topic(url)
        return {'len': len(travel_lst), 'list': travel_lst}
    def crawl_culture(self):
        for i in range(1,MAX_NUM_OF_PAGES):
            print(i)
            url = f"https://www.telegraph.co.uk/culture/page-{i}/"
            culture_lst = self.crawl_from_topic(url)
        return {'len': len(culture_lst), 'list': culture_lst}
    def crawl_style(self):
        for i in range(1,MAX_NUM_OF_PAGES):
            print(i)
            url = f"https://www.telegraph.co.uk/style/page-{i}/"
            style_lst = self.crawl_from_topic(url)
        return {'len': len(style_lst), 'list': style_lst}

if __name__ == "__main__":
    crawler = Telegraph("https://www.telegraph.co.uk/")
    crawler.start()