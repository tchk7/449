import json
import os

import pytest

from sprint_5.models.game_recorder import GameRecorder


@pytest.fixture
def recorder():
    return GameRecorder()


def test_record_game(recorder):
    recorder.record_game("Simple", 3, "Human", "Computer")

    assert recorder.get_recording_status() == True
    assert recorder._game_settings["mode"] == "Simple"
    assert recorder._game_settings["board_size"] == 3

def test_add_move(recorder):
    recorder.record_game("Simple", 3, "Human", "Computer")
    recorder.add_move(0, 0, "S", 0)

    assert len(recorder._moves) == 1
    assert recorder._moves[0] == {"row": 0,
                                  "col": 0,
                                  "letter": "S",
                                  "player": 0
                                  }

def test_add_move_not_recording(recorder):

    recorder.add_move(0, 0, "S", 0)

    assert len(recorder._moves) == 0

def test_save_game(recorder, tmp_path):

    recorder.record_game("Simple", 3, "Human", "Computer")
    recorder.add_move(0, 0, "S", 0)

    file_path = str(tmp_path / "test_save_game.json")

    result = recorder.save_game(file_path)

    assert os.path.exists(file_path) == True
    assert result == True
    assert recorder.get_recording_status() == True

    with open(file_path, "r") as file:
        data = json.load(file)

    assert data["game_settings"]["mode"] == "Simple"
    assert data["game_settings"]["board_size"] == 3
    assert data["moves"][0]["letter"] == "S"

def test_load_game(recorder, tmp_path):

    file_path = str(tmp_path / "test_load_game.json")

    data = {"game_settings":
                {"mode": "Simple",
                 "board_size": 3,
                 "player_type_1" : "Human",
                 "player_type_2" : "Computer"
                 },
            "moves": [{"row": 0, "col": 0, "letter": "S", "player": 0}]
            }

    with open(file_path, "w") as file:
        json.dump(data, file)

    loaded_game = recorder.load_game(file_path)

    assert loaded_game is not None
    assert loaded_game.game_settings["mode"] == "Simple"
    assert loaded_game.game_settings["board_size"] == 3
    assert len(loaded_game.moves) == 1
    assert loaded_game.moves[0]["row"] == 0


def test_load_game_not_found(recorder, tmp_path):

    file_path = str(tmp_path / "test_load_game_not_found.json")
    result = recorder.load_game(file_path)

    assert result is None

