"""
This module provides the command-line interface for Pokésummary.
In terms of model-view-controller, this is the controller.
"""

import argparse
import string
import sys

from pokesummary import __version__, view
from pokesummary.model import PokemonDict


def prepare_args(args=None):
    """
    Use argparse to create the command-line interface.

    :param args: a list of arguments passed to the program.
    If no value is given, use the sys.argv[1:] arguments.
    :return: the namespace of program arguments
    """
    parser = argparse.ArgumentParser(
        description="Get summaries for a Pokémon or multiple Pokémon."
    )
    parser.add_argument(
        "pokemon_names",
        nargs="*",
        help="the Pokémon to look up"
    )
    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="run interactively"
    )
    parser.add_argument(
        "-s", "--show-examples",
        action="store_true",
        help="show example uses of the program",
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"pokesummary {__version__}",
    )
    return parser.parse_args(args)


def print_examples():
    """
    Print example uses of the program, along with commentary.
    """
    examples = """The simplest example is passing a Pokémon as an argument.
Here, we want to display Bulbasaur's summary,
so we pass `bulbasaur` as an argument.

    pokesummary bulbasaur

Multiple Pokémon can be chained.
Now, we pass Bulbasaur's whole evolution line.
Note that Pokémon with multi-word names
(e.g. Mega Venusaur) must be surrounded by quotation marks.

    pokesummary bulbasaur ivysaur venusaur "mega venusaur"

If you would like to run pokesummary interactively,
use the `-i` flag.
Now we can type several Pokémon names,
hitting Enter after each one.
Use Ctrl-D (EOF) to exit.

    pokesummary -i

Since the `-i` flag reads from standard input,
we can pipe Pokémon names to it.
If we have a file `pokemon_names.txt`
filled with Pokémon names (each separated by newline),
we can use the following to display each of their summaries.

    cat pokemon_names.txt | pokesummary -i
    """
    print(examples)


def safe_print(dictionary, pokemon_name):
    """
    Try to print a summary of a Pokémon.

    If the given dictionary lacks the given Pokémon name as one of its keys,
    handle it gracefully.

    :param dictionary: the dict of Pokémon name/Pokémon info pairs
    :param pokemon_name: the Pokémon name to look up
    """
    try:
        pokemon = dictionary[pokemon_name]
    except KeyError:
        print(f"Invalid Pokémon {pokemon_name}\n")
        return

    view.print_summary(pokemon)


def run_program(pokemon_names, interactive, show_examples):
    """
    Run the program.

    :param pokemon_names: a list of Pokémon names to look up
    :param interactive: if the program should read from standard input
    :param show_examples: if the program should print example uses
    """
    if show_examples:
        print_examples()
        return

    data_dictionary = PokemonDict().data

    input_pokemon = sys.stdin if interactive else pokemon_names
    for pokemon in input_pokemon:
        safe_print(data_dictionary, string.capwords(pokemon))


def main():
    """
    Driver code.
    """
    cli_args = prepare_args()
    run_program(**vars(cli_args))


if __name__ == "__main__":
    main()
