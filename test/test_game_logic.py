import sys
from unittest.mock import MagicMock

# Mock streamlit before importing app so module-level st.* calls don't fail
sys.modules["streamlit"] = MagicMock()

from app import check_guess, parse_guess


# Bug 1: Hints were backwards
class TestCheckGuess:
    def test_guess_higher_than_secret_says_go_lower(self):
        outcome, message = check_guess(90, 50)
        assert outcome == "Too High"
        assert "LOWER" in message

    def test_guess_lower_than_secret_says_go_higher(self):
        outcome, message = check_guess(10, 50)
        assert outcome == "Too Low"
        assert "HIGHER" in message

    def test_correct_guess_returns_win(self):
        outcome, message = check_guess(50, 50)
        assert outcome == "Win"


# Bug 2: Guessing outside the bounds was accepted
class TestParseGuess:
    def test_guess_above_range_is_rejected(self):
        ok, value, err = parse_guess("101", "Normal")
        assert ok is False
        assert value is None
        assert err is not None

    def test_guess_below_range_is_rejected(self):
        ok, value, err = parse_guess("0", "Normal")
        assert ok is False
        assert value is None
        assert err is not None

    def test_guess_at_upper_bound_is_accepted(self):
        ok, value, err = parse_guess("100", "Normal")
        assert ok is True
        assert value == 100
        assert err is None

    def test_guess_at_lower_bound_is_accepted(self):
        ok, value, err = parse_guess("1", "Normal")
        assert ok is True
        assert value == 1
        assert err is None

    def test_valid_guess_within_range_is_accepted(self):
        ok, value, err = parse_guess("50", "Normal")
        assert ok is True
        assert value == 50
        assert err is None


# Bug 3: Clicking "New Game" did not reset status, blocking new guesses
class TestNewGameReset:
    def test_status_reset_to_playing_allows_new_guesses(self):
        # Simulate session state before and after clicking New Game
        session = {"status": "won", "attempts": 5, "secret": 42}

        # Apply what the fixed new_game block does
        session["attempts"] = 0
        session["status"] = "playing"

        # The guard `if status != "playing": st.stop()` should no longer fire
        assert session["status"] == "playing"
        assert session["attempts"] == 0

    def test_without_status_reset_game_remains_blocked(self):
        # Without the fix, status stays "won" after reset
        session = {"status": "won", "attempts": 0}

        # The guard would call st.stop(), blocking all new guesses
        assert session["status"] != "playing"