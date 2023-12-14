import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Argument Parser')
    
    # Add your arguments here
    parser.add_argument('--config_path', help='Configuration file path', type=str)
    parser.add_argument('--json_dumping', help='Dump the data to a JSON', type=bool, default=True)
    parser.add_argument('--newspaper_names', help='The name(s) of newspaper', type=list, default=['nytimes'])
    parser.add_argument('--crawl_all', help='If True, crawl all the news paper in the list (read README.md for more information)', type=bool, default=False)
    # Parse the arguments
    args = parser.parse_args()
    
    return args
