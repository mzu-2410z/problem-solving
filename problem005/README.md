# Problem 005 – Sum of the First N Natural Numbers

## 📌 Problem

Write a Python program that accepts a positive integer `N` and calculates the sum of all natural numbers from `1` to `N` using a loop.

**Do not** use the mathematical formula. The goal is to practice loops and accumulators.

## 💡 Approach

1. Read a positive integer from the user.
2. Check whether the input is greater than zero.
3. Initialize a variable to store the running total.
4. Iterate from `1` to `N`.
5. Add each number to the running total.
6. Print the final sum.

## 🧠 Solution

The program:

* Accepts an integer from the user.
* Validates that the number is positive.
* Uses a `for` loop to add each number from `1` to `N`.
* Displays the total sum.

## 🧪 Sample Output

### Example 1

```text id="dhpv8y"
Enter a number: 5
The sum of first 5 numbers is 15.
```

### Example 2

```text id="w9n72l"
Enter a number: 10
The sum of first 10 numbers is 55.
```

### Example 3

```text id="ry7jlwm"
Enter a number: -3
Please enter a valid number!
```

## ✅ Test Cases

| Input | Expected Output                       |
| ----: | ------------------------------------- |
|     1 | The sum of first 1 numbers is 1.      |
|     5 | The sum of first 5 numbers is 15.     |
|    10 | The sum of first 10 numbers is 55.    |
|   100 | The sum of first 100 numbers is 5050. |
|    -5 | Please enter a valid number!          |
|     0 | Please enter a valid number!          |

## ⏱️ Time Complexity

**O(n)**

The program loops once for each number from `1` to `N`.

## 💾 Space Complexity

**O(1)**

Only a few variables are used regardless of the input size.

## 📚 What I Learned

* How to use a `for` loop in Python.
* How to use an accumulator variable to build a running total.
* Why input validation is important.
* How to analyze the time and space complexity of a loop-based solution.

## 🔍 Possible Improvements

* Use a more descriptive variable name such as `total` instead of `sum` to avoid shadowing Python's built-in `sum()` function.
* Iterate directly from `1` to `N` instead of modifying the loop variable inside the loop body. This makes the code simpler and easier to read.

## 🚀 Next Goal

Continue practicing loops by solving problems involving counting, multiplication tables, and number patterns before moving on to nested loops and strings.
