from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QApplication, QPushButton
import sys

from sprint_2.board import Board


class BoardUI(QWidget):
    def __init__(self, size = 3):
        super().__init__()

        self.setWindowTitle("SOS Game")
        self.board = Board(size)

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

        # for rowIndex in range(self.board.size):
        #     for colIndex in range(self.board.size):
        #         cell = QLabel(f"[{rowIndex + 1}, {colIndex + 1}]")
        #         cell.setAlignment(Qt.AlignCenter)
        #         self.grid_layout.addWidget(cell, rowIndex, colIndex)

    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #
    #     width = self.width()
    #     height = self.height()
    #     size = self.board.size
    #
    #     for col in range(1, size):
    #         x = col * width / size
    #         painter.drawLine(int(x), 0, int(x), height)
    #
    #     for row in range(1, size):
    #         y = row * height / size
    #         painter.drawLine(0, int(y), width, int(y))

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = BoardUI()
    window.show()
    sys.exit(app.exec())

