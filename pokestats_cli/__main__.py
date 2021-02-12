import csv
import pprint
import importlib.resources

if __name__ == "__main__":
    from . import data

    with importlib.resources.open_text(data, "pokemon.csv") as file:
        data = tuple(csv.reader(file))
    pp = pprint.PrettyPrinter()
    pp.pprint(data)
