import pytest

from sprint_3.models.board import Board
from sprint_3.models.general_game import GeneralGame
from sprint_3.models.player import Player

@pytest.fixture
def players():

    return [Player("Blue"), Player("Red")]

@pytest.fixture
def general_game(players):

    board = Board(3)

    game = GeneralGame(board, players)

    return game


def test_general_game_score(general_game):
    game = general_game

    game.board.grid[0][0] = 'S'
    game.board.grid[0][1] = 'O'
    game.board.grid[0][2] = 'S'

    result = game.handle_move(0, 2, 0)

    assert result == "SCORE"
    assert game.game_over == False
    assert game.players[0].score == 1
    assert game.players[1].score == 0


def test_general_game_score_multiple(general_game):
    game = general_game

    game.board.grid[0][0] = 'S'
    game.board.grid[0][2] = 'S'
    game.board.grid[2][0] = 'S'
    game.board.grid[2][2] = 'S'
    game.board.grid[1][1] = 'O'

    result = game.handle_move(1, 1, 1)

    assert result == "SCORE"
    assert game.game_over == False
    assert game.players[0].score == 0
    assert game.players[1].score == 2

def test_general_game_continue(general_game):
    game = general_game

    game.board.grid[0][0] = 'S'
    game.board.grid[0][1] = 'S'
    game.board.grid[0][2] = 'S'

    result = game.handle_move(0, 2, 0)

    assert result == "CONTINUE"
    assert game.game_over == False
    assert game.players[0].score == 0
    assert game.players[1].score == 0

def test_general_game_win_full_board(general_game):
    game = general_game

    game.board.grid[0][0] = 'S'
    game.board.grid[0][1] = 'S'
    game.board.grid[0][2] = 'S'
    game.board.grid[1][0] = 'O'
    game.board.grid[1][1] = 'O'
    game.board.grid[1][2] = 'S'
    game.board.grid[2][0] = 'S'
    game.board.grid[2][1] = 'S'
    game.board.grid[2][2] = 'S'

    game.players[0].score = 2
    game.players[1].score = 1

    result = game.handle_move(2, 2, 0)

    assert result == "We have a winner."
    assert game.game_over == True

def test_general_game_draw_full_board(general_game):
    game = general_game

    game.board.grid[0][0] = 'S'
    game.board.grid[0][1] = 'O'
    game.board.grid[0][2] = 'S'
    game.board.grid[1][0] = 'S'
    game.board.grid[1][1] = 'S'
    game.board.grid[1][2] = 'S'
    game.board.grid[2][0] = 'S'
    game.board.grid[2][1] = 'O'
    game.board.grid[2][2] = 'S'

    game.players[0].score = 1
    game.players[1].score = 1

    result = game.handle_move(1, 1, 1)

    assert result == "We have a draw."
    assert game.game_over == True

