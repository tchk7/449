import sys

from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QLabel, QWidget, QCheckBox, QRadioButton, QGridLayout, QApplication

class Board(QWidget):
    def __init__(self, rows = 3, cols = 3):
        super().__init__()
        self.rows = rows
        self.cols = cols


    def paintEvent(self, event):
        painter = QPainter(self)

        width = self.width()
        height = self.height()

        for colIndex in range(1, self.cols):
            xPosition = colIndex * width / self.cols
            painter.drawLine(int(xPosition), 0, int(xPosition), height)

        for rowIndex in range(1, self.rows):
            yPosition = rowIndex * height / self.rows
            painter.drawLine(0, int(yPosition), width, int(yPosition))

class Window(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Sample SOS Game")
        checkboxSimple = QCheckBox("Simple Game")
        checkboxDynamic = QCheckBox("Dynamic Game")

        radioHuman = QRadioButton("Human Button")
        radioComputer = QRadioButton("Computer Button")

        board = Board(rows=3, cols=3)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(label, 0, 0, 1, 2)
        grid.addWidget(board, 1, 0, 1, 2)
        grid.addWidget(checkboxSimple, 2, 0)
        grid.addWidget(checkboxDynamic, 2, 1)
        grid.addWidget(radioHuman, 3, 0)
        grid.addWidget(radioComputer, 3, 1)

        self.resize(500, 500)







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())