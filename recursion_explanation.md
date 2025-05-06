# Recursion Lesson Explanation

Recursion is a programming technique where a function calls itself to solve smaller instances of a problem. It is commonly used for problems that can be broken down into smaller, similar subproblems.

## Key Concepts

1. **Base Case**: The condition under which the recursion stops. Without a base case, the recursion would continue indefinitely, leading to a stack overflow.
2. **Recursive Case**: The part of the function where it calls itself to solve a smaller problem.

## Example: Factorial Calculation

The factorial of a number `n` is the product of all positive integers less than or equal to `n`. It can be calculated using recursion as follows:

```python
# Recursive function to calculate factorial
def factorial_recursive(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial_recursive(n - 1)  # Recursive case
```

## Example: Fibonacci Sequence

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. It can also be implemented using recursion:

```python
# Recursive function to calculate Fibonacci numbers
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
```

## Advantages of Recursion

- Simplifies code for problems that have a natural recursive structure, such as tree traversal and divide-and-conquer algorithms.
- Makes the code more readable and easier to understand for certain problems.

## Disadvantages of Recursion

- Can lead to high memory usage due to the function call stack.
- May be less efficient than iterative solutions for some problems.

## When to Use Recursion

- When the problem can be divided into smaller subproblems of the same type.
- When an iterative solution would be more complex or less intuitive.

## Practice Problems

1. Write a recursive function to calculate the sum of all elements in a list.
2. Implement a recursive function to reverse a string.
3. Create a recursive function to find the greatest common divisor (GCD) of two numbers.