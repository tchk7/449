import pytest

from sprint_5.models.board import Board
from sprint_5.models.general_game import GeneralGame
from sprint_5.models.human_player import HumanPlayer

@pytest.fixture
def players():

    return [HumanPlayer("Blue"), HumanPlayer("Red")]

@pytest.fixture
def general_game(players):

    board = Board(3)

    game = GeneralGame(board, players)

    return game


def test_general_game_score(general_game):
    game = general_game

    game.board.put_letter(0, 0, 'S')
    game.board.put_letter(0, 1, 'O')

    result = game.handle_move(0, 2,'S', 0)

    assert result == "SCORE"
    assert game.game_over == False
    assert game.get_player(0).get_score() == 1
    assert game.get_player(1).get_score() == 0


def test_general_game_score_multiple(general_game):
    game = general_game

    game.board.put_letter(0, 0, 'S')
    game.board.put_letter(0, 2, 'S')
    game.board.put_letter(2, 0, 'S')
    game.board.put_letter(2, 2, 'S')

    result = game.handle_move(1, 1, 'O', 1)

    assert result == "SCORE"
    assert game.game_over == False
    assert game.get_player(0).get_score() == 0
    assert game.get_player(1).get_score() == 2

def test_general_game_continue(general_game):
    game = general_game

    game.board.put_letter(0, 0, 'S')
    game.board.put_letter(0, 1, 'S')

    result = game.handle_move(0, 2, 'S', 0)

    assert result == "CONTINUE"
    assert game.game_over == False
    assert game.get_player(0).get_score() == 0
    assert game.get_player(1).get_score() == 0

def test_general_game_win_full_board(general_game):
    game = general_game

    game.board.put_letter(0, 0, 'S')
    game.board.put_letter(0, 1, 'S')
    game.board.put_letter(0, 2, 'S')
    game.board.put_letter(1, 0, 'O')
    game.board.put_letter(1, 1, 'O')
    game.board.put_letter(1, 2, 'S')
    game.board.put_letter(2, 0, 'S')
    game.board.put_letter(2, 1, 'S')

    game.get_player(0).set_score(2)
    game.get_player(1).set_score(1)

    result = game.handle_move(2, 2, 'S', 0)

    assert result == "We have a winner."
    assert game.game_over == True

def test_general_game_draw_full_board(general_game):
    game = general_game

    game.board.put_letter(0, 0, 'S')
    game.board.put_letter(0, 1, 'O')
    game.board.put_letter(0, 2, 'S')
    game.board.put_letter(1, 0, 'O')
    game.board.put_letter(1, 1, 'S')
    game.board.put_letter(1, 2, 'S')
    game.board.put_letter(2, 0, 'S')
    game.board.put_letter(2, 1, 'S')
    game.board.put_letter(2, 2, 'S')

    game.get_player(0).set_score(1)
    game.get_player(1).set_score(1)

    result = game.handle_move(2, 2,'O',  1)

    assert result == "We have a draw."
    assert game.game_over == True

