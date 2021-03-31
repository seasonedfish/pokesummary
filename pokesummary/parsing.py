import csv
from importlib import resources


def csv_to_2d_dict(package, csv_file, index, lambda_function=lambda x: x):
    with resources.open_text(package, csv_file) as f:
        data_iterator = csv.DictReader(f)
        data_dictionary = {
            row[index]: {
                k: lambda_function(v)
                for k, v in list(row.items())[1:]
            }
            for row in data_iterator
        }
    return data_dictionary


if __name__ == "__main__":
    data = csv_to_2d_dict("pokesummary.data", "type_defenses_modified.csv", "defending_type", lambda x: float(x))
    print(data)
    data2 = csv_to_2d_dict("pokesummary.data", "pokemon_modified.csv", "pokemon_name")
    print(data2)
