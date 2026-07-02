# Problem 008 – Find the Largest Number

## 📌 Problem

Write a Python program that asks the user how many numbers they want to enter and determines the largest number.

**Constraints:**

* Do **not** use Python's built-in `max()` function.
* Do **not** store the numbers in a list.
* Process each number as it is entered.

## 💡 Approach

1. Ask the user how many numbers they want to enter.
2. Read the **first** number and assume it is the largest.
3. Read the remaining numbers one at a time using a loop.
4. Compare each new number with the current largest number.
5. If the new number is larger, update the largest value.
6. After all numbers have been processed, print the largest number.

## 🧠 Solution

The program:

* Accepts the total number of inputs from the user.
* Reads the first number separately to initialize the largest value.
* Uses a `for` loop to process the remaining numbers.
* Updates the largest value whenever a larger number is found.
* Prints the largest number after all inputs have been processed.

## 🧪 Sample Output

### Example 1

```text
How many numbers? 5

Enter number 1: 12
Enter number 2: 8
Enter number 3: 25
Enter number 4: 3
Enter number 5: 19

The largest number is 25
```

### Example 2

```text
How many numbers? 4

Enter number 1: -5
Enter number 2: -2
Enter number 3: -9
Enter number 4: -1

The largest number is -1
```

## ✅ Test Cases

| Inputs         | Expected Largest |
| -------------- | ---------------: |
| 5, 2, 9, 1, 7  |                9 |
| -5, -2, -9, -1 |               -1 |
| 10, 10, 10     |               10 |
| 42             |               42 |
| 100, 50, 100   |              100 |

## ⏱️ Time Complexity

**O(n)**

Each number is read and compared exactly once.

## 💾 Space Complexity

**O(1)**

The program stores only the current input number and the current largest value, regardless of how many numbers are entered.

## 📚 What I Learned

* How to solve a problem without storing all the input values.
* How to use the **best-so-far** pattern to track the largest value.
* Why initializing the largest value with the first input avoids errors with negative numbers.
* How to process data as it arrives instead of collecting it first.

## 🔍 Possible Improvement

The `else: continue` statement is unnecessary because a `for` loop automatically moves to the next iteration. The code can be simplified by keeping only the `if` statement that updates the largest value.

## 🚀 Next Goal

Apply the **best-so-far** pattern to similar problems, such as finding the smallest number, the longest word, or the highest score, before moving on to more advanced loop and data structure challenges.
