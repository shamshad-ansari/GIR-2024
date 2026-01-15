# GIR 2024 Python Projects

This repository contains a collection of Python projects developed as part of the **GIR 2024** program. These projects range from command-line games to utility-based tools and object-oriented simulations.

---

## 📁 Projects Overview

### 1. **BlackJack**

A command-line implementation of the classic card game **Blackjack**.

* Players can **Hit** or **Stay** to get as close to 21 as possible without going over.
* Includes a **dealer AI** that follows standard Blackjack rules (hits until reaching a hand value of at least 17).
* Features automated **game status reporting** and **winner determination**.

---

### 2. **Human Dictionary**

A tool for managing a custom dictionary with support for multiple definitions per word.

* **Add Definitions**: Map words to a list of definitions.
* **Remove Content**: Remove specific definitions or entire words.
* **Lookup**: Efficiently retrieve all definitions associated with a keyword.

---

### 3. **Robot Pirate**

An object-oriented simulation of a pirate robot navigating a 2D grid.

* **Movement & Navigation**: The robot can move forward, turn left, or turn right while staying within grid boundaries.
* **Treasure Mechanics**: Starts with a fixed amount of treasure that can be dropped at specific coordinates and picked up later.
* **Visual Representation**: Implements a `__str__` method to display the grid, robot position, and treasure locations.

---

### 4. **Search Engine**

A metadata-driven search tool designed to process article information.

* **Keyword Search**: Maps keywords to article titles for fast retrieval.
* **Advanced Filtering**: Filter results by author, publication year, or article character length.
* **Metadata Mapping**: Converts raw metadata into optimized dictionary structures for efficient lookups.

---

### 5. **Tic-Tac-Toe**

A classic two-player game played on a **3 × 3** grid.

* **Interactive Gameplay**: Players take turns entering coordinates to place their symbols (`X` or `O`).
* **Win Detection**: Automatically checks for horizontal, vertical, and diagonal wins after each move.
* **Input Validation**: Ensures moves are valid and spaces are unoccupied.

---

### 6. **Wordle**

A Python class-based implementation of the popular word-guessing game **Wordle**.

* **Guess Feedback**:

  * `(g)` – Correct letter in the correct position
  * `(y)` – Correct letter in the wrong position
  * `(r)` – Letter not in the word
* **Game Logic**: Tracks remaining guesses and maintains a global win/loss record.
* **Validation**: Restricts guesses to unique 5-letter words.

---

## ▶️ How to Run

Each project is self-contained. You can run the main script for any project using Python:

```bash
python <folder_name>/main.py
```

**Note:**

* For **BlackJack**, run `blackjack.py`
* For **Search Engine**, run `search.py`

---

Happy coding 🚀
