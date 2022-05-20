"""
This module contains the view part
of the model-view-controller organization of Pokésummary.
The classes and functions here are used to display model.Pokemon objects.
"""

import csv
from collections import UserDict
from importlib import resources
from typing import cast, Dict, List

from pokesummary import data
from pokesummary.model import Pokemon, PokemonType


class Color:
    GREEN = "\033[49;32m"
    RED = "\033[49;31m"

    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


TypeDefenses = Dict[PokemonType, float]


class TypeDefensesDict(UserDict):
    def __init__(self):
        type_defenses_dict = self._read_dataset_to_dict()
        UserDict.__init__(self, type_defenses_dict)

    @staticmethod
    def _read_dataset_to_dict() -> Dict[PokemonType, TypeDefenses]:
        # Parses the grid of type defenses.
        # The csv file is modified from the
        # visual chart on Pokémon Database.
        # https://pokemondb.net/type
        with resources.open_text(data, "type_defenses_modified.csv") as f:
            # The QUOTE_NONNUMERIC part allows us to read numbers directly as floats.
            data_iterator = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            # Gets the column names as a list of PokemonType members.
            attacking_types = list(
                map(PokemonType, data_iterator.__next__()[1:])
            )

            all_type_defenses: Dict[PokemonType, TypeDefenses] = {
                PokemonType(row[0]): dict(
                    zip(attacking_types, cast(List[float], row[1:]))
                )
                for row in data_iterator
            }
        return all_type_defenses


ALL_TYPE_DEFENSES = TypeDefensesDict().data

MULTIPLIER_STRINGS = {
    0.00: f"{Color.GREEN} 0 {Color.END}",
    0.25: f"{Color.GREEN} ¼ {Color.END}",
    0.50: f"{Color.GREEN} ½ {Color.END}",
    1.00: "   ",
    2.00: f"{Color.RED} 2 {Color.END}",
    4.00: f"{Color.RED} 4 {Color.END}",
}


def get_types_string(pokemon: Pokemon) -> str:
    if pokemon.secondary_type is None:
        return pokemon.primary_type.value
    else:
        return f"{pokemon.primary_type.value}, {pokemon.secondary_type.value}"


def get_base_stats_chart(pokemon: Pokemon) -> str:
    base_stats = vars(pokemon.base_stats)

    highest_stat = max(base_stats.values())
    lowest_stat = min(base_stats.values())

    stat_names = {
        "hp": "HP",
        "attack": "Attack",
        "defense": "Defense",
        "special_attack": "Sp. Atk",
        "special_defense": "Sp. Def",
        "speed": "Speed",
    }

    string_list = []
    for key, value in base_stats.items():
        string_list.append(f"{stat_names[key]:<9}")

        if value == highest_stat:
            color = Color.GREEN
        elif value == lowest_stat:
            color = Color.RED
        else:
            color = ""
        string_list.append(f"{color}{value:>4}{Color.END}")
        string_list.append(f" {'*' * (value // 5)}\n")

    string_list.append(
        f"{'Total':<9}"
        f"{Color.BOLD}{sum(base_stats.values()):>4}"
        f"{Color.END}\n"
    )
    return "".join(string_list)


def calculate_type_defenses(pokemon: Pokemon) -> TypeDefenses:
    type1 = pokemon.primary_type
    type2 = pokemon.secondary_type

    if type2 is None:
        return ALL_TYPE_DEFENSES[type1]
    else:
        return {
            t: ALL_TYPE_DEFENSES[type1][t] * ALL_TYPE_DEFENSES[type2][t]
            for t in PokemonType
        }


def get_type_defenses_chart(pokemon: Pokemon) -> str:
    type_defenses = calculate_type_defenses(pokemon)

    abbreviations = [
        attacking_type.value[0:3]
        for attacking_type, _ in type_defenses.items()
    ]
    row1 = "|".join(abbreviations)

    multipliers = [
        f"{MULTIPLIER_STRINGS[multiplier]}"
        for _, multiplier in type_defenses.items()
    ]
    row2 = "|".join(multipliers)

    return "\n".join([row1, row2])


def print_summary(pokemon: Pokemon) -> None:
    """
    Display a Pokémon's summary.

    Given a Pokémon object,
    format and print its classification, height, weight,
    base stat chart, and type defenses chart.

    :param pokemon The Pokémon object
    """
    print(
        f"{Color.BOLD}{Color.UNDERLINE}{pokemon.name.upper()}, "
        f"{pokemon.classification.upper()}{Color.END}"
    )
    print(
        f"{pokemon.height}m, "
        f"{pokemon.weight}kg"
    )
    print(get_types_string(pokemon))
    print()

    print(f"{Color.BOLD}BASE STATS{Color.END}")
    print(get_base_stats_chart(pokemon))

    print(f"{Color.BOLD}TYPE DEFENSES{Color.END}")
    print(get_type_defenses_chart(pokemon))
    print()
