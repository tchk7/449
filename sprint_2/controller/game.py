from functools import partial


class Game():
    def __init__(self, game_ui):
        self.game_ui = game_ui
        self.board_ui = self.game_ui.get_board_ui()
        self.player_uis = self.game_ui.get_player_uis()
        self.current_player = 0



        self.buttons = self.board_ui.get_buttons()

        for row_index, row in enumerate(self.buttons):
            for col_index, btn in enumerate(row):
                btn.clicked.connect(partial(self.handle_click, row_index, col_index))


    def handle_click(self, row, col):
        board = self.board_ui.get_board()
        player_ui = self.player_uis[self.current_player]

        letter = player_ui.get_selected_letter()

        board.put_letter(row, col, letter)
        self.buttons[row][col].setText(letter)

        self.current_player = 1 - self.current_player

        next_player = self.player_uis[self.current_player]

        self.game_ui.player_turn_label.setText(f"{next_player.get_player().name}'s Turn")
