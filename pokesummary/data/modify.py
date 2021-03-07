#!/usr/bin/env python3
import pandas as pd

"""
This module not used when the main program is executed
because the main program reads from modified database.
"""


def main():
    """
    Append the alternate form names to the names themselves in
    pokemon.csv, writing to pokemon_modified.csv

    :return: None
    """
    # Open from file
    df = pd.read_csv("pokemon.csv")

    alt_pokemon = df.query("`Alternate Form Name` != ''")
    print(alt_pokemon["Pokemon Name"].head())

    # Prepare regional demonyms
    regional_demonyms = [{"Alola": "Alolan"}, {"Galar": "Galarian"}]
    for dictionary in regional_demonyms:
        alt_pokemon["Alternate Form Name"].replace(dictionary)
    # Append all other form names, including regional
    alt_pokemon["Pokemon Name"] = alt_pokemon["Alternate Form Name"] + " " + alt_pokemon["Pokemon Name"]

    # Write to file
    df.update(alt_pokemon)
    df.to_csv("new_pokemon.csv", index=False)


if __name__ == "__main__":
    main()
