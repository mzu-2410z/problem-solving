# Problem 007 – Count Even and Odd Numbers

## 📌 Problem

Write a Python program that accepts a positive integer `N` and counts how many even and odd numbers exist between `1` and `N`.

## 💡 Approach

1. Read a positive integer from the user.
2. Create two counter variables:

   * One for even numbers.
   * One for odd numbers.
3. Iterate through the numbers from `1` to `N`.
4. Check whether each number is even or odd using the modulus (`%`) operator.
5. Increment the appropriate counter.
6. Print the final counts.

## 🧠 Solution

The program:

* Accepts an integer from the user.
* Uses a single `for` loop to examine each number.
* Counts even and odd numbers separately.
* Displays both totals at the end.

## 🧪 Sample Output

### Example 1

```text
Enter a number: 10
Even numbers from 1 to 10 are 5.
Odd numbers from 1 to 10 are 5.
```

### Example 2

```text
Enter a number: 7
Even numbers from 1 to 7 are 3.
Odd numbers from 1 to 7 are 4.
```

## ✅ Test Cases

| Input | Even Count | Odd Count |
| ----: | ---------: | --------: |
|     1 |          0 |         1 |
|     2 |          1 |         1 |
|     5 |          2 |         3 |
|    10 |          5 |         5 |
|    15 |          7 |         8 |

## ⏱️ Time Complexity

**O(n)**

The program examines each number from `1` to `N` exactly once.

## 💾 Space Complexity

**O(1)**

Only two counter variables are maintained regardless of the input size.

## 📚 What I Learned

* How to use multiple counters inside a loop.
* How to classify numbers as even or odd.
* The difference between an accumulator and a counter.
* How to update different variables based on a condition.

## 🔍 Possible Improvement

The loop should include the value `N`. Using `range(1, n)` excludes the final number because the upper limit of `range()` is not included. To count numbers from `1` through `N`, the loop should iterate over the full required range.

This is an example of an **off-by-one error**, one of the most common mistakes when working with loops.

## 🚀 Next Goal

Continue practicing loop-based problems by combining counting with conditions and learning to avoid common boundary errors.
