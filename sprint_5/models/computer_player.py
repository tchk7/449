import random

from sprint_5.models.base_player import BasePlayer


class ComputerPlayer(BasePlayer):
    def __init__(self, name):
        super().__init__(name)
        self._computer = True


    def decide_move(self, board, game_type):

        empty_cells = board.get_empty_cells()

        if not empty_cells:
            return None, None, None

        for (row, col) in empty_cells:
            if game_type.check_sos(row, col, 'S') > 0:
                return row, col, 'S'
            elif game_type.check_sos(row, col, 'O') > 0:
                return row, col, 'O'

        (row, col) = random.choice(empty_cells)
        letter = random.choice(['S', 'O'])

        return (row, col, letter)

