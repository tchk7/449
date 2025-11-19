from sprint_5.models.base_game import BaseGame


class GeneralGame(BaseGame):
    def __init__(self, board, players):
        super().__init__(board, players)

    def handle_move(self, row, col, letter, player):

        self.board.put_letter(row, col, letter)

        count = self.check_sos(row, col, letter)

        if count > 0:
            moving_player = self.get_player(player)

            if moving_player:
                moving_player.add_to_score(count)

            if self.board.is_full():
                return self._check_winner()

            return "SCORE"

        if self.board.is_full():
            return self._check_winner()

        return "CONTINUE"

    def _check_winner(self):

        self.game_over = True

        if self.get_player(0).get_score() > self.get_player(1).get_score():
            return "We have a winner."
        elif self.get_player(1).get_score() > self.get_player(0).get_score():
            return "We have a winner."
        else:
            return "We have a draw."