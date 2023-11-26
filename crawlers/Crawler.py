import requests
from bs4 import BeautifulSoup
import abc
import json
import os

class Crawler:
    def __init__(self, root_url) -> None:
        self.root = root_url
        self.all_links = {}
    @abc.abstractmethod
    def crawl_from_topic(self, topic_url):
        pass
    @abc.abstractmethod
    def crawl_all(self):
        """
        Crawl all the links of all tags, categories or topics
        """
        pass
    def dump_to_json(self, filename):
        """
        Dump the crawled links to a json file
        """
        # if not os.path.exists(filename):
        #     os.makedirs(filename)
            
        # TODO: prevent overwriting
        with open(filename, 'w') as f:
            json.dump(self.all_links, f)
    def start(self):
        pass