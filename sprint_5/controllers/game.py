from functools import partial

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from sprint_5.models.board import Board
from sprint_5.models.computer_player import ComputerPlayer
from sprint_5.models.game_recorder import GameRecorder
from sprint_5.models.general_game import GeneralGame
from sprint_5.models.human_player import HumanPlayer
from sprint_5.models.simple_game import SimpleGame


class Game():
    def __init__(self, game_ui):
        self.game_ui = game_ui
        self.board_ui = self.game_ui.get_board_ui()
        self.player_uis = self.game_ui.get_player_uis()

        self.players = []

        self.current_player = 0

        self.buttons = []

        self.game_mode = "Simple"
        self.game_type = None

        self.recorder = GameRecorder()

        self.replay_timer = QTimer()
        self.replay_timer.timeout.connect(self._play_replay)
        self.replay_moves = []
        self.replay = 0

        self.game_ui.simple_radio.toggled.connect(self.update_game_mode)
        self.game_ui.general_radio.toggled.connect(self.update_game_mode)

        self.game_ui.new_game.clicked.connect(self.start_new_game)

        self.game_ui.replay_game_button.clicked.connect(self.start_replay)

        self.start_new_game()

    def connect_buttons(self):
        self.buttons = self.board_ui.get_buttons()
        for row_index, row in enumerate(self.buttons):
            for col_index, btn in enumerate(row):
                btn.clicked.connect(partial(self.handle_click, row_index, col_index))

    def handle_click(self, row, col):
        board = self.board_ui.get_board()

        if self.players[self.current_player].is_computer():
            return

        if not board.is_empty(row, col) or self.game_type.game_over:
            return

        self.game_ui.set_options_enabled(False)

        player_ui = self.player_uis[self.current_player]

        letter = player_ui.get_selected_letter()

        self.buttons[row][col].setText(letter)

        status = self.game_type.handle_move(row, col, letter, self.current_player)

        self.recorder.add_move(row, col, letter, self.current_player)

        self._process_move_status(status)

        self.check_game_over_save()

        if self.game_type.game_over:
            self.game_ui.set_options_enabled(True)

    def _handle_simple_win(self):
        winner = self.players[self.current_player].get_name()
        self.game_ui.show_winner_message(f"{winner} wins.")
        self.game_ui.disable_board()

    def _handle_draw(self):
        self.game_ui.show_draw_message()
        self.game_ui.disable_board()

    def _handle_general_win(self):
        player_1_score = self.players[0].get_score()
        player_2_score = self.players[1].get_score()

        self.game_ui.update_player_score(0, player_1_score)
        self.game_ui.update_player_score(1, player_2_score)

        if player_1_score > player_2_score:
            winner = self.players[0].get_name()
        else:
            winner = self.players[1].get_name()

        self.game_ui.show_winner_message(f"{winner} wins with {max(player_1_score, player_2_score)} points.")
        self.game_ui.disable_board()

    def _process_move_status(self, status):

        switch_player = False

        current_player_now = self.players[self.current_player]
        score = current_player_now.get_score()

        if status == "WIN":
            self.game_ui.update_player_score(self.current_player, score)
            self._handle_simple_win()

        elif status == "DRAW":
            self._handle_draw()

        elif status == "SCORE":
            switch_player = False
            self.game_ui.update_player_score(self.current_player, score)
            self.game_ui.update_player_turn_label(f"{self.players[self.current_player].get_name()} scores. Go again.")

        elif status == "CONTINUE":
            switch_player = True

        elif status == "We have a winner.":
            self._handle_general_win()


        elif status == "We have a draw.":
            self._handle_draw()

        if switch_player and not self.game_type.game_over:
            self.current_player = 1 - self.current_player

        if not self.game_type.game_over and status != "SCORE":
            next_player = self.players[self.current_player]
            self.game_ui.update_player_turn_label(f"{next_player.get_name()}'s Turn")

        if not self.replay_timer.isActive():
            self.check_player_turn()

    def start_new_game(self):

        size = self.game_ui.get_board_size()

        board = Board(size)

        self.players = []

        if self.player_uis[0].is_computer():
            self.players.append(ComputerPlayer("Blue (Computer)"))
        else:
            self.players.append(HumanPlayer("Blue"))

        if self.player_uis[1].is_computer():
            self.players.append(ComputerPlayer("Red (Computer)"))
        else:
            self.players.append(HumanPlayer("Red"))

        self.player_uis[0].link_player(self.players[0])
        self.player_uis[1].link_player(self.players[1])


        if self.game_mode == "Simple":
            self.game_type = SimpleGame(board, self.players)
        else:
            self.game_type = GeneralGame(board, self.players)

        self.game_ui.update_player_score(0, self.players[0].get_score())
        self.game_ui.update_player_score(1, self.players[1].get_score())

        self.board_ui = self.game_ui.build_board_ui(board)
        self.connect_buttons()

        self.current_player = 0

        self.game_ui.set_options_enabled(True)

        self.game_ui.update_player_turn_label(f"{self.players[0].get_name()}'s Turn")
        self.game_ui.enable_board()

        if self.game_ui.is_recording():
            if self.players[0].is_computer():
                player_1 = "Computer"
            else:
                player_1 = "Human"
            if self.players[1].is_computer():
                player_2 = "Computer"
            else:
                player_2 = "Human"
            self.recorder.record_game(self.game_mode, size, player_1, player_2)

        self.check_player_turn()

    def update_game_mode(self):

        self.game_mode = self.game_ui.get_game_mode()

    def check_player_turn(self):

        if self.game_type.game_over:
            return

        current_player_now = self.players[self.current_player]

        if current_player_now.is_computer():
            self.game_ui.disable_board()
            QApplication.processEvents()

            board = self.board_ui.get_board()

            next_move = current_player_now.decide_move(board, self.game_type)

            if next_move:
                row, col, letter = next_move
                self.process_computer_move(row, col, letter)

            else:
                self.game_ui.enable_board()

        else:
            self.game_ui.enable_board()

    def process_computer_move(self, row, col, letter):

        self.game_ui.set_options_enabled(False)

        self.buttons[row][col].setText(letter)

        status = self.game_type.handle_move(row, col, letter, self.current_player)

        self.recorder.add_move(row, col, letter, self.current_player)

        self._process_move_status(status)

        self.check_game_over_save()

        if self.game_type.game_over:
            self.game_ui.set_options_enabled(True)

    def start_replay(self):

        data = self.recorder.load_game()

        if not data:
            return

        game_settings = data.get("game_settings", {})
        self.replay_moves = data.get("moves", [])
        self.replay = 0

        board_size = game_settings.get("board_size", 3)
        game_mode = game_settings.get("mode", "Simple")

        self.game_ui.set_board_size_text(board_size)
        self.game_ui.set_game_mode(game_mode)

        self.start_new_game()

        self.game_ui.set_options_enabled(False)
        self.game_ui.disable_board()

        self.replay_timer.start(1000)




    def _play_replay(self):

        if self.replay < len(self.replay_moves):

            move = self.replay_moves[self.replay]
            row = move["row"]
            col = move["col"]
            letter = move["letter"]
            player = move["player"]

            self.current_player = player

            self.buttons[row][col].setText(letter)

            status = self.game_type.handle_move(row, col, letter, self.current_player)

            self._process_move_status(status)

            self.replay += 1

        else:

            self.replay_timer.stop()
            self.game_ui.set_options_enabled(True)

    def check_game_over_save(self):
        if self.game_type.game_over and self.recorder.get_recording_status():
            self.recorder.save_game("game_record")
