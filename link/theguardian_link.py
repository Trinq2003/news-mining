from bs4 import BeautifulSoup

from .dlink import DownloadLinkFetcher


class TheGuardianLinkFetcher(DownloadLinkFetcher):
    def __init__(self, config):
        super(TheGuardianLinkFetcher, self).__init__(config)
        self.MONTH_ARRAY = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov','dec']


    def _next_api(self, base_url, current_date):
        year = current_date.year
        month = self.MONTH_ARRAY[current_date.month-1]
        day = current_date.day
        api_url = base_url.format(year=year, month=month, day=day)
        return api_url

    def _html_to_links(self, html):
        soup = BeautifulSoup(html, 'lxml')

        links = []
        li_elements = soup.find_all("li", class_="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link")
        for link in li_elements:
            a = link.find("a")
            href = a["href"]
            if '/video/' not in href and '/live/' not in href:
                links.append(href)


        return list(set(links))
