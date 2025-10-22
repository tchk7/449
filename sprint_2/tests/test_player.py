
from sprint_2.model.player import Player

def test_player_letter_choice():
    blue = Player("Blue")
    blue.set_letter("S")
    assert blue.letter == "S"
