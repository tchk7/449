from sprint_4.models.human_player import HumanPlayer


def test_human_not_computer():
    player = HumanPlayer("Blue")

    assert player.is_computer() == False