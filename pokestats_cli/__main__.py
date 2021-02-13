import csv
import pprint
import importlib.resources

if __name__ == "__main__":
    from . import data

    with importlib.resources.open_text(data, "pokemon_modified.csv") as file:
        data_iterator = csv.reader(file)
        data = {row[2]: row[3:40]
                for row in data_iterator}
    pp = pprint.PrettyPrinter()
    pp.pprint(data["Bulbasaur"])
