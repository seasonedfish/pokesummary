"""
This module contains the model part
of the model-view-controller organization of Pokésummary.
The classes here are used to store information about Pokémon.
"""

import csv
from collections import UserDict
from dataclasses import dataclass
from enum import Enum
from importlib import resources
from typing import Optional

from pokesummary import data


class PokemonType(Enum):
    NORMAL = "Normal"
    FIRE = "Fire"
    WATER = "Water"
    ELECTRIC = "Electric"
    GRASS = "Grass"
    ICE = "Ice"
    FIGHTING = "Fighting"
    POISON = "Poison"
    GROUND = "Ground"
    FLYING = "Flying"
    PSYCHIC = "Psychic"
    BUG = "Bug"
    ROCK = "Rock"
    GHOST = "Ghost"
    DRAGON = "Dragon"
    DARK = "Dark"
    STEEL = "Steel"
    FAIRY = "Fairy"

    @staticmethod
    def optional_pokemon_type(s: str):
        if s == "":
            return None
        return PokemonType(s)


@dataclass(frozen=True)
class PokemonBaseStats:
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int


@dataclass(frozen=True)
class Pokemon:
    name: str
    classification: str
    height: float
    weight: float

    primary_type: PokemonType
    secondary_type: Optional[PokemonType]

    base_stats: PokemonBaseStats


class PokemonDict(UserDict):
    def __init__(self):
        pokemon_dict = self._read_dataset_to_dict()
        UserDict.__init__(self, pokemon_dict)

    @staticmethod
    def _read_dataset_to_dict():
        with resources.open_text(data, "pokemon_modified.csv") as f:
            csv_iterator = csv.DictReader(f)

            dataset_dict = {
                csv_row["pokemon_name"]: Pokemon(
                    name=csv_row["pokemon_name"],
                    classification=csv_row["classification"],
                    height=float(csv_row["pokemon_height"]),
                    weight=float(csv_row["pokemon_weight"]),
                    primary_type=PokemonType(csv_row["primary_type"]),
                    secondary_type=PokemonType.optional_pokemon_type(csv_row["secondary_type"]),
                    base_stats=PokemonBaseStats(
                        hp=int(csv_row["health_stat"]),
                        attack=int(csv_row["attack_stat"]),
                        defense=int(csv_row["defense_stat"]),
                        special_attack=int(csv_row["special_attack_stat"]),
                        special_defense=int(csv_row["special_defense_stat"]),
                        speed=int(csv_row["speed_stat"]),
                    )
                )
                for csv_row in csv_iterator
            }

        return dataset_dict


def main():
    pokemon_dict = PokemonDict()
    print("It worked!!")


if __name__ == "__main__":
    main()
