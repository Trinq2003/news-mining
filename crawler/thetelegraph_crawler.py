import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from settings.dataset_conf_page import PageDatasetConfiguration
from article.thetelegraph_article import TheTelegraphArticleFetcher


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('please input configuration path')
        exit()
    config = PageDatasetConfiguration()
    config.load(sys.argv[1])

    bbc_article_fetcher = TheTelegraphArticleFetcher(config)
    bbc_article_fetcher.fetch()
        
