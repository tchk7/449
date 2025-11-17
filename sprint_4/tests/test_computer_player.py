import pytest

from sprint_4.models.board import Board
from sprint_4.models.computer_player import ComputerPlayer
from sprint_4.models.simple_game import SimpleGame


@pytest.fixture
def board():
    return Board(3)

@pytest.fixture
def player():
    return ComputerPlayer("Red")

@pytest.fixture
def game(board):
    return SimpleGame(board, [])


def test_is_computer():
    player = ComputerPlayer("Red")

    assert player.is_computer() == True

def test_decide_move(board, player, game):

    row, col, letter = player.decide_move(game.board, game)

    assert board.is_empty(row, col)
    assert letter in ['S', 'O']

def test_computer_win_move(board, player, game):

    board.put_letter(0, 0, 'S')
    board.put_letter(0, 2, 'S')

    row, col, letter = player.decide_move(board, game)

    assert (row, col) == (0, 1)
    assert letter == 'O'
