import itertools
from enum import Enum

from pokesummary import parsing


class Color(str, Enum):
    GREEN = "\033[49;32m"
    RED = "\033[49;31m"

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# Parses the grid of type defenses.
# The csv file is modified from the
# visual chart on Pokémon Database.
# https://pokemondb.net/type
all_type_defenses = parsing.csv_to_nested_dict(
    "pokesummary.data",
    "type_defenses_modified.csv",
    "defending_type",
    lambda x: float(x)
)


def get_base_stats(pokemon_stats):
    keys_list = list(pokemon_stats.keys())
    start = keys_list.index("health_stat")
    stop = keys_list.index("base_stat_total")
    base_stats = dict(itertools.islice(pokemon_stats.items(), start, stop))
    return {k: int(v) for k, v in base_stats.items()}


def get_base_stats_chart(pokemon_stats):
    base_stats = get_base_stats(pokemon_stats)

    highest_stat = max(base_stats.values())
    lowest_stat = min(base_stats.values())

    stat_names = {
        "health_stat": "HP",
        "attack_stat": "Attack",
        "defense_stat": "Defense",
        "special_attack_stat": "Sp. Atk",
        "special_defense_stat": "Sp. Def",
        "speed_stat": "Speed",
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
        f"{Color.BOLD}{pokemon_stats['base_stat_total']:>4}"
        f"{Color.END}\n"
    )
    return "".join(string_list)


def calculate_type_defenses(pokemon_stats):
    type1 = pokemon_stats["primary_type"]
    type2 = pokemon_stats["secondary_type"]

    if type2 == "":
        return all_type_defenses[type1]
    else:
        return {
            k: all_type_defenses[type1][k] * all_type_defenses[type2][k]
            for k in all_type_defenses[type1].keys()
        }


def get_type_defenses_chart(type_defenses):
    abbreviations = [
        attacking_type[0:3]
        for attacking_type in type_defenses
    ]
    row1 = "|".join(abbreviations)

    multipliers = [
        f"{format_multiplier(type_defenses[attacking_type])}"
        for attacking_type in type_defenses
    ]
    row2 = "|".join(multipliers)

    return "\n".join([row1, row2])


def format_multiplier(multiplier):
    if multiplier == 0:
        return f"{Color.GREEN} 0 {Color.END}"
    elif multiplier == 0.25:
        return f"{Color.GREEN} ¼ {Color.END}"
    elif multiplier == 0.5:
        return f"{Color.GREEN} ½ {Color.END}"
    elif multiplier == 1:
        return "   "
    elif multiplier == 2:
        return f"{Color.RED} 2 {Color.END}"
    elif multiplier == 4:
        return f"{Color.RED} 4 {Color.END}"
    else:
        raise ValueError("Multiplier must be 0, 0.25, 0.5, 1, 2, or 4")


def display_summary(pokemon_name, pokemon_stats):
    """
    Given a Pokémon's name and a dictionary of its stats,
    format and print its classification, height, weight,
    base stat chart, and type defenses chart.

    :param pokemon_name: the name of the Pokémon
    :param pokemon_stats: a dictionary of the Pokémon's stats
    """
    print(
        f"{Color.BOLD}{Color.UNDERLINE}{pokemon_name.upper()}, "
        f"{pokemon_stats['classification'].upper()}{Color.END}"
    )
    print(
        f"{pokemon_stats['pokemon_height']}m, "
        f"{pokemon_stats['pokemon_weight']}kg")
    print(
        f"{pokemon_stats['primary_type']}"
        f"{', ' if pokemon_stats['secondary_type'] != '' else ''}"
        f"{pokemon_stats['secondary_type']}"
    )
    print()

    print(f"{Color.BOLD}BASE STATS{Color.END}")
    print(get_base_stats_chart(pokemon_stats))

    print(f"{Color.BOLD}TYPE DEFENSES{Color.END}")
    type_defenses = calculate_type_defenses(pokemon_stats)
    print(get_type_defenses_chart(type_defenses))
    print()
