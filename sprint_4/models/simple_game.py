from sprint_4.models.base_game import BaseGame


class SimpleGame(BaseGame):
    def __init__(self, board, players):
        super().__init__(board, players)

    def handle_move(self, row, col, letter, player):

        self.board.put_letter(row, col, letter)

        if self.check_sos(row, col, letter) > 0:
            self.game_over = True
            moving_player = self.get_player(player)

            if moving_player:
                moving_player.set_score(1)

            return "WIN"

        if self.board.is_full():
            self.game_over = True
            return "DRAW"

        return "CONTINUE"