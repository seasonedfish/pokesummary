import argparse
import sys

from .data_parse import parse_data
from .summary_print import print_summary


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
    :return: True if accessed, False if not accessed
    """
    try:
        print_summary(dictionary[pokemon])
        return True
    except KeyError:
        print(f"Invalid Pokémon {pokemon}")
        return False


def main():
    """
    Driver code.
    """
    data_dictionary = parse_data()
    args = prepare_args()

    input_pokemon = sys.stdin if args.interactive else args.pokemon
    for pokemon in input_pokemon:
        safe_print(
            data_dictionary,
            pokemon.rstrip().capitalize()
        )


if __name__ == "__main__":
    main()
