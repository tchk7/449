from idlelib.debugger_r import restart_subprocess_debugger

import pytest

from sprint_4.models.board import Board
from sprint_4.models.player import Player
from sprint_4.models.simple_game import SimpleGame

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

    game.board.put_letter(0, 0, 'S')
    game.board.put_letter(0, 1, 'O')

    result = game.handle_move(0, 2, 'S', 0)

    assert result == "WIN"
    assert game.game_over == True
    assert game.get_player(0).get_score() == 1
    assert game.get_player(1).get_score() == 0


def test_simple_game_continue(simple_game):
    game = simple_game

    result = game.handle_move(0, 0, 'O', 0)

    assert result == "CONTINUE"
    assert game.game_over == False
    assert game.get_player(0).get_score() == 0

def test_simple_game_draw(simple_game):
    game = simple_game

    game.board.put_letter(0, 0, 'S')
    game.board.put_letter(0, 1, 'O')
    game.board.put_letter(0, 2, 'S')
    game.board.put_letter(1, 0, 'S')
    game.board.put_letter(1, 1, 'S')
    game.board.put_letter(1, 2, 'S')
    game.board.put_letter(2, 0, 'S')
    game.board.put_letter(2, 1, 'S')

    result = game.handle_move(2, 2, 'O', 0)

    assert result == "DRAW"
    assert game.game_over == True
