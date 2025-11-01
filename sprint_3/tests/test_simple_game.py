from idlelib.debugger_r import restart_subprocess_debugger

import pytest

from sprint_3.models.board import Board
from sprint_3.models.player import Player
from sprint_3.models.simple_game import SimpleGame

@pytest.fixture
def players():

    return [Player("Blue"), Player("Red")]

@pytest.fixture
def simple_game(players):

    board = Board(3)
    game = SimpleGame(board, players)

    return game


def test_simple_game_win(simple_game):
    game = simple_game

    game.board.grid[0][0] = 'S'
    game.board.grid[0][1] = 'O'
    game.board.grid[0][2] = 'S'

    result = game.handle_move(0, 2, 0)

    assert result == "WIN"
    assert game.game_over == True
    assert game.players[0].score == 1
    assert game.players[1].score == 0


def test_simple_game_continue(simple_game):
    game = simple_game

    game.board.grid[0][0] = 'S'

    result = game.handle_move(0, 0 , 0)

    assert result == "CONTINUE"
    assert game.game_over == False
    assert game.players[0].score == 0

def test_simple_game_draw(simple_game):
    game = simple_game

    game.board.grid[0][0] = 'S'
    game.board.grid[0][1] = 'S'
    game.board.grid[0][2] = 'O'
    game.board.grid[1][0] = 'S'
    game.board.grid[1][1] = 'S'
    game.board.grid[1][2] = 'S'
    game.board.grid[2][0] = 'S'
    game.board.grid[2][1] = 'S'
    game.board.grid[2][2] = 'O'

    result = game.handle_move(2, 2, 0)

    assert result == "DRAW"
    assert game.game_over == True
