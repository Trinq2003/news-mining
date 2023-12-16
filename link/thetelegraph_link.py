from bs4 import BeautifulSoup

from .dlink_page import PageDownloadLinkFetcher


class TheTelegraphLinkFetcher(PageDownloadLinkFetcher):
    def __init__(self, config):
        super(TheTelegraphLinkFetcher, self).__init__(config)

    def _next_api(self, base_url, current_page):
        api_url = base_url.format(page=current_page)
        return api_url

    def _html_to_links(self, html):
        soup = BeautifulSoup(html, 'lxml')

        links = []
        li_elements = soup.find_all("li", class_="cst-card")
        for link in li_elements:
            a = link.find("a")
            href = a["href"]
            links.append(href)


        return list(set(links))
