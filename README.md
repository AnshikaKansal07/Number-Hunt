# Number Hunt 
A terminal-based number guessing game with higher/lower hints.

---

## 1. Description
- Language: Python
- Input: Upper limit, guesses
- Output: Higher/Lower hints + attempt count
- Validation: Rejects limit ≤ 0

---

## 2. How It Works
1. Set an upper limit (must be > 0)
2. Computer picks a random number in that range
3. Guess the number — get Higher or Lower hints
4. Keep guessing until correct
5. See how many attempts it took

---

## 3. Input / Output
| Scenario | Input | Output |
|---|---|---|
| Too low | 30 (ans=75) | "Wrong number. Guess higher" |
| Too high | 90 (ans=75) | "Wrong number. Guess lower" |
| Correct | 75 (ans=75) | "Correct number is 75 that you guessed in X chances." |
| Invalid limit | -5 or 0 | "Please choose a number greater than 0" |

---

## 4. Screenshot
<img width="765" height="311" alt="Image" src="https://github.com/user-attachments/assets/80024c44-946e-41d5-954e-cb1d9edb4070" />

---
