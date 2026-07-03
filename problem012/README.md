# Problem 012 – Right-Aligned Star Triangle

## 📌 Problem

Write a Python program that accepts a positive integer `N` and prints a right-aligned triangle using asterisks (`*`).

**Example (N = 5):**

```text id="xjz40k"
    *
   **
  ***
 ****
*****
```

**Constraint:** Use nested `for` loops. Do not use string multiplication (e.g., `" " * n` or `"*" * n`).

---

## 💡 Approach

1. Read a positive integer `N` from the user.
2. Use an outer `for` loop to iterate through each row.
3. For every row:

   * Print the required number of leading spaces.
   * Print the required number of stars.
4. Move to the next line after completing each row.

---

## 🧠 Solution

The program:

* Accepts a positive integer as input.
* Uses one outer loop to control the rows.
* Uses one inner loop to print leading spaces.
* Uses another inner loop to print stars.
* Produces a right-aligned triangle.

---

## 🧪 Sample Output

### Example 1

```text id="l0k4ws"
Enter a number: 5
    *
   **
  ***
 ****
*****
```

### Example 2

```text id="5zc0zr"
Enter a number: 3
  *
 **
***
```

---

## ✅ Test Cases

| Input | Expected Output                         |
| ----: | --------------------------------------- |
|     1 | `*`                                     |
|     2 | <pre> *<br>**</pre>                     |
|     4 | <pre>   *<br>  **<br> ***<br>****</pre> |
|     6 | Right-aligned triangle with 6 rows      |

---

## ⏱️ Time Complexity

**O(n²)**

The outer loop executes `N` times. For each row, the program prints both spaces and stars, resulting in approximately `N` operations per row.

---

## 💾 Space Complexity

**O(1)**

Only loop variables are used. No additional memory proportional to the input size is allocated.

---

## 📚 What I Learned

* How to combine multiple nested loops within a single outer loop.
* How to divide a problem into smaller parts instead of solving it all at once.
* How to print leading spaces to control alignment.
* How to use expressions like `N - current_row` to determine how many times an operation should be performed.
* Why decomposing a problem into sections leads to cleaner and easier-to-understand code.

---

## 🔍 Pattern Used

**Nested Loops + Output Composition**

Each row is composed of two independent sections:

1. Leading spaces
2. Stars

By solving each section separately, the overall pattern becomes much easier to implement.

---

## 🚀 Next Goal

Continue practicing nested-loop problems by combining spaces, numbers, and symbols. The objective is to become comfortable decomposing complex output into simple, repeatable steps before moving on to two-dimensional data structures and matrices.
