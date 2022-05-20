import pytest

from pokesummary.model import PokemonDict


@pytest.fixture()
def pokemon_dict():
    return PokemonDict()


def test_pokemon_dict_init(pokemon_dict):
    pokemon_data = pokemon_dict.data
    assert(len(pokemon_data) == 1052)
    assert("Squirtle" in pokemon_data)
    assert("Totodile" in pokemon_data)
    assert("Mudkip" in pokemon_data)
    assert("Piplup" in pokemon_data)
    assert("Oshawott" in pokemon_data)
    assert("Froakie" in pokemon_data)
    assert("Popplio" in pokemon_data)
    assert("Sobble" in pokemon_data)


