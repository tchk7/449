from sprint_3.models.base_game import BaseGame


class GeneralGame(BaseGame):
    def __init__(self, board, players):
        super().__init__(board, players)

    def handle_move(self, row, col, player):

        letter = self.board.get_cell(row, col)

        count = self.check_sos(row, col, letter)

        if count > 0:
            self.players[player].score += count

            if self.board.is_full():
                return self._check_winner()

            return "SCORE"

        if self.board.is_full():
            return self._check_winner()

        return "CONTINUE"

    def _check_winner(self):

        self.game_over = True

        if self.players[0].score > self.players[1].score:
            return "We have a winner."
        elif self.players[1].score > self.players[0].score:
            return "We have a winner."
        else:
            return "We have a draw."