import argparse
import sys

from pokesummary import displaying, parsing


def prepare_args():
    """
    Use argparse to create the command-line interface.

    :return: the namespace of program arguments
    """
    parser = argparse.ArgumentParser(
        description="Get summaries for a Pokémon or multiple Pokémon."
    )
    parser.add_argument(
        "pokemon",
        nargs="*",
        help="the Pokémon to look up"
    )
    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="run interactively"
    )
    return parser.parse_args()


def safe_print(dictionary, pokemon):
    """
    Tries to print a summary of the Pokémon specified by string ``pokemon``.
    If ``pokemon`` is not a key in the dictionary, return gracefully.

    :param dictionary: the dict of Pokémon/Pokémon info pairs
    :param pokemon: the key to access
    """
    try:
        pokemon_stats = dictionary[pokemon]
    except KeyError:
        print(f"Invalid Pokémon {pokemon}\n")
        return
    displaying.display_summary(pokemon, pokemon_stats)


def main():
    """
    Driver code.
    """
    args = prepare_args()
    data_dictionary = parsing.csv_to_nested_dict(
        "pokesummary.data",
        "pokemon_modified.csv",
        "pokemon_name"
    )

    input_pokemon = sys.stdin if args.interactive else args.pokemon
    for pokemon in input_pokemon:
        safe_print(
            data_dictionary,
            pokemon.rstrip().title()
        )


if __name__ == "__main__":
    main()
