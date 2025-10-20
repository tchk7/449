from functools import partial


class Game():
    def __init__(self, game_ui):
        self.game_ui = game_ui
        self.board_ui = self.game_ui.get_board_ui()
        self.player_ui = self.game_ui.get_player_uis()



        self.buttons = self.board_ui.get_buttons()

        for row_index, row in enumerate(self.buttons):
            for col_index, btn in enumerate(row):
                btn.clicked.connect(partial(self.handle_click, row_index, col_index))


    def handle_click(self, row, col):
        board = self.board_ui.get_board()
        # player = self.player_ui.get_player()

        letter = "X"

        board.put_letter(row, col, letter)
        self.buttons[row][col].setText(letter)