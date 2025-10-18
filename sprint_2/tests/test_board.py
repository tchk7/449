from sprint_2.model.board import Board

def test_default_board():
    board = Board()
    assert board.size == 3

def test_initial_board():
    board = Board(size= 3)
    assert board.size == 3
    for row in range(board.size):
        for col in range(board.size):
            assert board.get_cell(row, col) == ""

def test_minimum_board_size():
    board = Board(size=2)
    assert board.size == 3


def test_put_letter():
    board = Board(3)
    letter_played = board.put_letter(0, 0, "S")
    assert letter_played == True
    assert board.get_cell(0, 0) == "S"

def test_non_empty_cell():
    board = Board(3)
    assert board.is_empty(0, 0)
    board.put_letter(0, 0, "S")
    assert not board.is_empty(0, 0)
    letter_played = board.put_letter(0, 0, "O")
    assert letter_played == False

def test_full_board():
    board = Board(3)
    assert board.is_full() == False

    for row in range(board.size):
        for col in range(board.size):
            board.put_letter(row, col, "S")
    assert board.is_full() == True

def test_reset_board():
    board = Board(3)
    for row in range(board.size):
        for col in range(board.size):
            board.put_letter(row, col, "S")
    assert not board.is_empty(0, 0)
    assert board.is_full() == True
    board.reset_board()
    assert board.is_full() == False