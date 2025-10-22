import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QLabel, QLineEdit, QGridLayout, QApplication, \
    QRadioButton, QPushButton

from sprint_2.controller.game import Game
from sprint_2.model.board import Board
from sprint_2.model.player import Player
from sprint_2.view.board_ui import BoardUI
from sprint_2.view.player_ui import PlayerUI


class GameUI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("SOS Game")

        self.game_board = Board()
        self.board_ui = BoardUI(self.game_board)
        self.blue_player = Player("Blue")
        self.blue_player_ui = PlayerUI(self.blue_player)
        self.red_player = Player("Red")
        self.red_player_ui = PlayerUI(self.red_player)

        self.new_game = QPushButton("New Game")

        self.game_type_label = QLabel("Game Mode:")
        self.simple_radio = QRadioButton("Simple Game")
        self.simple_radio.setChecked(True)
        self.general_radio = QRadioButton("General Game")

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.game_type_label)
        radio_layout.addWidget(self.simple_radio)
        radio_layout.addWidget(self.general_radio)

        board_size_label = QLabel("Board Size")
        self.board_size_text_box = QLineEdit()
        self.board_size_text_box.setValidator(QIntValidator(3, 12))
        self.board_size_text_box.setPlaceholderText("Choose 3 to 12")

        board_size_layout = QHBoxLayout()
        board_size_layout.addWidget(board_size_label)
        board_size_layout.addWidget(self.board_size_text_box)


        self.player_turn_label = QLabel(f"{self.blue_player.name}'s Turn", alignment=Qt.AlignCenter)

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.grid.addLayout(radio_layout, 0, 0, 1, 2)
        self.grid.addLayout(board_size_layout, 0, 3, 1, 1)
        self.grid.addWidget(QWidget(), 0, 2, 1, 1)
        self.grid.addWidget(self.blue_player_ui, 2, 0, 1, 1)
        self.grid.addWidget(self.board_ui, 1, 1, 3, 3)
        self.grid.addWidget(self.red_player_ui, 2, 4, 1, 1)
        self.grid.addWidget(self.player_turn_label, 4, 0, 1, 5)
        self.grid.addWidget(self.new_game, 0, 4, 1, 1)

        self.resize(500, 500)

        self.controller = Game(self)

    def get_player_uis(self):
        return [self.blue_player_ui, self.red_player_ui]

    def get_board_ui(self):
        return self.board_ui

    def build_board_ui(self, board):

        self.grid.removeWidget(self.board_ui)

        self.board_ui.deleteLater()

        self.game_board = board
        self.board_ui = BoardUI(self.game_board)
        self.grid.addWidget(self.board_ui, 1, 1, 3, 3)

        return self.board_ui


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameUI()
    window.show()
    sys.exit(app.exec())


