# Problem 002 – Positive, Negative, or Zero

## 📌 Problem

Write a Python program that accepts an integer from the user and determines whether the number is **positive**, **negative**, or **zero**.

## 💡 Approach

1. Read an integer from the user.
2. Check if the number is equal to `0`.
3. If not, check whether it is greater than `0`.
4. If neither condition is true, the number must be less than `0`.
5. Print the appropriate result.

## 🧠 Solution

The program:

* Accepts an integer from the user.
* Uses `if`, `elif`, and `else` statements to determine the sign of the number.
* Prints whether the number is positive, negative, or zero.

## 🧪 Sample Output

### Example 1

```text
Enter a number: 15
15 is positive.
```

### Example 2

```text
Enter a number: -8
-8 is negative.
```

### Example 3

```text
Enter a number: 0
0 is zero.
```

## ✅ Test Cases

| Input | Expected Output  |
| ----: | ---------------- |
|    25 | 25 is positive.  |
|   -10 | -10 is negative. |
|     0 | 0 is zero.       |
|   999 | 999 is positive. |
|    -1 | -1 is negative.  |

## ⏱️ Time Complexity

**O(1)**

The program performs a fixed number of comparisons regardless of the input value.

## 💾 Space Complexity

**O(1)**

Only one variable is used to store the user's input.

## 📚 What I Learned

* How to use multiple conditional statements with `if`, `elif`, and `else`.
* Why the order of conditions matters.
* Every integer falls into exactly one of three categories:

  * Positive
  * Negative
  * Zero
* How to think about mutually exclusive conditions when solving problems.

## 🔍 Possible Improvement

Since the input is already converted to an integer, the final `else` statement is unnecessary. After checking for `0` and values greater than `0`, any remaining integer must be negative.

## 🚀 Next Goal

Move on to **Problem 003**, where I'll continue strengthening my understanding of conditional logic and begin applying it to slightly more realistic problems.
