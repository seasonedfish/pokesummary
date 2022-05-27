# Pokésummary
**In the heat of a Pokémon battle,
Pokésummary lets you quickly get the information you need!**

Pokésummary is an easy-to-use, informative command line interface (CLI)
for displaying Pokémon height, weight, types, base stats, and type defenses.
It works completely offline, opting to use local datasets instead of APIs.
It requires no third-party libraries.

![image](https://user-images.githubusercontent.com/29507110/113649578-adaebe00-965c-11eb-992f-7a0e2b051967.png)


## Usage

### Command-line usage
The simplest example is passing a Pokémon name as an argument.
Here, we want to display Bulbasaur's summary,
so we pass `bulbasaur` as an argument.

    pokesummary bulbasaur

Multiple Pokémon names can be chained.
Now, we pass the names of Bulbasaur's whole evolution line.
Note that Pokémon names consisting of multiple words
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

### Python library usage
Starting from version 2.0.0, you can use Pokésummary as a library.
```pycon
>>> from pokesummary.model import PokemonDict
>>> pokemon_dict = PokemonDict()
>>> my_pokemon = pokemon_dict["Lanturn"]
>>> my_pokemon
Pokemon(name='Lanturn', classification='Light Pokémon', height=1.2, weight=22.5, primary_type=<PokemonType.WATER: 'Water'>, secondary_type=<PokemonType.ELECTRIC: 'Electric'>, base_stats=PokemonBaseStats(hp=125, attack=58, defense=58, special_attack=76, special_defense=76, speed=67))
```

## Installation

### Requirements
- Python 3.7+
- A terminal supporting ANSI escape codes
(most Linux and macOS terminals,
see [here](https://superuser.com/questions/413073/windows-console-with-ansi-colors-handling) for Windows)

### Install from PyPI
1. Install using pip
```console
pip3 install pokesummary
```

### Install from Source Code
1. Clone or download the repository
2. Install using pip
```console
pip3 install .
```

### Uninstall
1. Uninstall using pip
```console
pip3 uninstall pokesummary
```

## Contributing
Please see [CONTRIBUTING.md](./CONTRIBUTING.md).

## Acknowledgements
- Type chart from [Pokémon Database](https://pokemondb.net/type)
- Pokémon data from [Yu-Chi Chiang's fixed database](https://www.kaggle.com/mrdew25/pokemon-database/discussion/165031)
