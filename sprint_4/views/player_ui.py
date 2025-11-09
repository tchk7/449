from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QRadioButton
import sys

from sprint_4.models.player import Player

class PlayerUI(QWidget):
    def __init__(self, player):
        super().__init__()

        self.player = player

        player_name = QLabel(player.name)
        player_name.setAlignment(Qt.AlignCenter)

        self.score = QLabel(f"Score: {player.get_score()}")
        self.score.setAlignment(Qt.AlignCenter)

        self.letter_s = QRadioButton("S")
        self.letter_s.setChecked(True)
        self.letter_o = QRadioButton("O")

        player_layout = QVBoxLayout()

        player_layout.addWidget(player_name)
        player_layout.addWidget(self.letter_s, alignment=Qt.AlignCenter)
        player_layout.addWidget(self.letter_o, alignment=Qt.AlignCenter)
        player_layout.addWidget(self.score)

        self.setLayout(player_layout)

    def get_selected_letter(self):
        """Get letter player wants to play"""

        if self.letter_s.isChecked():
            return "S"
        elif self.letter_o.isChecked():
            return "O"
        return None

    def get_player(self):
        return self.player

    def update_score(self, score):
        self.score.setText(f"Score: {score}")