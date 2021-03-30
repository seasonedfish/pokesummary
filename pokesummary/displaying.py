import csv
from enum import Enum
from importlib import resources


class Color(str, Enum):
    WEAK = "\033[49;32m"
    RESISTANT = "\033[49;31m"
    IMMUNE = "\033[49;34m"

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def parse_all_type_defenses():
    with resources.open_text("pokesummary.data", "type_defenses_modified.csv") as f:
        data_iterator = csv.DictReader(f)
        types_dictionary = {
            row["defending_type"]: row
            for row in data_iterator
        }
        for defending_type in types_dictionary.keys():
            del types_dictionary[defending_type]["defending_type"]

            for attacking_type in types_dictionary[defending_type].keys():
                types_dictionary[defending_type][attacking_type] = float(
                    types_dictionary[defending_type][attacking_type]
                )

    return types_dictionary


all_type_defenses = parse_all_type_defenses()


def display_summary(pokemon_stats):
    # TODO: implement
    print(f"{Color.BOLD}{pokemon_stats['pokemon_name'].upper()}, {pokemon_stats['classification'].upper().upper()}{Color.END}")
    print(f"{pokemon_stats['pokemon_height']}m, {pokemon_stats['pokemon_weight']}kg")

    type_defenses = calculate_type_defenses(pokemon_stats)
    print(f"{Color.BOLD}TYPE DEFENSES{Color.END}")
    for attacking_type in type_defenses:
        print(f"{attacking_type:<10}{format_multiplier(type_defenses[attacking_type])}")


def format_multiplier(multiplier):
    if multiplier == 0:
        return f"{Color.IMMUNE}0×{Color.END}"
    elif multiplier == 0.25:
        return f"{Color.RESISTANT}¼×{Color.END}"
    elif multiplier == 0.5:
        return f"{Color.RESISTANT}½×{Color.END}"
    elif multiplier == 1:
        return ""
    elif multiplier == 2:
        return f"{Color.WEAK}2×{Color.END}"
    elif multiplier == 4:
        return f"{Color.WEAK}4×{Color.END}"
    else:
        raise ValueError("Multiplier must be 0, 0.25, 0.5, 1, 2, or 4")


def calculate_type_defenses(pokemon_stats):
    if pokemon_stats["secondary_type"] == "":
        return all_type_defenses[pokemon_stats["primary_type"]]
    else:
        return {
            k: all_type_defenses[pokemon_stats["primary_type"]][k] * all_type_defenses[pokemon_stats["secondary_type"]][
                k]
            for k in all_type_defenses[pokemon_stats["primary_type"]].keys()
        }
