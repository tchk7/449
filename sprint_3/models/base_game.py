class BaseGame:
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.game_over = False

    def check_sos(self):
        return