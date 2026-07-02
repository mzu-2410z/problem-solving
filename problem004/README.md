# Problem 004 – Leap Year Checker

## 📌 Problem

Write a Python program that determines whether a given year is a **leap year**.

A year is considered a leap year if:

* It is divisible by **400**, or
* It is divisible by **4** but **not** divisible by **100**.

Otherwise, it is **not** a leap year.

## 💡 Approach

1. Read a year from the user.
2. Check if the year is divisible by `400`.
3. If not, check whether it is divisible by `4` but not by `100`.
4. If either condition is true, the year is a leap year.
5. Otherwise, it is not a leap year.

## 🧠 Solution

The program:

* Accepts a year as input.
* Uses a compound conditional statement with `and` and `or`.
* Prints whether the year is a leap year or not.

## 🧪 Sample Output

### Example 1

```text id="1knh6r"
Enter a year: 2024
This is a leap year!
```

### Example 2

```text id="nmld18"
Enter a year: 1900
This is not a leap year.
```

### Example 3

```text id="yjlwmw"
Enter a year: 2000
This is a leap year!
```

## ✅ Test Cases

| Input | Expected Output          |
| ----: | ------------------------ |
|  2000 | This is a leap year!     |
|  1900 | This is not a leap year. |
|  2024 | This is a leap year!     |
|  2023 | This is not a leap year. |
|  2400 | This is a leap year!     |
|  2100 | This is not a leap year. |

## ⏱️ Time Complexity

**O(1)**

The program performs a fixed number of arithmetic and comparison operations regardless of the input.

## 💾 Space Complexity

**O(1)**

Only one variable is used to store the input year.

## 📚 What I Learned

* How to combine multiple conditions using `and` and `or`.
* How to translate real-world rules into program logic.
* Why operator precedence matters in conditional expressions.
* The importance of testing special cases such as century years (`1900`, `2000`).

## 🔍 Possible Improvement

Although the condition is correct, adding parentheses improves readability:

```python
(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
```

This makes the evaluation order clear to anyone reading the code.

## 🚀 Next Goal

Continue practicing compound conditions before moving on to loops and more complex problem-solving patterns.
