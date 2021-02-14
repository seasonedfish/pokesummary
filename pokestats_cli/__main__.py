import argparse
from sys import stdin

from .data_parse import parse_data
from .summary_print import print_summary


def get_args_namespace():
    parser = argparse.ArgumentParser(
        description="Get stats for a Pokémon or multiple Pokémon."
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


def main():
    data_dictionary = parse_data()
    args = get_args_namespace()

    if args.interactive:
        for line in stdin:
            print_summary(data_dictionary[line])
    else:
        for pokemon in args.pokemon:
            print_summary(data_dictionary[pokemon])


if __name__ == "__main__":
    main()
