# Part 01 — Python Foundations
These are original exercises that complement an introductory text such as *Python Crash Course*.

## 1. How Python executes a program
Python evaluates expressions and executes statements in order, except when control flow changes the path. Indentation defines blocks. Use four spaces. Names refer to objects; `=` binds a name to a value, while `==` compares values.

```python
name = "Greydev"
years_learning = 1
print(f"{name} has practised for {years_learning} year(s).")
```
An f-string inserts an expression into a string. `input()` always returns text, so convert and validate before arithmetic.

## 2. Core types
- `int`: whole numbers, e.g. `4`
- `float`: approximate decimal numbers, e.g. `3.5`
- `str`: text, e.g. `"Python"`
- `bool`: `True` or `False`
- `None`: intentional absence of a value

Use `type(value)` while learning, but don't build code around repeated type checks when clear design is possible.

## 3. Operators and comparisons
Arithmetic: `+ - * / // % **`. Comparisons: `== != < <= > >=`. Boolean operators: `and`, `or`, `not`. Remember precedence; use parentheses when they make intent clearer. `=` assigns, `==` compares.

## 4. Branching
```python
score = 82
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "Keep practising"
```
Conditions should express business rules clearly. Test boundary values such as 69, 70, 79, 80.

## 5. Loops
Use `for` to iterate over a sequence or range. Use `while` when repeating until a condition changes. Every `while` loop needs a clear route to termination. `break` exits a loop; `continue` skips to the next iteration.

## 6. Strings
Strings are immutable sequences. Useful methods include `.strip()`, `.lower()`, `.upper()`, `.replace()`, `.split()`, and `"separator".join(items)`. Indexing starts at zero; negative indexes count from the end. Slices exclude the ending index.

## 7. Input validation
Convert user input inside a `try` block when conversion can fail:
```python
try:
    age = int(input("Age: "))
except ValueError:
    print("Enter a whole number.")
else:
    if age < 0:
        print("Age cannot be negative.")
    else:
        print(f"Age recorded: {age}")
```
Do not silently turn invalid data into fake values.

## Exercises — do not look at solutions first
### Batch 1: Values and expressions
1. Ask for a person's name and preferred programming language; print a personalised sentence.
2. Ask for two numbers and print their sum, difference, product, and quotient. Handle a zero divisor.
3. Convert minutes into hours and remaining minutes.
4. Given a price and percentage discount, calculate the final price. Reject negative prices and discounts outside 0–100.

### Batch 2: Decisions
5. Ask for a score from 0–100 and map it to grades you define. Reject out-of-range scores.
6. Determine whether a year is a leap year. Explain the divisible-by-4, century, and divisible-by-400 rules.
7. Build a simple shipping calculator using order total and a free-shipping threshold.

### Batch 3: Loops and strings
8. Print a multiplication table for a number from 1 to 12.
9. Count vowels in a sentence, ignoring case.
10. Repeatedly ask for a positive integer until valid input is entered.
11. Build a number guessing game with a fixed secret number and a maximum of six attempts.
12. Print a right-angled triangle of `*` characters with a user-selected height.

### Boss challenge: CLI expense tracker
Ask the user to enter expenses until they type `done`. Each expense has a description and a positive amount. Print the total, number of expenses, and average. Handle malformed amounts and an empty list. Keep the program readable; functions are introduced in Part 03, so a first version can be procedural.
