# Problem 003 – Largest of Three Numbers

## 📌 Problem

Write a Python program that accepts three integers from the user and determines the largest number **without using Python's built-in `max()` function**.

## 💡 Approach

1. Read three integers from the user.
2. Compare the first number with the second and third numbers.
3. If the first number is the largest, print it.
4. Otherwise, compare the second number with the first and third numbers.
5. If the second number is the largest, print it.
6. If neither of the above conditions is true, print the third number as the largest.

## 🧠 Solution

The program:

* Accepts three integer inputs.
* Uses `if`, `elif`, and `else` statements to compare the numbers.
* Prints the largest value without relying on built-in helper functions.

## 🧪 Sample Output

### Example 1

```text
Enter first number: 5
Enter second number: 9
Enter third number: 2

9 is the largest number.
```

### Example 2

```text
Enter first number: -5
Enter second number: -9
Enter third number: -1

-1 is the largest number.
```

## ✅ Test Cases

| Number 1 | Number 2 | Number 3 | Expected Output           |
| -------: | -------: | -------: | ------------------------- |
|        5 |        9 |        2 | 9 is the largest number.  |
|        2 |        1 |        5 | 5 is the largest number.  |
|       -5 |       -9 |       -1 | -1 is the largest number. |

## ⏱️ Time Complexity

**O(1)**

The program performs a fixed number of comparisons, so the running time does not depend on the input size.

## 💾 Space Complexity

**O(1)**

The program stores only three integer variables.

## 📚 What I Learned

* How to compare multiple values using conditional statements.
* How to combine conditions using the `and` operator.
* Why solving a problem without built-in functions strengthens logical thinking.
* The importance of testing edge cases, especially when duplicate values are involved.

## ⚠️ Known Limitation

This implementation does **not** correctly handle cases where two or more numbers share the maximum value (for example, `10, 10, 3` or `100, 50, 100`). Improving the comparison logic to handle equal values is the next step.

## 🚀 Next Goal

Refine this solution so it correctly handles duplicate maximum values, then move on to more complex conditional problems.
