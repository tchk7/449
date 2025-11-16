

class BasePlayer:
    def __init__(self, name):
        self.name = name + " Player"
        self._score = 0
        self._computer = False

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score

    def add_to_score(self, points):
        self._score += points

    def decide_move(self, board, game):
        return None

    def get_name(self):
        return self.name

    def is_computer(self):
        return self._computer