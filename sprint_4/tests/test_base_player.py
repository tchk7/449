import pytest
from sprint_4.models.base_player import BasePlayer


@pytest.fixture
def player():
    return BasePlayer("Blue")


def test_base_player_setup(player):

    assert player.get_name() == "Blue Player"
    assert player.get_score() == 0
    assert player.is_computer() == False

def test_scores(player):

    player.set_score(1)

    assert player.get_score() == 1

    player.add_to_score(2)

    assert player.get_score() == 3