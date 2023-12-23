from bs4 import BeautifulSoup

from .dlink import DownloadLinkFetcher
from datetime import datetime

STARTTIME_2008 = 39448

class EconomicTimesLinkFetcher(DownloadLinkFetcher):
    def __init__(self, config):
        super(EconomicTimesLinkFetcher, self).__init__(config)


    def _next_api(self, base_url, current_date):
        year = current_date.year
        month = current_date.month
        # day = current_date.day
        diff_date = current_date - datetime(2008, 1, 1)
        start_time = diff_date.days + STARTTIME_2008

        api_url = base_url.format(year=year, month=month, starttime = start_time)
        return api_url

    def _html_to_links(self, html):
        soup = BeautifulSoup(html, 'lxml')

        links = []
        ul_elements = soup.find_all("ul", class_="content")
        for link in ul_elements:
            a = link.find("a")
            href = a["href"]
            links.append(href)
        return list(set(links))
