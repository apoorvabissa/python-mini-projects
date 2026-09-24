# 🎮 Snake, Water & Gun

A simple command-line game built with Python where the player competes against the computer in the classic **Snake, Water & Gun** game.

This project was created while learning Python fundamentals through the **CodeWithHarry Python course**.

## 📌 About the Game

The player chooses one of three options:

* 🐍 Snake
* 💧 Water
* 🔫 Gun

The computer randomly selects an option, and the winner is determined according to these rules:

| Choice   | Beats    |
| -------- | -------- |
| 🐍 Snake | 💧 Water |
| 💧 Water | 🔫 Gun   |
| 🔫 Gun   | 🐍 Snake |

If both the player and computer choose the same option, the game ends in a draw.

## ✨ Features

* Player vs Computer gameplay
* Random computer choice generation
* Win, lose, and draw detection
* Simple command-line interface
* Beginner-friendly Python implementation

## 🛠️ Technologies Used

* **Python 3**
* `random` module

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/snake-water-gun.git
```

### 2. Navigate to the project directory

```bash
cd snake-water-gun
```

### 3. Run the program

```bash
python main.py
```

## 🎯 Example

```text
Enter Snake, Water or Gun: Snake

Computer chose: Gun

You Lose!
```

## 📚 Concepts Practiced

This project helped me practice:

* Variables
* Data types
* Conditional statements (`if`, `elif`, `else`)
* User input
* Dictionaries
* Random number generation
* Basic game logic
* Comparison operators

## 🚀 Future Improvements

Possible improvements for a future version:

* Add multiple rounds
* Keep track of the score
* Add input validation
* Make the game case-insensitive
* Add a replay option
* Improve the command-line interface

## 👨‍💻 Author

**Apoorva Bissa**

* GitHub: [@apoorvabissa](https://github.com/apoorvabissa)
* LinkedIn: [Apoorva Bissa](https://www.linkedin.com/in/apoorvabissa/)

---

⭐ created while learning Python through the CodeWithHarry Python course
