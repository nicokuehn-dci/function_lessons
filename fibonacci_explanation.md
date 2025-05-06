# Explanation of Fibonacci Methods in Python

This document explains the different methods used in the `fibonacci_examples.py` file to calculate the Fibonacci sequence. The script demonstrates three distinct approaches: iterative, recursive, and dynamic programming.

## 1. Iterative Fibonacci

This method calculates the Fibonacci sequence up to the nth term using an iterative approach. It initializes two variables, `a` and `b`, to represent the first two terms of the sequence. A loop is used to calculate subsequent terms by updating these variables and appending the current term to the sequence.

### When to Use:
- When you need an efficient and straightforward solution.
- For generating the entire sequence up to a specific term.

```python
def fibonacci_iterative(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
```

## 2. Recursive Fibonacci

This method calculates the nth Fibonacci number using recursion. It defines base cases for `n = 0` and `n = 1`. For other values of `n`, it returns the sum of the Fibonacci numbers for `n-1` and `n-2`.

### When to Use:
- For educational purposes to demonstrate recursion.
- When calculating individual terms rather than the entire sequence.

### Note:
- Be cautious with large values of `n`, as recursion depth is limited in Python and this method has exponential time complexity.

```python
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
```

## 3. Using Dynamic Programming

This method calculates the Fibonacci sequence up to the nth term using dynamic programming. It stores previously calculated terms in a list to avoid redundant calculations, making it more efficient than the recursive approach.

### When to Use:
- When you need an efficient solution for generating the entire sequence.
- For scenarios where performance is critical.

```python
def fibonacci_dynamic(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence
```

## Summary

Each of these methods has its own strengths and is suited for specific scenarios. For general-purpose use, the iterative and dynamic programming methods are recommended due to their efficiency. The recursive method is valuable for understanding the concept of recursion and for educational purposes.