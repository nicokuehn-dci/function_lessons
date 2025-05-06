# Recursion Examples in Python

# Example 1: Factorial Calculation using Recursion
def factorial_recursive(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial_recursive(n - 1)  # Recursive case

# Example 2: Fibonacci Sequence using Recursion
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example 3: Sum of a List using Recursion
def sum_recursive(lst):
    if len(lst) == 0:  # Base case
        return 0
    else:
        return lst[0] + sum_recursive(lst[1:])  # Recursive case

# Example 4: Reverse a String using Recursion
def reverse_string_recursive(s):
    if len(s) == 0:  # Base case
        return s
    else:
        return s[-1] + reverse_string_recursive(s[:-1])  # Recursive case

# Example 5: Greatest Common Divisor (GCD) using Recursion
def gcd_recursive(a, b):
    if b == 0:  # Base case
        return a
    else:
        return gcd_recursive(b, a % b)  # Recursive case

# Example usage
if __name__ == "__main__":
    print("Factorial of 5:", factorial_recursive(5))
    print("Fibonacci of 6:", fibonacci_recursive(6))
    print("Sum of [1, 2, 3, 4, 5]:", sum_recursive([1, 2, 3, 4, 5]))
    print("Reverse of 'recursion':", reverse_string_recursive("recursion"))
    print("GCD of 48 and 18:", gcd_recursive(48, 18))