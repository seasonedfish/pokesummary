#!/usr/bin/env python3
import pandas as pd

"""
This module not used when the main program is executed
because the main program reads from modified dataset.
"""


def main():
    """
    Append the alternate form names to the names themselves in
    pokemon.csv, writing to pokemon_modified.csv

    :return: None
    """
    # Open from file
    df = pd.read_csv("pokemon.csv")
    # Make copy of rows that have alternate forms
    alt_pokemon = df.query("`Alternate Form Name` != ''")

    # Prepare regional demonyms
    regional_demonyms = [{"Alola": "Alolan"}, {"Galar": "Galarian"}]
    for dictionary in regional_demonyms:
        alt_pokemon["Alternate Form Name"].replace(dictionary, inplace=True)
    # Append all form names
    alt_pokemon["Pokemon Name"] = alt_pokemon["Alternate Form Name"] + " " + alt_pokemon["Pokemon Name"]
    # TODO: fix order of mega (e.g. Mega Charizard X, not Mega X Charizard)

    # Update original dataframe
    df.update(alt_pokemon)
    df.drop(["Alternate Form Name"], axis=1)
    # Write to file
    df.to_csv("pokemon_modified.csv", index=False)


if __name__ == "__main__":
    main()
