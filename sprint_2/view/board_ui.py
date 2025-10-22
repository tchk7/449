from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QApplication, QPushButton
import sys

from sprint_2.model.board import Board


class BoardUI(QWidget):
    def __init__(self, board):
        super().__init__()

        self.setWindowTitle("SOS Game")
        self.board = board

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        self.buttons = []
        for row in range(self.board.size):
            button_row = []
            for col in range(self.board.size):
                btn = QPushButton("")
                btn.setFixedSize(60, 60)
                self.grid_layout.addWidget(btn, row, col)
                button_row.append(btn)
            self.buttons.append(button_row)



    def get_buttons(self):
        return self.buttons

    def get_board(self):
        return self.board

