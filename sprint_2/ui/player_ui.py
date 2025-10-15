from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QApplication, QRadioButton
import sys

from sprint_2.player import Player

class PlayerUI(QWidget):
    def __init__(self, player):
        super().__init__()

        self.player = player

        player_name = QLabel(player.name)
        player_name.setAlignment(Qt.AlignCenter)

        letter_s = QRadioButton("S")
        letter_s.setChecked(True)
        letter_o = QRadioButton("O")

        player_layout = QVBoxLayout()

        player_layout.addWidget(player_name)
        player_layout.addSpacing(5)
        player_layout.addWidget(letter_s, alignment=Qt.AlignCenter)
        player_layout.addWidget(letter_o, alignment=Qt.AlignCenter)

        self.setLayout(player_layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = Player("Blue")
    window = PlayerUI(player)
    window.show()
    sys.exit(app.exec())