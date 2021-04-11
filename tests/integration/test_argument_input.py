import pytest
import subprocess
from importlib import resources

FIXTURE_PACKAGE = "tests.integration.fixtures"


@pytest.fixture
def expected_single_pokemon_output():
    return resources.read_binary(FIXTURE_PACKAGE, "single_pokemon_output.ansi")


def test_single_pokemon(expected_single_pokemon_output):
    output = subprocess.check_output(["pokesummary", "bulbasaur"])
    assert output == expected_single_pokemon_output


@pytest.fixture
def expected_multiple_pokemon_output():
    return resources.read_binary(FIXTURE_PACKAGE, "multiple_pokemon_output.ansi")


def test_multiple_pokemon(expected_multiple_pokemon_output):
    output = subprocess.check_output(
        ["pokesummary", "bulbasaur", "ivysaur", "venusaur", "mega venusaur"]
    )
    assert output == expected_multiple_pokemon_output
