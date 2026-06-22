import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_secret_as_string():
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high_with_string_secret():
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low_with_string_secret():
    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
