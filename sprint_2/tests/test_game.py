import sys
from unittest.mock import MagicMock

import pytest
from PySide6.QtWidgets import QApplication

# This assumes your project structure allows this import.
# If you run into ModuleNotFoundError, you may need to adjust your Python path.
from sprint_2.controller.game import Game


@pytest.fixture(scope="session")
def qapp():
    """
    This fixture creates a QApplication instance for the entire test session.
    A QApplication is necessary to test any code that interacts with Qt widgets,
    even if the widgets are not physically shown.
    """
    # Check if a QApplication instance already exists
    app = QApplication.instance()
    if app is None:
        # If not, create one
        app = QApplication(sys.argv)
    return app


@pytest.fixture
def game_with_mock_ui(qapp):
    """
    This fixture sets up a Game instance with a mocked UI.
    Mocking the UI allows us to test the game's logic in isolation,
    without needing to interact with a live GUI.
    """
    # 1. Create a mock object that pretends to be the GameUI
    mock_game_ui = MagicMock()

    # 2. The Game's __init__ method calls get_board_ui() and get_player_uis().
    #    We need to ensure these methods exist on our mock and return other mocks.
    mock_game_ui.get_board_ui.return_value = MagicMock()
    mock_game_ui.get_player_uis.return_value = [MagicMock(), MagicMock()]

    # 3. Instantiate the Game class, passing in our mocked UI
    game = Game(mock_game_ui)

    # 4. Return both the game instance and the mock UI so our tests can use them
    return game, mock_game_ui


def test_default_game_mode_is_simple(game_with_mock_ui):
    """
    Given a new game instance,
    When the game is initialized,
    Then the default game mode should be "Simple".
    """
    # The fixture 'game_with_mock_ui' creates the game instance
    game, _ = game_with_mock_ui

    # Assert that the game_mode attribute is set to "Simple" by default
    assert game.game_mode == "Simple"


def test_changing_game_mode_to_general(game_with_mock_ui):
    """
    Given a game instance in the default "Simple" mode,
    When the general game mode radio button is selected,
    Then the game mode should be updated to "General".
    """
    game, mock_game_ui = game_with_mock_ui

    # 1. (Optional) Confirm the initial state is "Simple"
    assert game.game_mode == "Simple"

    # 2. Simulate the UI change: the user clicks the "General" radio button.
    #    In the UI, this would make simple_radio unchecked and general_radio checked.
    #    We simulate this by telling our mocks what to return when isChecked() is called.
    mock_game_ui.simple_radio.isChecked.return_value = False
    mock_game_ui.general_radio.isChecked.return_value = True

    # 3. Manually call the update_game_mode method.
    #    In the actual application, the 'toggled' signal from the radio button
    #    would trigger this method. In our test, we call it directly.
    game.update_game_mode()

    # 4. Assert that the game mode has been successfully changed
    assert game.game_mode == "General"
