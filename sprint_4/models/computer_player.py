import random

from sprint_4.models.base_player import BasePlayer


class ComputerPlayer(BasePlayer):
    def __init__(self, name):
        super().__init__(name)
        self._computer = True


    def make_move(self, board, game):

        empty_cells = board.get_empty_cells()

        if not empty_cells:
            return

        row, col = random.choice(empty_cells)
        letter = random.choice(['S', 'O'])

        game.handle_click(row, col, letter)
