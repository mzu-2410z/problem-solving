# Problem 009 – Right-Angled Star Pattern

## 📌 Problem

Write a Python program that accepts a positive integer `N` and prints a right-angled triangle pattern using asterisks (`*`).

**Example (N = 5):**

```text
*
**
***
****
*****
```

**Constraint:** Use nested `for` loops. Do not use string multiplication (e.g., `"*" * n`).

---

## 💡 Approach

1. Read a positive integer `N` from the user.
2. Use an outer `for` loop to control the number of rows.
3. For each row, use an inner `for` loop to print the required number of stars.
4. After printing all stars for the current row, move to the next line.
5. Repeat until all rows have been printed.

---

## 🧠 Solution

The program:

* Accepts a positive integer as input.
* Uses nested `for` loops.
* Prints one additional star on each new row.
* Produces a right-angled triangle pattern.

---

## 🧪 Sample Output

### Example 1

```text
Enter a number: 5
*
**
***
****
*****
```

### Example 2

```text
Enter a number: 3
*
**
***
```

---

## ✅ Test Cases

| Input | Expected Output                            |
| ----: | ------------------------------------------ |
|     1 | `*`                                        |
|     2 | <pre>*<br>**</pre>                         |
|     5 | <pre>*<br>**<br>***<br>****<br>*****</pre> |
|     7 | Triangle with 7 rows                       |

---

## ⏱️ Time Complexity

**O(n²)**

The outer loop executes `N` times, and the inner loop prints an increasing number of stars on each iteration. In total, the program prints:

```text
1 + 2 + 3 + ... + N
```

which results in quadratic time complexity.

---

## 💾 Space Complexity

**O(1)**

The program uses only loop variables and does not allocate additional memory based on the input size.

---

## 📚 What I Learned

* How nested `for` loops work.
* How the outer loop controls the rows.
* How the inner loop controls the number of items printed in each row.
* Why `print(end="")` is useful for printing multiple values on the same line.
* How to move to the next line after completing each row.

---

## 🔍 Possible Improvement

Instead of:

```python
print("")
```

Python programmers typically write:

```python
print()
```

Both produce the same output, but `print()` more clearly expresses the intent of printing a newline.

---

## 🚀 Next Goal

Continue practicing nested loops with different patterns, such as inverted triangles, pyramids, and number patterns, before applying the same concept to matrices and two-dimensional data structures.
