
from sprint_2.model.player import Player
from sprint_2.model.board import Board

def test_player_letter_choice():
    blue = Player("Blue")
    blue.set_letter("S")
    assert blue.letter == "S"

def test_player_move():
    board = Board()
    blue = Player("Blue")
    blue.set_letter("S")

    assert board.is_empty(0, 0) == True

    blue.make_move(board, 0, 0)

    assert board.is_empty(0, 0) == False
    assert board.get_cell(0, 0) == "S"
