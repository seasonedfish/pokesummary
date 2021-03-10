import csv
from importlib import resources


def parse_data():
    with resources.open_text("pokesummary.data", "pokemon_modified.csv") as f:
        data_iterator = csv.DictReader(f)
        data_dictionary = {
            row["Pokemon Name"]: row
            for row in data_iterator
        }
    return data_dictionary
