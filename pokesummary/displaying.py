from enum import Enum
from pokesummary import parsing


class Color(str, Enum):
    WEAK = "\033[49;32m"
    RESISTANT = "\033[49;31m"
    IMMUNE = "\033[49;34m"

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


all_type_defenses = parsing.csv_to_2d_dict(
    "pokesummary.data",
    "type_defenses_modified.csv",
    "defending_type",
    lambda x: float(x)
)


def calculate_type_defenses(pokemon_stats):
    primary_type = pokemon_stats["primary_type"]
    secondary_type = pokemon_stats["secondary_type"]

    if secondary_type == "":
        return all_type_defenses[primary_type]
    else:
        return {
            k: all_type_defenses[primary_type][k] * all_type_defenses[secondary_type][k]
            for k in all_type_defenses[primary_type].keys()
        }


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


def display_summary(pokemon_stats):
    print(
        f"{Color.BOLD}{pokemon_stats['pokemon_name'].upper()}, "
        f"{pokemon_stats['classification'].upper()}{Color.END}"
    )
    print(f"{pokemon_stats['pokemon_height']}m, {pokemon_stats['pokemon_weight']}kg")

    print(f"{Color.BOLD}TYPE DEFENSES{Color.END}")
    type_defenses = calculate_type_defenses(pokemon_stats)
    for attacking_type in type_defenses:
        print(f"{attacking_type:<10}{format_multiplier(type_defenses[attacking_type])}")
