# Problem 006 – Multiplication Table

## 📌 Problem

Write a Python program that accepts an integer `N` and prints its multiplication table from `1` to `10`.

## 💡 Approach

1. Read an integer from the user.
2. Use a `for` loop to iterate through the numbers `1` to `10`.
3. Multiply the input number by the current loop value.
4. Print each multiplication result in a formatted table.

## 🧠 Solution

The program:

* Accepts an integer from the user.
* Uses a `for` loop to generate the multiplication table.
* Displays the product of the input number and each number from `1` to `10`.

## 🧪 Sample Output

### Example 1

```text
Enter a number: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

### Example 2

```text
Enter a number: -3
-3 x 1 = -3
-3 x 2 = -6
-3 x 3 = -9
...
-3 x 10 = -30
```

## ✅ Test Cases

| Input | Expected             |
| ----: | -------------------- |
|     2 | Table of 2           |
|     5 | Table of 5           |
|    10 | Table of 10          |
|    -3 | Table of -3          |
|     0 | All products equal 0 |

## ⏱️ Time Complexity

**O(1)**

The loop always executes exactly 10 times, regardless of the input. Since 10 is a constant, the running time is considered constant.

## 💾 Space Complexity

**O(1)**

The program uses only a fixed number of variables.

## 📚 What I Learned

* How to use a `for` loop to repeat a task a fixed number of times.
* How to generate formatted output using f-strings.
* How loop variables change with each iteration.
* How multiplication tables can be produced efficiently without repeating code.

## 🔍 Possible Improvements

* Iterate directly from `1` to `10` instead of incrementing the loop variable inside the loop body.
* Keep the loop variable unchanged inside the loop for better readability and to follow common Python practices.

## 🚀 Next Goal

Build more confidence with loops by solving counting and pattern-based problems, then move on to nested loops and string manipulation.
