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
    #
    #     for col in range(1, self.cols):
    #         x = colIndex * width / self.cols
    #         painter.drawLine(int(xPosition), 0, int(xPosition), height)
    #
    #     for row in range(1, self.rows):
    #         yPosition = rowIndex * height / self.rows
    #         painter.drawLine(0, int(yPosition), width, int(yPosition))

if __name__ == "__main__":

    board = Board()

    app = QApplication(sys.argv)
    window = BoardUI(board)
    window.show()
    sys.exit(app.exec())

