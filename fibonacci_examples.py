# Fibonacci Examples in Python

# Example 1: Iterative Fibonacci
# This method calculates the Fibonacci sequence up to the nth term using an iterative approach.
def fibonacci_iterative(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example 2: Recursive Fibonacci
# This method calculates the nth Fibonacci number using recursion.
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example 3: Using Dynamic Programming
# This method calculates the Fibonacci sequence up to the nth term using dynamic programming.
def fibonacci_dynamic(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

# Example usage
if __name__ == "__main__":
    number = 10
    print("Fibonacci (Iterative):", fibonacci_iterative(number))
    print("Fibonacci (Recursive nth term):", [fibonacci_recursive(i) for i in range(number)])
    print("Fibonacci (Dynamic Programming):", fibonacci_dynamic(number))