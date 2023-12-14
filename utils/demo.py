import os
import json

def json_storage(root_folder, storage_folder):
    all_articles = []
    for month_folder in os.listdir(root_folder):
        month_path = os.path.join(root_folder, month_folder)
        if os.path.isdir(month_path):
            for date_folder in os.listdir(month_path):
                date_path = os.path.join(month_path, date_folder)
                if os.path.isdir(date_path):
                    articles_file = os.path.join(date_path, "articles.json")
                    with open(articles_file, "r") as f:
                        data = json.load(f)
                        all_articles.extend(data["articles"])

    output_file = os.path.join(storage_folder, "all_articles.json")
    with open(output_file, "w") as f:
        dump_data = {
            'number': len(all_articles),
            'articles': all_articles
        }
        json.dump(dump_data, f, indent=4)

