import sys

from PySide6.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QLabel, QLineEdit, QGridLayout, QApplication

from sprint_2.board import Board
from sprint_2.player import Player
from sprint_2.ui.board_ui import BoardUI
from sprint_2.ui.player_ui import PlayerUI


class GameUI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("SOS Game")

        game_board = Board()
        board_ui = BoardUI(game_board.size)
        blue_player = Player("Blue")
        player_ui = PlayerUI(blue_player)


        game_type_label = QLabel("Select Game Type")
        simple_checkbox = QCheckBox("Simple Game")
        general_checkbox = QCheckBox("General Game")
        board_size_text_box = QLineEdit("Board Size")

        mode_size_layout = QHBoxLayout()
        mode_size_layout.addWidget(game_type_label)
        mode_size_layout.addWidget(simple_checkbox)
        mode_size_layout.addWidget(general_checkbox)
        mode_size_layout.addWidget(board_size_text_box)

        player_turn_label = QLabel("{blue_player.name}'s Turn")

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addLayout(mode_size_layout, 0, 0, 1, 3)
        grid.addWidget(player_ui, 1, 0, 1, 1)
        grid.addWidget(board_ui, 1, 1, 1, 1)
        grid.addWidget(player_ui, 1, 2, 1, 1)
        grid.addWidget(player_turn_label, 2, 0, 1, 3)

        self.resize(500, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameUI()
    window.show()
    sys.exit(app.exec())

