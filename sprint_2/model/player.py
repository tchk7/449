


class Player:
    def __init__(self, name):
        self.name = name + " Player"
        self.letter = ""

    def set_letter(self, letter_choice):
        if letter_choice.upper() in ("S", "O"):
            self.letter = letter_choice
        else:
            raise ValueError("Letter must be an 'S' or 'O'")

