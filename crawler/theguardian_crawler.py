import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from settings.dataset_conf import DatasetConfiguration
from article.theguardian_article import TheGuardianArticleFetcher


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('please input configuration path')
        exit()
    config = DatasetConfiguration()
    config.load(sys.argv[1])

    bbc_article_fetcher = TheGuardianArticleFetcher(config)
    bbc_article_fetcher.fetch()
        
