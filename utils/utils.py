import os
import csv
import json
import collections

def json_storage(root_folder, storage_folder, newspaper_name):
    all_articles = []
    for year_folder in os.listdir(root_folder):
        year_path = os.path.join(root_folder, year_folder)
        for month_folder in os.listdir(year_path):
            month_path = os.path.join(year_path, month_folder)
            if os.path.isdir(month_path):
                for date_folder in os.listdir(month_path):
                    date_path = os.path.join(month_path, date_folder)
                    if os.path.isdir(date_path):
                        articles_file = os.path.join(date_path, "articles.json")
                        with open(articles_file, "r") as f:
                            data = json.load(f)
                            all_articles.extend(data["articles"])

    output_file = os.path.join(storage_folder, F"{newspaper_name}_all_articles.json")
    with open(output_file, "w") as f:
        dump_data = {
            'number': len(all_articles),
            'articles': all_articles
        }
        json.dump(dump_data, f, indent=4)

def convert_csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as file:
        csv_data = csv.DictReader(file)
        data = []
        for row in csv_data:
            data.append(row)
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

def convert_json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as file:
        json_data = json.load(file)
        data = json_data['articles']
    with open(csv_file, 'w') as file:
        csv_data = csv.DictWriter(file, data[0].keys())
        csv_data.writeheader()
        csv_data.writerows(data)