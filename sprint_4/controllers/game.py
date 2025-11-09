from functools import partial

from sprint_4.models.board import Board
from sprint_4.models.general_game import GeneralGame
from sprint_4.models.simple_game import SimpleGame


class Game():
    def __init__(self, game_ui):
        self.game_ui = game_ui
        self.board_ui = self.game_ui.get_board_ui()
        self.player_uis = self.game_ui.get_player_uis()

        self.players = [self.player_uis[0].get_player(), self.player_uis[1].get_player()]

        self.current_player = 0

        self.buttons = []
        self.connect_buttons()

        self.game_mode = "Simple"
        self.game_type = SimpleGame(self.board_ui.get_board(), self.players)

        self.game_ui.simple_radio.toggled.connect(self.update_game_mode)
        self.game_ui.general_radio.toggled.connect(self.update_game_mode)

        self.game_ui.new_game.clicked.connect(self.start_new_game)

    def connect_buttons(self):
        self.buttons = self.board_ui.get_buttons()
        for row_index, row in enumerate(self.buttons):
            for col_index, btn in enumerate(row):
                btn.clicked.connect(partial(self.handle_click, row_index, col_index))

    def handle_click(self, row, col):
        board = self.board_ui.get_board()

        if not board.is_empty(row, col) or self.game_type.game_over:
            return

        player_ui = self.player_uis[self.current_player]

        letter = player_ui.get_selected_letter()

        self.buttons[row][col].setText(letter)

        status = self.game_type.handle_move(row, col, letter, self.current_player)

        switch_player = False

        if status == "WIN":
            winner = self.players[self.current_player].name
            self.game_ui.show_winner_message(f"{winner} wins.")
            self.game_ui.disable_board()

        elif status == "DRAW":
            self.game_ui.show_draw_message()
            self.game_ui.disable_board()

        elif status == "SCORE":
            # current_player_ui = self.player_uis[self.current_player]
            current_player_now = self.players[self.current_player]
            # current_player_ui.update_score(current_player_now.score)

            score = current_player_now.get_score()

            self.game_ui.update_player_score(self.current_player, score)

            switch_player = False
            self.game_ui.update_player_turn_label(f"{self.players[self.current_player].name} scores. Go again.")

        elif status == "CONTINUE":
            switch_player = True

        elif status == "We have a winner.":
            player_1_score = self.players[0].get_score()
            player_2_score = self.players[1].get_score()

            # self.player_uis[0].update_score(player_1_score)
            # self.player_uis[1].update_score(player_2_score)

            self.game_ui.update_player_score(0, player_1_score)
            self.game_ui.update_player_score(1, player_2_score)


            if player_1_score > player_2_score:
                winner = self.players[0].name
            else:
                winner = self.players[1].name

            self.game_ui.show_winner_message(f"{winner} wins with {max(player_1_score, player_2_score)} points.")
            self.game_ui.disable_board()

        elif status == "We have a draw.":
            self.game_ui.show_draw_message()
            self.game_ui.disable_board()

        if switch_player and not self.game_type.game_over:
            self.current_player = 1 - self.current_player

        if not self.game_type.game_over:
            next_player = self.players[self.current_player]
            self.game_ui.update_player_turn_label(f"{next_player.name}'s Turn")


    def start_new_game(self):

        text = self.game_ui.get_board_size_text()
        if text.isnumeric():
            size = int(text)
        else:
            size = 3

        board = Board(size)

        self.board_ui = self.game_ui.build_board_ui(board)
        self.connect_buttons()

        for player in self.players:
            player.set_score(0)

        # self.player_uis[0].update_score(0)
        # self.player_uis[1].update_score(0)

        self.game_ui.update_player_score(0, 0)
        self.game_ui.update_player_score(1, 0)

        self.current_player = 0

        if self.game_mode == "Simple":
            self.game_type = SimpleGame(board, self.players)
        else:
            self.game_type = GeneralGame(board, self.players)

        self.game_ui.update_player_turn_label(f"{self.players[0].name}'s Turn")
        self.game_ui.enable_board()

    def update_game_mode(self):
        if self.game_ui.simple_radio.isChecked():
            self.game_mode = "Simple"
        elif self.game_ui.general_radio.isChecked():
            self.game_mode = "General"
