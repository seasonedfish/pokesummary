#!/usr/bin/env python3
import pandas as pd

"""
This module not used when the main program is executed
because the main program reads from modified dataset.
"""


def snake_case(columns):
    return columns \
        .str.replace(" ", "_", regex=False) \
        .str.replace(r"\W+", "", regex=True) \
        .str.lower()


def prune(df):
    kept_columns = [
        "pokemon_name",
        "classification",
        "pokemon_height",
        "pokemon_weight",
        "primary_type",
        "secondary_type",
        "health_stat",
        "attack_stat",
        "defense_stat",
        "special_attack_stat",
        "special_defense_stat",
        "speed_stat",
        "base_stat_total",
    ]
    return df[kept_columns]


def rename_alternate_forms(df):
    # Make copy of rows that have alternate forms
    alt_pokemon = df.query("`alternate_form_name` != ''")
    # Prepare regional demonyms
    regional_demonyms = [{"Alola": "Alolan"}, {"Galar": "Galarian"}]
    for dictionary in regional_demonyms:
        alt_pokemon["alternate_form_name"].replace(dictionary, inplace=True)
    # Append all form names
    alt_pokemon["pokemon_name"] = alt_pokemon["alternate_form_name"] + " " + alt_pokemon["pokemon_name"]
    # TODO: fix order of mega (e.g. Mega Charizard X, not Mega X Charizard)

    df1 = df.copy()
    df1.update(alt_pokemon)
    return df1


def main():
    """
    Append the alternate form names to the names themselves in
    pokemon.csv, writing to pokemon_modified.csv

    :return: None
    """
    df = pd.read_csv("pokemon_original.csv")

    df.columns = snake_case(df.columns)
    df = rename_alternate_forms(df)
    df = prune(df)

    df.to_csv("pokemon_modified.csv", index=False)


if __name__ == "__main__":
    main()
