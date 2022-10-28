"""
This package contains the datasets that Pokésummary needs to function.

These files are not packaged (only available in the repo):
- pokemon_original.csv
    This is the original Pokémon dataset,
    created by Dakota Worzella and Yu-Chi Chiang.
    https://www.kaggle.com/datasets/mrdew25/pokemon-database/discussion/165031
- type_defenses_original.csv
    This is the original type defenses grid,
    copied from the visual chart on Pokémon Database.
    https://pokemondb.net/type
- modify_pokemon
    This is a Python script that uses Pandas
    to generate pokemon_modified.csv from pokemon_original.csv.
- modify_type_defenses
    This is a Python script that uses Pandas
    to generate type_defenses_modified.csv from type_defenses_original.csv.

These files are packaged:
- pokemon_modified.csv
    Pokésummary reads this file to get its data on Pokémon.
    It is the reduced version of pokemon_original.csv,
    generated using the modify_pokemon script.
- type_defenses_modified.csv
    Pokésummary reads this file to get the type defense float values.
    It is the modified version of type_defenses_original.csv,
    generated using the modify_type_defenses script.
    Its non-numeric fields must be quoted
    so that Python can read the numbers directly as floats.
"""