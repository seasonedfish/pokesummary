import argparse
from sys import stdin

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
    try:
        print_summary(dictionary[pokemon])
    except KeyError:
        print(f"Invalid Pokémon {pokemon}")


def main():
    """
    Driver code.
    """
    data_dictionary = parse_data()
    args = prepare_args()

    input_pokemon = stdin if args.interactive else args.pokemon
    for pokemon in input_pokemon:
        safe_print(
            data_dictionary,
            pokemon.rstrip().capitalize()
        )


if __name__ == "__main__":
    main()
