import sys
import os.path
import json
import time
from datetime import timedelta

from network.network_page import PageNetworkFetcher


class PageArticleFetcher:

    RETRY = 5

    def __init__(self, config):
        self.config = config
        self.download_link_fetcher = None
        self.html_fetcher = PageNetworkFetcher()
        self.path = config.path

        self.total_page = 0

        self._mkdir(self.path,
                    config.start_page,
                    config.end_page,
                    config.step)

    def _mkdir(self, path, start_page, end_page, step):
        if os.path.isdir(path):
            # current_date = start_date
            # while current_date < end_date:
            #     current_date += step
            #     self.total_page += 1
            # return
            pass
        else:
            os.makedirs(path)
        current_page = start_page
        existed_pages = dict()
        while current_page < end_page:
            current_page_path = os.path.join(path, str(current_page))

            if current_page not in existed_pages.keys():
                existed_pages[current_page] = dict()
                if not os.path.isdir(current_page_path):
                    os.mkdir(current_page_path)
            current_page += step

            self.total_page += 1

    def _html_to_infomation(self, html, link, page):
        return {}

    def _extract_information(self, link, page):
        html = self.html_fetcher.fetch(link)
        if html is None:
            for _ in range(0, self.RETRY):
                html = self.html_fetcher.fetch(link)
                if html is not None:
                    break
        if html is None:
            print('article ', link, 'failed')
            return None
        return self._html_to_infomation(html, link, page)

    def _get_storage_path(self, path, page):
        return os.path.join(path, str(page))

    def _lazy_storage(self, storage_path, links, page):
        total_links = len(links)
        current_link = 1

        titles_path = os.path.join(storage_path, 'titles.txt')
        with open(titles_path, mode='w', encoding='utf-8') as titles_file:
            articles = list()
            titles = list()
            for link in links:
                print('>>> {c} in {t} articles\r'.format(c=current_link, t=total_links), end='')
                current_link += 1

                article = self._extract_information(link, page)
                if article is not None:
                    titles.append(article['title'] + '\n')
                    articles.append(article)

            articles_path = os.path.join(storage_path, 'articles.json')
            with open(articles_path, mode='w', encoding='utf-8') as articles_file:
                json.dump({
                    'expected_number': len(links),
                    'number': len(articles),
                    'articles': articles
                }, articles_file, indent=4)
            titles_file.writelines(titles)

    def _non_lazy_storage(self, storage_path, links, page):
        total_links = len(links)
        current_link = 1

        titles_path = os.path.join(storage_path, 'titles.txt')
        with open(titles_path, mode='w', encoding='utf-8') as titles_file:
            for article_index, link in enumerate(links):
                print('{c} in {t} articles\r'.format(c=current_link, t=total_links), end='')
                current_link += 1

                article = self._extract_information(link, page)
                if article is not None:
                    titles_file.write(article['title'] + '\n')

                    article_path = os.path.join(storage_path, str(article_index))
                    with open(article_path, mode='w', encoding='utf-8') as article_file:
                        json.dump(article, article_file, indent=4)

    def fetch(self, lazy_storage=True):
        current_page = 1
        while True:
            api_url, page = self.download_link_fetcher.next()
            if api_url is None:
                break
            print(page,
                  '{c} in {t} pages                  '.format(c=current_page, t=self.total_page))

            storage_path = self._get_storage_path(self.path, page)
            links = self.download_link_fetcher.fetch(api_url)
            if lazy_storage:
                self._lazy_storage(storage_path, links, page)
            else:
                self._non_lazy_storage(storage_path, links, page)

            time.sleep(self.config.sleep)

            print(page,
                  'page {c} finished                 '.format(c=current_page))
            current_page += 1
