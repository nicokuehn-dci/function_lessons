# Explanation of Factorial Methods in Python

This document explains the different methods used in the `factorial_examples.py` file to calculate the factorial of a number. The script demonstrates three distinct approaches: iterative, recursive, and using the built-in `math.factorial` function.

## 1. Iterative Factorial

This method calculates the factorial of a number using an iterative approach. It initializes a variable `result` to 1 and iterates from 1 to `n` (inclusive), multiplying the current value of `result` by the loop variable `i` at each step. The final value of `result` is the factorial of the number.

### When to Use:
- When you prefer a straightforward and explicit approach.
- For scenarios where recursion might lead to stack overflow (e.g., very large `n`).

```python
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

## 2. Recursive Factorial

This method calculates the factorial of a number using recursion. It defines a base case where the factorial of 0 or 1 is 1. For other values of `n`, it returns `n` multiplied by the factorial of `n-1`.

### When to Use:
- When you want a concise and elegant solution.
- For educational purposes to demonstrate recursion.

### Note:
- Be cautious with large values of `n`, as recursion depth is limited in Python.

```python
def factorial_recursive(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial_recursive(n - 1)
```

## 3. Using `math.factorial`

This method uses the built-in `factorial` function from Python's `math` module. It is the simplest and most efficient way to calculate the factorial of a number, as it is implemented in C and optimized for performance.

### When to Use:
- When you need a quick and reliable solution.
- For production code where performance is critical.

```python
import math

def factorial_math(n):
    return math.factorial(n)
```

## Summary

Each of these methods has its own strengths and is suited for specific scenarios. For general-purpose use, the `math.factorial` function is recommended due to its simplicity and efficiency. However, the iterative and recursive methods are valuable for understanding the underlying concepts and for educational purposes.