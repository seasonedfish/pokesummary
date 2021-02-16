import csv
from importlib import resources


def parse_data():
    with resources.open_text("pokesummary.data", "pokemon_modified.csv") as f:
        data_iterator = csv.reader(f)
        data_dictionary = {
            row[2]: row[3:40]
            for row in data_iterator
        }
    return data_dictionary
