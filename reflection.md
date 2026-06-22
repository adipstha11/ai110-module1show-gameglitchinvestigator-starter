# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess is too high or too low | If too high, say “go lower.” If too low, say “go higher.” | The game gives the opposite hint both ways. | No console error; logic is incorrect. |
| Select Easy, Medium, Hard | Easy should have most guesses, Medium fewer, Hard least. | Easy = 6, Medium = 8, Hard = 4, so the order is wrong. | No console error; difficulty settings are incorrect. |
| Finish game and click Restart Game | Game should fully reset and start a new round. | Restart button does not properly restart the game. | No console error; restart functionality is broken. |
| inputting answer | should just take in input and increase attempt if wrong| some times the submit answer button doesnt process command| just does not process command|
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

asnwer -
I used Claude as my AI coding assistant during this project. One helpful suggestion Claude gave was to look closely at the conditional statements inside the guess-checking logic because the high and low hints were reversed. I verified this by running the app again and testing guesses above and below the secret number to make sure the hints matched the correct direction. Claude also helped me think about moving game logic into logic_utils.py so the code would be easier to test.

Not every AI suggestion was perfect. At first, Claude only focused on the if/else condition and did not fully identify the whole bug. After fixing one part of the hint logic, I realized there was another issue where the secret number was sometimes being treated as a string instead of consistently as an integer. I had to ask Claude to look through the code again, and then I manually verified the fix by running both the app and the pytest tests.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
- Did AI help you design or understand any tests? How?
I decided a bug was fixed only after I tested it in the live Streamlit app and checked that the behavior matched what I expected. For example, after changing the check_guess function, I reran the app and tried guesses that were too high and too low to confirm the game gave the correct hints. I also ran pytest to make sure the logic worked outside of the Streamlit interface. The tests used assertions to check that guesses above the secret returned “Too High,” guesses below the secret returned “Too Low,” and correct guesses returned “Win.”

AI helped me design the unit tests by showing me how to test the check_guess function with simple inputs and expected outputs. This helped me understand that a good test does not need to be complicated. It just needs to clearly prove whether one specific piece of logic works correctly.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would explain it to a friend like this: Streamlit keeps refreshing the page from top to bottom, but st.session_state is like the app's memory. Without session state, the game would forget the secret number and score every time the user made a guess. For this project, I learned that properly resetting session state is important because the restart button needs to clear old values and start a truly new game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  : 1) I would want to carry on by asking about every change made by the AI assistant instead of just accepting all the changes made by it,
    2) I would also like to take away creation of tests and constructing clearier guidlines while using AI to fix or generate code
    3) I also took away the importance for AI to explain all generated code for me to specially understand what the changes were made by it as when I push the AI code I technically am responsible for it
- What is one thing you would do differently next time you work with AI on a coding task?
- I looked around and found this github repository called grill me which seems to tell the AI to interview me heavily on the project we are going to build so that there is less ambiguity in our project this is something I would like to implement every time I work on any coding project from now.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
- This project made me realize how dump AI can be at some times, it does overlook small details that needs to be taken care of by a use manually.
