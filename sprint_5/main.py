import sys

from PySide6.QtWidgets import QApplication

from sprint_5.controllers.game import Game
from sprint_5.views.game_ui import GameUI


def main():
    app = QApplication(sys.argv)

    view = GameUI()

    controller = Game(view)

    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()