from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QRadioButton, QHBoxLayout, QButtonGroup
import sys

from sprint_4.models.player import Player

class PlayerUI(QWidget):
    def __init__(self):
        super().__init__()

        self.player  = None

        self.player_name_text = QLabel(self.player.get_name())
        self.player_name_text.setAlignment(Qt.AlignCenter)

        self.human_radio = QRadioButton("Human")
        self.human_radio.setChecked(True)
        self.computer_radio = QRadioButton("Computer")

        player_type_layout = QHBoxLayout()
        player_type_layout.addStretch()
        player_type_layout.addWidget(self.human_radio)
        player_type_layout.addWidget(self.computer_radio)
        player_type_layout.addStretch()



        human_layout = QVBoxLayout()
        human_layout.addWidget(self.human_radio)

        computer_layout = QVBoxLayout()
        computer_layout.addWidget(self.computer_radio)

        self.score = QLabel(f"Score: {self.player.get_score()}")
        self.score.setAlignment(Qt.AlignCenter)

        self.letter_s = QRadioButton("S")
        self.letter_s.setChecked(True)
        self.letter_o = QRadioButton("O")

        player_letter_layout = QHBoxLayout()
        player_letter_layout.addStretch()
        player_letter_layout.addWidget(self.letter_s)
        player_letter_layout.addWidget(self.letter_o)
        player_letter_layout.addStretch()


        self.player_type_group = QButtonGroup(self)
        self.player_type_group.addButton(self.human_radio)
        self.player_type_group.addButton(self.computer_radio)

        self.letter_group = QButtonGroup(self)
        self.letter_group.addButton(self.letter_s)
        self.letter_group.addButton(self.letter_o)



        player_layout = QVBoxLayout()
        player_layout.addWidget(self.player_name_text)
        player_layout.addLayout(player_type_layout)
        player_layout.addLayout(player_letter_layout)
        # player_layout.addWidget(self.letter_s, alignment=Qt.AlignCenter)
        # player_layout.addWidget(self.letter_o, alignment=Qt.AlignCenter)
        player_layout.addWidget(self.score)

        self.setLayout(player_layout)

    def get_selected_letter(self):
        """Get letter player wants to play"""

        if self.letter_s.isChecked():
            return "S"
        elif self.letter_o.isChecked():
            return "O"
        return None

    def get_player(self, player):

        self.player = player
        self.player_name_text.setText(self.player.get_name())
        self.update_score(self.player.get_score())

    def update_score(self, score):
        self.score.setText(f"Score: {score}")

    def is_computer(self):
        return self.computer_radio.isChecked()