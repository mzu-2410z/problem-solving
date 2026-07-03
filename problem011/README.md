# Problem 011 – Number Triangle

## 📌 Problem

Write a Python program that accepts a positive integer `N` and prints a right-angled triangle using consecutive numbers.

**Example (N = 5):**

```text
1
12
123
1234
12345
```

**Constraint:** Use nested `for` loops. Do not convert numbers to strings.

---

## 💡 Approach

1. Read a positive integer `N` from the user.
2. Use an outer `for` loop to control the number of rows.
3. For each row, use an inner `for` loop to print the numbers from `1` up to the current row number.
4. Print all numbers on the same line using `end=""`.
5. Move to the next line after each row.

---

## 🧠 Solution

The program:

* Accepts a positive integer as input.
* Uses nested `for` loops.
* Prints consecutive numbers from `1` to the current row number.
* Produces a right-angled number triangle.

---

## 🧪 Sample Output

### Example 1

```text
Enter a number: 5
1
12
123
1234
12345
```

### Example 2

```text
Enter a number: 3
1
12
123
```

---

## ✅ Test Cases

| Input | Expected Output                       |
| ----: | ------------------------------------- |
|     1 | `1`                                   |
|     2 | <pre>1<br>12</pre>                    |
|     4 | <pre>1<br>12<br>123<br>1234</pre>     |
|     6 | Triangle with numbers from `1` to `6` |

---

## ⏱️ Time Complexity

**O(n²)**

The outer loop runs `N` times, and the inner loop prints an increasing number of values on each iteration. The total number of printed values is:

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

* How to reuse the same nested-loop structure for different output patterns.
* The outer loop controls the number of rows.
* The inner loop controls what is printed on each row.
* Changing only the printed value can produce an entirely different pattern.
* Understanding the algorithm is more valuable than memorizing the code.

---

## 🔍 Key Insight

This problem uses the same nested-loop structure as the previous star pattern problems. The only difference is that the inner loop prints the current number instead of an asterisk.

This demonstrates an important programming principle:

> Keep the algorithm the same and change only the behavior when necessary.

---

## 🚀 Next Goal

Continue practicing nested-loop patterns with numbers, letters, and spaces to strengthen the ability to recognize and adapt common programming templates.
