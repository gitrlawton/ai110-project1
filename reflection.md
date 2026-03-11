# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - The hints were backwards -> If you guess "1", it tells you to go lower, and if you guess "100", it tells you to go higher
  - Guessing outside the bounds is still accepted -> uses a guess and adds number to history
  - When I click "new Game", the attempts and secret number correctly reset, but I can't guess any new numbers (it doesn't register my attempts)

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - Claude suggested to swap the "Go HIGHER!" / "Go LOWER!" strings
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - Claude didn't give any suggestions that were misleading

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I re-ran the streamlit app and tested the same actions again, this time receiving the expected results
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - I input numbers -1, 0, and 1, along with 99, 100, and 101 as guesses and received the expected output for each
- Did AI help you design or understand any tests? How?
  - Yes, it helped design my tests for me, and helped me understand the structure and keywords

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
