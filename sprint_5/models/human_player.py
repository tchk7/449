from sprint_5.models.base_player import BasePlayer


class HumanPlayer(BasePlayer):
    def __init__(self, name):
        super().__init__(name)
        self._computer = False


    def decide_move(self, board, game):
        return None