class Player:
    def __init__(self, name):
        self.name = name + " Player"
        self._score = 0

    def get_score(self):
        return self._score

    def add_to_score(self, points):
         self._score += points

    def set_score(self, score):
        self._score = score

