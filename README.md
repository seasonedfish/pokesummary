# Pokésummary
An easy-to-use, informative command line interface (CLI)
for accessing Pokémon summaries.

Currently in development.

## Screenshot
![image](https://user-images.githubusercontent.com/29507110/113600322-d52a6a00-960d-11eb-8813-ed86f394adf2.png)

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
- A terminal supporting ANSI escape codes
(most Linux and macOS terminals,
see [here](https://superuser.com/questions/413073/windows-console-with-ansi-colors-handling) for Windows)

### Manual Install
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
