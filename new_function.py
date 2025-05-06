list_of_nums = [1, 2, 3, 4, 5, 6, 8, 4, 1, 2, 3, 6, 9, 4]
def get_sum_1(list):
    sum = 0
    for item in list:
        sum += item
    return sum
def get_sum_2(list):
    return sum(list)
#we can use recursion
def recursive_sum(lst):
    """
    Recursively calculates the sum of a list of numbers.
    :param lst: List of numbers
        :return: Sum of the numbers in the list
    """
        if len(lst) == 0:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])

def get_sum_3(list):
    return recursive_sum(list)
#we can use recursion
print(recursive_sum(list_of_nums))