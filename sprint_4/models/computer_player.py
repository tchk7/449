from sprint_4.models.base_player import BasePlayer


class ComputerPlayer(BasePlayer):
    def __init__(self, name):
        super().__init__(name)
