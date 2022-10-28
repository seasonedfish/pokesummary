import pytest

from pokesummary.model import PokemonDict


@pytest.fixture()
def pokemon_dict():
    return PokemonDict()


def test_pokemon_dict_init(pokemon_dict):
    assert(len(pokemon_dict) == 1052)
    assert("Squirtle" in pokemon_dict)
    assert("Totodile" in pokemon_dict)
    assert("Mudkip" in pokemon_dict)
    assert("Piplup" in pokemon_dict)
    assert("Oshawott" in pokemon_dict)
    assert("Froakie" in pokemon_dict)
    assert("Popplio" in pokemon_dict)
    assert("Sobble" in pokemon_dict)


