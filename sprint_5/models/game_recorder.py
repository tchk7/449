class GameRecorder:
    def __init__(self):
        self.moves = []
        self.game_settings = {}
        self.is_recording = False

    def add_move(self, row, col, letter, player):

        move = {"row": row,
                "col": col,
                "letter": letter,
                "player": player
                }
        self.moves.append(move)

    def record_game(self, game_mode, board_size, player_type_1, player_type_2):
        self.moves = []
        self.game_settings = {"mode": game_mode,
                              "board_size": board_size,
                              "player_type_1": player_type_1,
                              "player_type_2": player_type_2
                              }
        self.is_recording = True

