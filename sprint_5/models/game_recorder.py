import json
import os


class GameRecorder:
    def __init__(self):
        self._moves = []
        self._game_settings = {}
        self._is_recording = False

    def add_move(self, row, col, letter, player):
        if self._is_recording:

            move = {"row": row,
                    "col": col,
                    "letter": letter,
                    "player": player
                    }
            self._moves.append(move)

    def record_game(self, game_mode, board_size, player_type_1, player_type_2):
        self._moves = []
        self._game_settings = {"mode": game_mode,
                              "board_size": board_size,
                              "player_type_1": player_type_1,
                              "player_type_2": player_type_2
                              }
        self._is_recording = True

    def save_game(self, file="game_record"):

        if not self._moves:
            return False

        data = {"moves": self._moves,
                "game_settings": self._game_settings
                }

        with open(file, "w") as outfile:
            json.dump(data, outfile)

        self._is_recording = False
        return True

    def load_game(self, file="game_record"):

        if not os.path.isfile(file):
            return None

        with open(file, "r") as infile:
            data = json.load(infile)
        return data

    def get_recording_status(self):
        return self._is_recording