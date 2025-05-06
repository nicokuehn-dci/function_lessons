# Additional Examples of Summing Methods in Python

# Example 1: Using List Comprehension
# This method uses a list comprehension to create a new list of numbers and then sums them.
def sum_with_comprehension(list_of_nums):
    return sum([num for num in list_of_nums])

# Example 2: Using a While Loop
# This method uses a while loop to iterate through the list and calculate the sum.
def sum_with_while_loop(list_of_nums):
    total = 0
    index = 0
    while index < len(list_of_nums):
        total += list_of_nums[index]
        index += 1
    return total

# Example 3: Using Reduce from functools
# This method uses the reduce function to calculate the sum of the list.
from functools import reduce

def sum_with_reduce(list_of_nums):
    return reduce(lambda x, y: x + y, list_of_nums)

# Example 4: Using Numpy for Summation
# This method uses the numpy library to calculate the sum of the list.
import numpy as np

def sum_with_numpy(list_of_nums):
    return np.sum(list_of_nums)

# Example usage
if __name__ == "__main__":
    list_of_nums = [1, 2, 3, 4, 5, 6, 8, 4, 1, 2, 3, 6, 9, 4]
    print("Sum with comprehension:", sum_with_comprehension(list_of_nums))
    print("Sum with while loop:", sum_with_while_loop(list_of_nums))
    print("Sum with reduce:", sum_with_reduce(list_of_nums))
    print("Sum with numpy:", sum_with_numpy(list_of_nums))