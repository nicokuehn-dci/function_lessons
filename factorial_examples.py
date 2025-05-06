# Factorial Examples in Python

# Example 1: Iterative Factorial
# This method calculates the factorial of a number using an iterative approach.
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example 2: Recursive Factorial
# This method calculates the factorial of a number using recursion.
def factorial_recursive(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example 3: Using math.factorial
# This method uses the built-in factorial function from the math module.
import math

def factorial_math(n):
    return math.factorial(n)

# Example usage
if __name__ == "__main__":
    number = 5
    print("Factorial (Iterative):", factorial_iterative(number))
    print("Factorial (Recursive):", factorial_recursive(number))
    print("Factorial (math module):", factorial_math(number))