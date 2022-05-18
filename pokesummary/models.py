from dataclasses import dataclass
from collections import UserDict
import csv
from importlib import resources
from pokesummary import data

@dataclass
class Pokemon:
    name: str
    classification: str
    height: float
    weight: float

    primary_type: str
    secondary_type: str

    base_stats: dict[str, int]
    type_defenses: dict[str, float]


def read_dataset_to_dictionary():
    with resources.open_text(data, "pokemon_modified.csv") as f:
        csv_iterator = csv.DictReader(f)

        dataset_dict = {}
        for csv_row in csv_iterator:
            current_pokemon = Pokemon(
                name=csv_row["pokemon_name"],
                classification=csv_row["classification"],
                height=csv_row["pokemon_height"],
                weight=csv_row["pokemon_weight"],
                primary_type=csv_row["primary_type"],
                secondary_type=csv_row["secondary_type"],
                # TODO base_stats
                # TODO type_defenses
            )
            dataset_dict[current_pokemon.name] = current_pokemon

    return dataset_dict


class PokemonDict(UserDict):
    def __init__(self):
        pokemon_dictionary = read_dataset_to_dictionary()
        UserDict.__init__(self, pokemon_dictionary)


