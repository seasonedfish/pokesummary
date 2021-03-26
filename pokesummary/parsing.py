import csv
from importlib import resources


def parse_data():
    with resources.open_text("pokesummary.data", "pokemon_modified.csv") as f:
        data_iterator = csv.DictReader(f)
        data_dictionary = {
            row["pokemon_name"]: row
            for row in data_iterator
        }
    return data_dictionary


def parse_type_defenses():
    with resources.open_text("pokesummary.data", "type_defenses.csv") as f:
        data_iterator = csv.DictReader(f)
        types_dictionary = {
            row["attacking_type"]: row
            for row in data_iterator
        }
        for key, value in types_dictionary.items():
            del types_dictionary[key]["attacking_type"]

    return types_dictionary
