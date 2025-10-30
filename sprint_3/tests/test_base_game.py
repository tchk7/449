from itertools import count

import pytest

from sprint_3.models.base_game import BaseGame
from sprint_3.models.board import Board


@pytest.fixture
def game_board():

    board = Board(5)
    game = BaseGame(board, players=None)

    return game

@pytest.mark.parametrize(
    "row, col, expected",
    [
        (0, 0, True),
        (0, 4, True),
        (4, 0, True),
        (4, 4, True),
        (1, 3, True),
        (-1, 0, False),
        (0, -1, False),
        (-2, -2, False),
        (5, 3, False),
        (3, 5, False),
        (6, 6, False)
    ]
)

def test_is_valid(game_board, row, col, expected):

    size = game_board.board.size
    assert game_board._is_valid(row, col, size) == expected

@pytest.mark.parametrize(
    "positions, row_col, expected",
    [
        ([(2, 2, 'S'), (3, 2, 'O'), (4, 2, 'S')], (3, 2), 1),
        ([(3, 1, 'S'), (3, 2, 'O'), (3, 3, 'S')], (3, 2), 1),
        ([(1, 1, 'S'), (2, 2, 'O'), (3, 3, 'S')], (2, 2), 1),
        ([(1, 3, 'S'), (2, 2, 'O'), (3, 1, 'S')], (2, 2), 1),
        ([(0, 0, 'S'), (0, 2, 'O'), (0, 4, 'S')], (0, 2), 0)
    ]
)

def test_check_sos_o(game_board, positions, row_col, expected):

    for row, col, letter in positions:
        game_board.board.grid[row][col] = letter

    row, col = row_col

    count = game_board.check_sos(row, col, 'O')

    assert count == expected

def test_check_sos_o_multiple(game_board):

    game_board.board.grid[2][1] = 'S'
    game_board.board.grid[2][3] = 'S'
    game_board.board.grid[1][2] = 'S'
    game_board.board.grid[3][2] = 'S'

    count = game_board.check_sos(2, 2, 'O')

    assert count == 2

@pytest.mark.parametrize(
    "positions, row_col, expected",
    [
        ([(2, 2, 'S'), (3, 2, 'O'), (4, 2, 'S')], (2, 2), 1),
        ([(3, 1, 'S'), (3, 2, 'O'), (3, 3, 'S')], (3, 3), 1),
        ([(1, 1, 'S'), (2, 2, 'O'), (3, 3, 'S')], (3, 3), 1),
        ([(1, 3, 'S'), (2, 2, 'O'), (3, 1, 'S')], (1, 3), 1),
        ([(0, 0, 'S'), (0, 2, 'O'), (0, 4, 'S')], (0, 4), 0),
    ]
)
def test_check_sos_s(game_board, positions, row_col, expected):
    for row, col, letter in positions:
        game_board.board.grid[row][col] = letter

    row, col = row_col

    count = game_board.check_sos(row, col, 'S')

    assert count == expected

def test_check_sos_s_multiple(game_board):

    game_board.board.grid[1][1] = 'S'
    game_board.board.grid[1][2] = 'O'
    game_board.board.grid[2][2] = 'O'
    game_board.board.grid[3][1] = 'S'

    count = game_board.check_sos(1, 3, 'S')

    assert count == 2





