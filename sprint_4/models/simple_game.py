from sprint_3.models.base_game import BaseGame


class SimpleGame(BaseGame):
    def __init__(self, board, players):
        super().__init__(board, players)

    def handle_move(self, row, col, player):

        letter = self.board.get_cell(row, col)

        if self.check_sos(row, col, letter) > 0:
            self.game_over = True
            self.players[player].score = 1
            return "WIN"

        if self.board.is_full():
            self.game_over = True
            return "DRAW"

        return "CONTINUE"