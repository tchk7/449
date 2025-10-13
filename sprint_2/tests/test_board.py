
import pytest
from sprint_2.board import Board

def test_default_board():
    board = Board()
    assert board.size == 3

def test_initial_board():
    board = Board(size= 3)
    assert board.size == 3
    for row in range(board.size):
        for col in range(board.size):
            assert board.get_cell(row, col) == ""