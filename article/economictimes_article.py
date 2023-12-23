import os

from bs4 import BeautifulSoup
from goose3 import Goose
from dateutil.relativedelta import relativedelta

from network.network import NetworkFetcher
from .darticle import ArticleFetcher
from link.economictimes_link import EconomicTimesLinkFetcher


class EconomicTimesArticleFetcher(ArticleFetcher):

    def __init__(self, config):
        super(EconomicTimesArticleFetcher, self).__init__(config)
        self.config = config
        self.download_link_fetcher = EconomicTimesLinkFetcher(config)

    def _extract_title(self, soup):
        if soup.title is not None:
            return soup.title.get_text()

    def _extract_published_date(self, soup):
        publish_element = soup.find('time', class_='jsdtTime')
        if publish_element is not None:
            result = publish_element.get_text()
            return result

    def _extract_authors(self, soup):
        return None

    def _extract_description(self, soup):
        description_element = soup.find('meta', property='og:description')
        if description_element is not None:
            return description_element['content']

    def _extract_section(self, soup):
        return None
    
    def _extract_tag(self, soup):
        return None

    def _extract_content(self, html):
        g = Goose({'enable_image_fetching': False})
        article = g.extract(raw_html=html)
        return article.cleaned_text

    def _html_to_infomation(self, html, link, date):
        soup = BeautifulSoup(html, 'html5lib')
        head = soup

        try:
            title = self._extract_title(head)
            published_date = self._extract_published_date(head)
            authors = self._extract_authors(head)
            description = self._extract_description(head)
            section = self._extract_section(head)
            tags = self._extract_tag(head)
            content = self._extract_content(html)
        except Exception as err:
            return None

        return {
            'title': title,
            'published_date': published_date,
            'authors': authors,
            'description': description,
            'section': section,
            'tags': tags,
            'content': content,
            'link': link
        }
