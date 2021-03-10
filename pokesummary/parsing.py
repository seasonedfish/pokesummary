import csv
from collections import namedtuple
from importlib import resources

PokemonStats = namedtuple(
    "PokemonStats",
    [
        "pokemon_id",
        "pokedex_number",
        "pokemon_name",
        "classification",
        "original_pokemon_id",
        "legendary_type",
        "pokemon_height",
        "pokemon_weight",
        "primary_type",
        "secondary_type",
        "primary_ability",
        "primary_ability_description",
        "secondary_ability",
        "secondary_ability_description",
        "hidden_ability",
        "hidden_ability_description",
        "special_event_ability",
        "special_event_ability_description",
        "male_ratio",
        "female_ratio",
        "base_happiness",
        "games_of_origin",
        "region_of_origin",
        "health_stat",
        "attack_stat",
        "defense_stat",
        "special_attack_stat",
        "special_defense_stat",
        "speed_stat",
        "base_stat_total",
        "health_ev",
        "attack_ev",
        "defense_ev",
        "special_attack_ev",
        "special_defense_ev",
        "speed_ev",
        "ev_yield_total",
        "catch_rate",
        "experience_growth",
        "experience_growth_total",
        "experience_yield",
        "primary_egg_group",
        "secondary_egg_group",
        "egg_cycle_count",
        "preevolution_pokemon_id",
        "evolution_details",
    ],
)


def parse_data():
    with resources.open_text("pokesummary.data", "pokemon_modified.csv") as f:
        data_iterator = csv.DictReader(f)
        data_dictionary = {
            row["pokemon_name"]: PokemonStats(**row)
            for row in data_iterator
        }
    return data_dictionary
