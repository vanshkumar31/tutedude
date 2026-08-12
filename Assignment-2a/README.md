# Assignment 2 — Menu-Driven Calculator

## Overview

This assignment implements a menu-driven calculator in Python. It uses separate functions for addition, subtraction, multiplication, and division, repeats until the user exits, and handles division by zero.

## Requirements Covered

- Menu-driven calculator
- Four separate mathematical functions
- Repeated execution using a loop
- `if-elif-else` operation selection
- Division-by-zero handling
- Variables for user inputs and results
- Comments explaining the implementation
- Demonstration of all four operations
- Division-by-zero demonstration
- Word documentation with screenshots

## Functions

- `add(x, y)` — adds two numbers.
- `subtract(x, y)` — subtracts the second number from the first.
- `multiply(x, y)` — multiplies two numbers.
- `divide(x, y)` — checks for a zero divisor before dividing.

## Program Flow

```text
Start
  |
  v
Display Menu
  |
  v
Get User Choice
  |
  +-- 1 --> Addition
  +-- 2 --> Subtraction
  +-- 3 --> Multiplication
  +-- 4 --> Division --> divisor 0 --> Error Message
  +-- 5 --> Exit
  |
  v
Repeat Menu
```

## Code Explanation

The `while True` loop keeps the calculator running until option `5` is selected.

The program uses `if-elif-else` statements to select the requested operation and stores the two user inputs in `num1` and `num2`. The returned value is stored in `result`.

The `divide()` function checks whether the divisor is zero before performing the division:

```python
if y == 0:
    return "Error: Cannot divide by zero."
```

## Example Output

### Addition

```text
Enter your choice: 1
Enter first number: 20
Enter second number: 10
Result: 30.0
```
![Addition](screenshots/01-addition.png)
### Subtraction

```text
Enter your choice: 2
Enter first number: 20
Enter second number: 10
Result: 10.0
```

![Subtraction](screenshots/02-subtraction.png)

### Multiplication

```text
Enter your choice: 3
Enter first number: 20
Enter second number: 10
Result: 200.0
```
![Multiplication](screenshots/03-multiplication.png)
### Division

```text
Enter your choice: 4
Enter first number: 20
Enter second number: 10
Result: 2.0
```


![Division](screenshots/04-division.png)


### Division by Zero

```text
Enter your choice: 4
Enter first number: 20
Enter second number: 0
Result: Error: Cannot divide by zero.
```
![Division by Zero](screenshots/05-division-by-zero.png)

>## Note About Assignment Requirements

The attached Assignment 2 brief may differ from the requirements communicated by the mentor. This repository follows the mentor's specified requirements.
