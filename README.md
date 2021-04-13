# Pokésummary
**In the heat of a Pokémon battle,
Pokésummary lets you quickly get the information you need!**

Pokésummary is an easy-to-use, informative command line interface (CLI)
for displaying Pokémon height, weight, types, base stats, and type defenses.
It works completely offline, opting to use local datasets instead of APIs.
It requires no third-party libraries.

![image](https://user-images.githubusercontent.com/29507110/113649578-adaebe00-965c-11eb-992f-7a0e2b051967.png)


## Usage
```txt
usage: pokesummary [-h] [-i] [-s] [-v] [pokemon [pokemon ...]]

Get summaries for a Pokémon or multiple Pokémon.

positional arguments:
  pokemon              the Pokémon to look up

optional arguments:
  -h, --help           show this help message and exit
  -i, --interactive    run interactively
  -s, --show-examples  show example uses of the program
  -v, --version        show program's version number and exit
```

## Installation

### Requirements
- Python 3.7+
- A terminal supporting ANSI escape codes
(most Linux and macOS terminals,
see [here](https://superuser.com/questions/413073/windows-console-with-ansi-colors-handling) for Windows)

### Install from PyPI
1. Install using pip
```sh
pip install pokesummary
```

### Install from Source Code
1. Clone or download the repository
2. Install using pip
```sh
pip3 install .
```

### Uninstall
1. Uninstall using pip
```sh
pip3 uninstall pokesummary
```

## Acknowledgements
- Type chart from [Pokémon Database](https://pokemondb.net/type)
- Pokémon data from [Yu-Chi Chiang's fixed database](https://www.kaggle.com/mrdew25/pokemon-database/discussion/165031)
