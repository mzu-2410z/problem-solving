# Problem 010 – Inverted Right-Angled Star Pattern

## 📌 Problem

Write a Python program that accepts a positive integer `N` and prints an inverted right-angled triangle using asterisks (`*`).

**Example (N = 5):**

```text
*****
****
***
**
*
```

**Constraint:** Use nested `for` loops. Do not use string multiplication (e.g., `"*" * n`).

---

## 💡 Approach

1. Read a positive integer `N` from the user.
2. Use an outer `for` loop to control the number of rows.
3. Start the outer loop at `N` and decrease it until `1`.
4. For each row, use an inner `for` loop to print the required number of stars.
5. After printing each row, move to the next line.

---

## 🧠 Solution

The program:

* Accepts a positive integer as input.
* Uses nested `for` loops.
* Prints one fewer star on each new row.
* Produces an inverted right-angled triangle pattern.

---

## 🧪 Sample Output

### Example 1

```text
Enter a number: 5
*****
****
***
**
*
```

### Example 2

```text
Enter a number: 3
***
**
*
```

---

## ✅ Test Cases

| Input | Expected Output                            |
| ----: | ------------------------------------------ |
|     1 | `*`                                        |
|     3 | <pre>***<br>**<br>*</pre>                  |
|     5 | <pre>*****<br>****<br>***<br>**<br>*</pre> |
|     7 | Inverted triangle with 7 rows              |

---

## ⏱️ Time Complexity

**O(n²)**

The outer loop runs `N` times, and the inner loop prints a decreasing number of stars on each iteration. The total number of stars printed is proportional to:

```text
N + (N - 1) + (N - 2) + ... + 1
```

which results in quadratic time complexity.

---

## 💾 Space Complexity

**O(1)**

The program uses only loop variables and does not allocate additional memory based on the input size.

---

## 📚 What I Learned

* How to modify an existing nested-loop solution instead of writing a new one from scratch.
* How changing the direction of a loop changes the output pattern.
* How the outer loop controls the number of rows, while the inner loop controls the number of stars printed in each row.
* Why understanding the logic behind a solution is more valuable than memorizing the code.

---

## 🔍 Key Insight

Compared to the previous star pattern, the only significant change was the direction of the outer loop. Instead of counting upward from `1` to `N`, it counts downward from `N` to `1`. The inner loop remains almost unchanged.

This demonstrates how small modifications to loop boundaries can produce entirely different output patterns.

---

## 🚀 Next Goal

Continue practicing nested loops with more advanced patterns, including centered pyramids and number-based patterns, before applying the same concepts to two-dimensional data structures.
