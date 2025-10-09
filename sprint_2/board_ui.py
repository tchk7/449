from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QApplication
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

        for rowIndex in range(self.board.size):
            for colIndex in range(self.board.size):
                cell = QLabel(f"[{rowIndex + 1}, {colIndex + 1}]")
                cell.setAlignment(Qt.AlignCenter)
                self.grid_layout.addWidget(cell, rowIndex, colIndex)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = BoardUI()
    window.show()
    sys.exit(app.exec())

