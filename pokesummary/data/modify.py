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

    pd.options.mode.use_inf_as_na = True
    alt_forms = df.loc[df["Alternate Form Name"].notnull(), "Alternate Form Name"]
    print(alt_forms.head())

    # Prepare regional demonyms
    regional_demonyms = [{"Alola": "Alolan"}, {"Galar": "Galarian"}]
    for dictionary in regional_demonyms:
        alt_forms.replace(dictionary)
    # Append all form names, including regional
    df["Pokemon Name"] = alt_forms + " " + df["Pokemon Name"]
    df["Pokemon Name"].str.lstrip()

    # Write to file
    df.to_csv("new_pokemon.csv", index=False)


if __name__ == "__main__":
    main()
