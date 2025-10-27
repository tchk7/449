from sprint_3.models.base_game import BaseGame


class SimpleGame(BaseGame):
    def __init__(self, board, players):
        super().__init__(board, players)