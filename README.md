# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game purpose:** A number guessing game where the player tries to guess a secret number. The game gives "Too High" or "Too Low" hints after each guess and tracks the score across rounds.

**Bugs found:**
1. **Hint logic reversed** — "Too High" returned when guess was below secret, "Too Low" when above.
2. **Difficulty settings wrong** — Easy=6, Medium=8, Hard=4 guesses. Order was incorrect; Easy should allow the most guesses.
3. **Secret number changed on every submit** — No session state, so each button click regenerated a new secret number.
4. **Restart broken** — Restart button did not fully clear session state, leaving stale values.

**Fixes applied:**
1. Swapped the `>` / `<` comparison in `check_guess` so hints match the correct direction.
2. Corrected the max-guesses mapping for each difficulty level.
3. Stored the secret number in `st.session_state` so it persists across button clicks.
4. Reset all relevant session state keys in the restart handler.

## 📸 Demo Walkthrough

1. User starts a new game on Easy difficulty (10 max guesses). Secret number is 53.
2. User enters a guess of 30 → game returns "Too Low".
3. User enters a guess of 80 → game returns "Too High".
4. Score counter updates after each guess, showing attempts used.
5. User enters a guess of 53 → game returns "You Win! 🎉" and the round score is recorded.
6. User clicks "Restart Game" → session state clears, a new secret number is generated, and a fresh round begins.

## 🧪 Test Results

```
$ python -m pytest tests/ -v
============================= test session starts ==============================
platform darwin -- Python 3.12.7, pytest-7.4.4, pluggy-1.6.0
collecting ... collected 6 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 16%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 33%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 50%]
tests/test_game_logic.py::test_secret_as_string PASSED                   [ 66%]
tests/test_game_logic.py::test_guess_too_high_with_string_secret PASSED  [ 83%]
tests/test_game_logic.py::test_guess_too_low_with_string_secret PASSED   [100%]

============================== 6 passed in 0.02s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
