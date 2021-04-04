# Pokésummary
An easy-to-use, informative command line interface (CLI)
for accessing Pokémon summaries.

Currently in development.

## Usage
```
usage: pokesummary [-h] [-i] [pokemon [pokemon ...]]

Get summaries for a Pokémon or multiple Pokémon.

positional arguments:
  pokemon            the Pokémon to look up

optional arguments:
  -h, --help         show this help message and exit
  -i, --interactive  run interactively
```

## Installation

### Requirements
- Python 3.7+
- A terminal supporting ANSI escape codes (most Linux and MacOS terminals, Windows Terminal on Windows)

## Manual Install
1. Clone or download the repository
2. Install using pip or Poetry

Using pip:
```sh
pip3 install .
```

Using poetry:
```sh
poetry install
```

## Acknowledgements
- Type chart from [Pokémon Database](https://pokemondb.net/type)
- Pokémon data from [Yu-Chi Chiang's fixed database](https://www.kaggle.com/mrdew25/pokemon-database/discussion/165031)
