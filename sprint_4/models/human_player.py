from sprint_4.models.base_player import BasePlayer


class HumanPlayer(BasePlayer):
    def __init__(self, name):
        super().__init__(name)


    def make_move(self, board, game):
        return