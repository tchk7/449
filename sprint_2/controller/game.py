from functools import partial

from sprint_2.model.board import Board


class Game():
    def __init__(self, game_ui):
        self.game_ui = game_ui
        self.board_ui = self.game_ui.get_board_ui()
        self.player_uis = self.game_ui.get_player_uis()
        self.current_player = 0

        self.buttons = []
        self.connect_buttons()

        # self.buttons = self.board_ui.get_buttons()
        #
        # for row_index, row in enumerate(self.buttons):
        #     for col_index, btn in enumerate(row):
        #         btn.clicked.connect(partial(self.handle_click, row_index, col_index))
        #
        self.game_ui.new_game.clicked.connect(self.start_new_game)

    def connect_buttons(self):
        self.buttons = self.board_ui.get_buttons()
        for row_index, row in enumerate(self.buttons):
            for col_index, btn in enumerate(row):
                btn.clicked.connect(partial(self.handle_click, row_index, col_index))

    def board_change(self, size):
        new_board = Board(size)

        self.board_ui = self.game_ui.build_board_ui(new_board)

        self.connect_buttons()

        self.start_new_game()


    def handle_click(self, row, col):
        board = self.board_ui.get_board()

        if not board.is_empty(row, col):
            return

        player_ui = self.player_uis[self.current_player]

        letter = player_ui.get_selected_letter()

        board.put_letter(row, col, letter)
        self.buttons[row][col].setText(letter)

        self.current_player = 1 - self.current_player

        next_player = self.player_uis[self.current_player]

        self.game_ui.player_turn_label.setText(f"{next_player.get_player().name}'s Turn")

    def start_new_game(self):
        self.board_ui.get_board().reset_board()

        for row in self.buttons:
            for btn in row:
                btn.setText("")

        self.current_player = 0

        next_player = self.player_uis[self.current_player]

        self.game_ui.player_turn_label.setText(f"{next_player.get_player().name}'s Turn")
