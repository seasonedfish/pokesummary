import importlib.resources
import csv


def parse_data():
    with importlib.resources.open_text("data", "pokemon_modified.csv") as file:
        data_iterator = csv.reader(file)
        data = {row[2]: row[3:40]
                for row in data_iterator}
    return data
