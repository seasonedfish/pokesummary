import csv
from collections import UserDict
from dataclasses import dataclass
from importlib import resources

from pokesummary import data


@dataclass(frozen=True)
class Pokemon:
    name: str
    classification: str
    height: float
    weight: float

    primary_type: str
    secondary_type: str

    @dataclass(frozen=True)
    class BaseStats:
        attack: int
        defense: int
        special_attack: int
        special_defense: int
        speed: int
        total: int

    base_stats: BaseStats
    type_defenses: dict[str, float]


class PokemonDict(UserDict):
    def __init__(self):
        pokemon_dictionary = self.read_dataset_to_dictionary()
        UserDict.__init__(self, pokemon_dictionary)

    @staticmethod
    def read_dataset_to_dictionary():
        with resources.open_text(data, "pokemon_modified.csv") as f:
            csv_iterator = csv.DictReader(f)

            dataset_dict = {}
            for csv_row in csv_iterator:
                current_pokemon = Pokemon(
                    name=csv_row["pokemon_name"],
                    classification=csv_row["classification"],
                    height=float(csv_row["pokemon_height"]),
                    weight=float(csv_row["pokemon_weight"]),
                    primary_type=csv_row["primary_type"],
                    secondary_type=csv_row["secondary_type"],
                    base_stats=None,
                    type_defenses=None
                )
                dataset_dict[current_pokemon.name] = current_pokemon

        return dataset_dict


if __name__ == "__main__":
    pokemon_dict = PokemonDict()
    print("It worked!!")
