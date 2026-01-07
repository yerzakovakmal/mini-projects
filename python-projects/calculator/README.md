# 🧮 Python CLI Calculator

A simple **command-line calculator** written in Python.  
This project demonstrates basic Python concepts such as functions, loops, conditionals, error handling, and the use of a `main()` function for clean program structure.

---

## 📌 Features

- Interactive command-line menu
- Supports basic mathematical operations:
  - Addition
  - Subtraction
  - Division (with zero-division handling)
  - Multiplication
  - Exponentiation (power)
- Input validation for menu selection
- Clean and modular code structure
- Uses `main()` and `if __name__ == "__main__"` best practice

---

## 🧠 Program Logic

1. The program starts by displaying a menu with available operations.
2. The user selects an option (1–6).
3. Depending on the selected operation:
   - The program asks for two numbers
   - Performs the chosen calculation
   - Displays the result
4. The program continues running until the user selects **Exit (6)**.

Core logic is handled inside the `main()` function, while each mathematical operation is implemented as a separate function for better readability and reusability.

---

## 🗂 Code Structure

- `menu()` → Displays available operations
- `add(a, b)` → Returns the sum
- `subtract(a, b)` → Returns the difference
- `divide(a, b)` → Performs division with zero-check
- `multiply(a, b)` → Returns the product
- `power(a, b)` → Calculates exponentiation
- `get_numbers()` → Handles numeric input
- `main()` → Controls program flow and user interaction

---

## ▶️ How to Run

### Requirements
- Python **3.10+** (required for `match-case`)

### Steps

1. Clone or download the repository
2. Open a terminal in the project directory
3. Run the program:

```bash
python main.py
```