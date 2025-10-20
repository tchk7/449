import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QLabel, QLineEdit, QGridLayout, QApplication

from sprint_2.controller.game import Game
from sprint_2.model.board import Board
from sprint_2.model.player import Player
from sprint_2.view.board_ui import BoardUI
from sprint_2.view.player_ui import PlayerUI


class GameUI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("SOS Game")

        self.game_board = Board(8)
        self.board_ui = BoardUI(self.game_board)
        self.blue_player = Player("Blue")
        self.blue_player_ui = PlayerUI(self.blue_player)
        self.red_player = Player("Red")
        self.red_player_ui = PlayerUI(self.red_player)



        game_type_label = QLabel("Game Mode:")
        simple_checkbox = QCheckBox("Simple Game")
        general_checkbox = QCheckBox("General Game")

        checkbox_layout = QHBoxLayout()
        # checkbox_layout.addWidget(game_type_label)
        checkbox_layout.addWidget(simple_checkbox)
        checkbox_layout.addWidget(general_checkbox)


        # mode_size_layout = QVBoxLayout()
        # # mode_size_layout.addWidget(game_type_label, alignment=Qt.AlignCenter)
        # mode_size_layout.addLayout(checkbox_layout)

        board_size_label = QLabel("Board Size")
        board_size_text_box = QLineEdit()

        board_size_layout = QHBoxLayout()
        board_size_layout.addWidget(board_size_label)
        board_size_layout.addWidget(board_size_text_box)


        player_turn_label = QLabel(f"{self.blue_player.name}'s Turn", alignment=Qt.AlignCenter)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(game_type_label, 0, 0, 1, 1)
        grid.addWidget(simple_checkbox, 0, 1, 1, 1)
        grid.addWidget(general_checkbox, 0, 2, 1, 1)
        # grid.addLayout(mode_size_layout, 0, 1, 1, 2)
        grid.addLayout(board_size_layout, 0, 3, 1, 1)
        grid.addWidget(QWidget(), 0, 2, 1, 1)
        grid.addWidget(self.blue_player_ui, 2, 0, 1, 1)
        grid.addWidget(self.board_ui, 1, 1, 3, 3)
        grid.addWidget(self.red_player_ui, 2, 4, 1, 1)
        grid.addWidget(player_turn_label, 4, 0, 1, 5)

        self.controller = Game(self)

        self.resize(500, 500)

    def get_player_uis(self):
        return [self.blue_player_ui, self.red_player_ui]

    def get_board_ui(self):
        return self.board_ui


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameUI()
    window.show()
    sys.exit(app.exec())


