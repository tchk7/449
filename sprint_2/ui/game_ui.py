import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QLabel, QLineEdit, QGridLayout, QApplication, QVBoxLayout

from sprint_2.board import Board
from sprint_2.player import Player
from sprint_2.ui.board_ui import BoardUI
from sprint_2.ui.player_ui import PlayerUI


class GameUI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("SOS Game")

        game_board = Board(8)
        board_ui = BoardUI(game_board.size)
        blue_player = Player("Blue")
        blue_player_ui = PlayerUI(blue_player)
        red_player = Player("Red")
        red_player_ui = PlayerUI(red_player)



        game_type_label = QLabel("Select Game Type")
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


        player_turn_label = QLabel(f"{blue_player.name}'s Turn", alignment=Qt.AlignCenter)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(game_type_label, 0, 0, 1, 1)
        grid.addWidget(simple_checkbox, 0, 1, 1, 1)
        grid.addWidget(general_checkbox, 0, 2, 1, 1)
        # grid.addLayout(mode_size_layout, 0, 1, 1, 2)
        grid.addLayout(board_size_layout, 0, 3, 1, 1)
        grid.addWidget(QWidget(), 0, 2, 1, 1)
        grid.addWidget(blue_player_ui, 1, 0, 1, 1)
        grid.addWidget(board_ui, 1, 2, 1, 1)
        grid.addWidget(red_player_ui, 1, 4, 1, 1)
        grid.addWidget(player_turn_label, 2, 0, 1, 5)

        self.resize(500, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameUI()
    window.show()
    sys.exit(app.exec())


