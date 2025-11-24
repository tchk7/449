import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QLabel, QLineEdit, QGridLayout, QApplication, \
    QRadioButton, QPushButton, QMessageBox

from sprint_5.models.board import Board
from sprint_5.views.board_ui import BoardUI
from sprint_5.views.player_ui import PlayerUI


class GameUI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("SOS Game")

        self._init_models()
        self._init_player_uis()

        self.new_game = QPushButton("New Game")

        self.game_type_label = QLabel("Game Mode:")
        self.simple_radio = QRadioButton("Simple Game")
        self.simple_radio.setChecked(True)
        self.general_radio = QRadioButton("General Game")

        self._build_radio_layout()

        self._init_layout()

        self.grid.addWidget(QWidget(), 0, 2, 1, 1)
        self.grid.addWidget(self.blue_player_ui, 2, 0, 1, 1)
        self.grid.addWidget(self.board_ui, 1, 1, 3, 3)
        self.grid.addWidget(self.red_player_ui, 2, 4, 1, 1)
        self.grid.addWidget(self.player_turn_label, 4, 0, 1, 5)
        self.grid.addWidget(self.new_game, 0, 4, 1, 1)

        self.resize(500, 500)

    def _init_models(self):
        self.game_board = Board()
        self.board_ui = BoardUI(self.game_board)

    def _init_player_uis(self):
        self.blue_player_ui = PlayerUI()
        self.red_player_ui = PlayerUI()
        self.player_uis = [self.blue_player_ui, self.red_player_ui]

    def _init_layout(self):
        board_size_label = QLabel("Board Size")
        self.board_size_text_box = QLineEdit()
        self.board_size_text_box.setValidator(QIntValidator(3, 12))
        self.board_size_text_box.setPlaceholderText("Choose 3 to 12")

        board_size_layout = QHBoxLayout()
        board_size_layout.addWidget(board_size_label)
        board_size_layout.addWidget(self.board_size_text_box)

        self.player_turn_label = QLabel(f"SOS Game New", alignment=Qt.AlignCenter)
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.grid.addLayout(self._build_radio_layout(), 0, 0, 1, 2)
        self.grid.addLayout(board_size_layout, 0, 3, 1, 1)
        self.grid.addWidget(self._build_board_ui(), 1, 1, 3, 3)

        left, right = self._build_player_uis()
        self.grid.addWidget(left, 2, 0)
        self.grid.addWidget(right, 2, 4)

    def _build_radio_layout(self):
        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.game_type_label)
        radio_layout.addWidget(self.simple_radio)
        radio_layout.addWidget(self.general_radio)
        return radio_layout

    def _build_player_uis(self):
        return self.blue_player_ui, self.red_player_ui

    def _build_board_ui(self):
        return self.board_ui

    def get_player_uis(self):
        return self.player_uis

    def get_board_ui(self):
        return self.board_ui

    def build_board_ui(self, board):

        self.grid.removeWidget(self.board_ui)

        self.board_ui.deleteLater()

        self.game_board = board
        self.board_ui = BoardUI(self.game_board)
        self.grid.addWidget(self.board_ui, 1, 1, 3, 3)

        return self.board_ui

    def show_winner_message(self, message):
        QMessageBox.information(self, "Game Over", message)

    def show_draw_message(self):
        QMessageBox.information(self, "Game Over", "We have a draw.")

    def disable_board(self):
        self.board_ui.setEnabled(False)

    def enable_board(self):
        self.board_ui.setEnabled(True)

    def update_player_turn_label(self, player_name):
        self.player_turn_label.setText(player_name)

    def update_player_score(self, player, score):

        if 0 <= player < len(self.player_uis):
            self.player_uis[player].update_score(score)

    def get_board_size(self):

        text = self.board_size_text_box.text()
        if text.isnumeric():
            return int(text)
        return 3

    def set_options_enabled(self, is_enabled):
        self.board_size_text_box.setEnabled(is_enabled)
        self.simple_radio.setEnabled(is_enabled)
        self.general_radio.setEnabled(is_enabled)

        for player_ui in self.player_uis:
            player_ui.set_options_enabled(is_enabled)

    def get_game_mode(self):

        if self.simple_radio.isChecked():
            return "Simple"
        return "General"

