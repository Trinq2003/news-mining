from utils import options
from utils.utils import *
import crawler
import configparser
import subprocess

general_config = configparser.RawConfigParser()
general_config.read('./settings/general_config.cfg')
LIST_OF_NEWSPAPERS = general_config.get('PARAMETERS','list_of_newspapers')[1:-1].split(',')
STORAGE_PATH = general_config.get('STORAGE','path')

args = options.parse_arguments()
config_path = args.config_path
json_dumping = args.json_dumping
newspaper_names = args.newspaper_names
crawl_all = args.crawl_all

if crawl_all:
    newspapers_to_be_downloaded = LIST_OF_NEWSPAPERS
else:
    newspapers_to_be_downloaded = newspaper_names

for newspaper in newspapers_to_be_downloaded:
    with open(f'./scripts/crawl_news/crawl_{newspaper}.sh', 'rb') as file:
        script = file.read()
    rc = subprocess.call(script, shell=True)
    if json_dumping:
        json_storage(os.path.join(STORAGE_PATH,newspaper), os.path.join(STORAGE_PATH, './json/'), newspaper)
