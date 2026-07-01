# Problem 001 – Even or Odd

## 📌 Problem

Write a Python program that accepts an integer from the user and determines whether it is **even** or **odd**.

## 💡 Approach

1. Read an integer from the user.
2. Use the modulus (`%`) operator to find the remainder when the number is divided by `2`.
3. If the remainder is `0`, the number is **even**.
4. Otherwise, the number is **odd**.
5. Display the result.

## 🧠 Solution

The program:

* Accepts an integer as input.
* Checks whether `number % 2 == 0`.
* Prints whether the number is even or odd.

## 🧪 Sample Output

### Example 1

```text
Enter your number: 8
8 is even
```

### Example 2

```text
Enter your number: 13
13 is odd
```

## ✅ Test Cases

| Input | Expected Output |
| ----: | --------------- |
|     2 | 2 is even       |
|     7 | 7 is odd        |
|     0 | 0 is even       |
|    -8 | -8 is even      |
|    -5 | -5 is odd       |

## ⏱️ Time Complexity

**O(1)**

The program performs a constant number of operations regardless of the input.

## 💾 Space Complexity

**O(1)**

Only one variable is used to store the input.

## 📚 What I Learned

* How to take integer input in Python.
* How to use the modulus (`%`) operator.
* How to write a basic `if-else` condition.
* The importance of testing positive numbers, negative numbers, and zero.
* How to analyze the time and space complexity of a simple program.

## 🚀 Next Goal

Move on to **Problem 002**, where I'll continue practicing basic problem-solving and learn how to think through problems before writing code.
