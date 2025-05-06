# Coding a Game of Rootexamples

# Importing necessary libraries
import random
import time
import os
import sys
import math
import json
from datetime import datetime
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from new_function import recursive_sum

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    print("Console cleared!")

# Function to display the game rules
def display_rules():
    print("Welcome to the Game of Root!")
    print("In this game, you will provide a number, and the program will calculate its square root.")
    print("Additionally, the program will calculate the sum of numbers up to your input using recursion.")
    print("Press Enter to start the game...")
    input()
    clear_console()
    print("\033[1;34mCoded by Nico Kuehn\033[0m")
    print("Game started!")

# Function to calculate the square root with steps and code explanation
def calculate_square_root_with_steps_and_code(number):
    print("\033[1;34mCalculating the square root of {number}...\033[0m")
    print("\033[1;33mStep 1: Use the math.sqrt function to calculate the square root.\033[0m")
    print("\033[1;32mCode:\033[0m")
    print("    import math")
    print("    sqrt = math.sqrt(number)")
    sqrt = math.sqrt(number)
    print(f"\033[1;36mResult: The square root of {number} is {sqrt:.2f}.\033[0m")
    return sqrt

# Function to calculate the sum using recursion with code explanation and depth restriction
def calculate_sum_with_recursion_and_code(number):
    print(f"\033[1;34mCalculating the sum of numbers from 1 to {number} using recursion...\033[0m")
    print("\033[1;33mCode:\033[0m")
    print("    def recursive_sum(list):")
    print("        if len(list) == 0:")
    print("            return 0")
    print("        else:")
    print("            return list[0] + recursive_sum(list[1:])")

    # Restricting the range to avoid excessive recursion depth
    if number > 1000:
        print("\033[1;31mNumber too large! Please enter a number less than or equal to 1000.\033[0m")
        print("\033[1;33mHint: Try entering a number between 1 and 1000.\033[0m")
        return

    numbers = list(range(1, number + 1))
    total_sum = recursive_sum(numbers)
    print(f"\033[1;36mResult: The sum of numbers from 1 to {number} is {total_sum}.\033[0m")
    return total_sum

# Function to save user data to a JSON file with detailed lesson information
def save_user_data(username, lessons_completed, preferences):
    user_data = {
        "username": username,
        "lessons_completed": lessons_completed,
        "last_session": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "preferences": preferences
    }
    with open("user_data.json", "w") as file:
        json.dump(user_data, file, indent=4)

# Function to load user data from a JSON file
def load_user_data():
    try:
        with open("user_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None

# Function to get or create user data with detailed structure
def get_or_create_user():
    user_data = load_user_data()
    if user_data:
        print(f"Welcome back, {user_data['username']}!")
        print("Lessons completed:")
        for lesson in user_data["lessons_completed"]:
            print(f"- {lesson['lesson_name']} (Completed at: {lesson['completed_at']})")
    else:
        username = input("Enter your name: ")
        preferences = {
            "color_scheme": "dark",
            "difficulty_level": "medium"
        }
        user_data = {
            "username": username,
            "lessons_completed": [],
            "preferences": preferences
        }
        save_user_data(username, user_data["lessons_completed"], preferences)
        print(f"Welcome, {username}! Your progress will be saved.")
    return user_data

# Function to update lessons completed with detailed information
def update_lessons_completed(user_data, lesson_name, steps_completed, score):
    user_data["lessons_completed"].append({
        "lesson_name": lesson_name,
        "completed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "details": {
            "steps_completed": steps_completed,
            "score": score
        }
    })
    save_user_data(user_data["username"], user_data["lessons_completed"], user_data["preferences"])

# Function to display lesson options and get user choice
def choose_lesson():
    print("\033[1;34mChoose a lesson to learn:\033[0m")
    print("1. Factorial")
    print("2. Fibonacci")
    print("3. Authorization")
    print("4. Additional Examples")
    print("5. Functions")
    print("6. New Function")
    print("7. Recursion")
    print("8. Exit")
    while True:
        try:
            choice = int(input("\033[1;35mEnter the number of your choice: \033[0m"))
            if choice in range(1, 9):
                return choice
            else:
                print("\033[1;31mInvalid choice. Please select a number between 1 and 8.\033[0m")
        except ValueError:
            print("\033[1;31mInvalid input. Please enter a number.\033[0m")

# Function to handle lessons step by step
def handle_lessons(selected_lessons):
    for lesson in selected_lessons:
        if lesson == "Factorial":
            factorial_lesson()
        elif lesson == "Fibonacci":
            fibonacci_lesson()
        elif lesson == "Authorization":
            authorization_lesson()
        elif lesson == "Additional Examples":
            additional_examples_lesson()
        elif lesson == "Functions":
            functions_lesson()
        elif lesson == "New Function":
            new_function_lesson()
        elif lesson == "Recursion":
            recursion_lesson()

# Function to make lessons deeper using examples from the root directory
def factorial_lesson():
    print("\033[1;34mWelcome to the Factorial Lesson!\033[0m")
    print("Step 1: What is a Factorial?")
    print("A factorial of a number is the product of all positive integers up to that number.")
    print("For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.")
    input("Press Enter to continue...")

    print("Step 2: Exploring Factorial Examples")
    print("Let's look at some examples from the `factorial_examples.py` file.")
    print("Code:")
    with open("factorial_examples.py", "r") as file:
        print(file.read())
    input("Press Enter to continue...")

    print("Step 3: Explanation of the Code")
    print("The code demonstrates different ways to calculate factorials, including iterative and recursive methods.")
    print("Iterative: Uses a loop to multiply numbers.")
    print("Recursive: Calls the function within itself to calculate the factorial.")
    input("Press Enter to continue...")

    print("Step 4: Try It Yourself")
    print("Now, let's calculate a factorial using the provided examples.")
    while True:
        try:
            number = int(input("Enter a number to calculate its factorial: "))
            break
        except ValueError:
            print("\033[1;31mInvalid input. Please enter a valid number.\033[0m")
    print(f"The factorial of {number} is calculated using the examples in the file.")
    input("Press Enter to complete the lesson...")
    print("\033[1;36mLesson completed!\033[0m")

# Function to generate random examples for Fibonacci Lesson
def fibonacci_lesson():
    print("\033[1;34mWelcome to the Fibonacci Lesson!\033[0m")
    sequence_length = random.randint(5, 10)
    print(f"Step 1: The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.")
    print(f"Example: Let's generate the first {sequence_length} numbers of the Fibonacci sequence.")
    input("Press Enter to continue...")
    print("Step 2: Fibonacci numbers are often used in algorithms and data structures.")
    input("Press Enter to continue...")
    print("Step 3: Let's calculate Fibonacci numbers using Python.")
    print("Code:")
    print("    def fibonacci(n):")
    print("        if n <= 0:")
    print("            return 0")
    print("        elif n == 1:")
    print("            return 1")
    print("        else:")
    print("            return fibonacci(n - 1) + fibonacci(n - 2)")
    input("Press Enter to continue...")
    print(f"\033[1;36mLesson completed! You explored Fibonacci sequences up to {sequence_length} terms.\033[0m")

# Function to generate random examples for Authorization Lesson
def authorization_lesson():
    print("\033[1;34mWelcome to the Authorization Lesson!\033[0m")
    usernames = ["admin", "user1", "guest"]
    selected_user = random.choice(usernames)
    print(f"Step 1: Authorization is the process of verifying if a user has access to a resource.")
    print(f"Example: Let's authorize the user '{selected_user}'.")
    input("Press Enter to continue...")
    print("Step 2: Authorization often involves checking usernames and passwords.")
    input("Press Enter to continue...")
    print("Step 3: Let's implement a basic authorization system in Python.")
    print("Code:")
    print("    def authorize(username, password):")
    print("        if username == 'admin' and password == 'password':")
    print("            return 'Access granted'")
    print("        else:")
    print("            return 'Access denied'")
    input("Press Enter to continue...")
    print(f"\033[1;36mLesson completed! You learned about authorizing the user '{selected_user}'.\033[0m")

# Function to generate random examples for Additional Examples Lesson
def additional_examples_lesson():
    print("\033[1;34mWelcome to the Additional Examples Lesson!\033[0m")
    print("Step 1: Understanding Different Summing Methods")
    print("In this lesson, we will explore various ways to calculate the sum of a list of numbers.")
    input("Press Enter to continue...")

    print("Step 2: Using List Comprehension")
    print("This method uses a list comprehension to create a new list of numbers and then sums them.")
    print("Code:")
    print("""
    def sum_with_comprehension(list_of_nums):
        return sum([num for num in list_of_nums])
    """)
    input("Press Enter to continue...")

    print("Step 3: Using a While Loop")
    print("This method uses a while loop to iterate through the list and calculate the sum.")
    print("Code:")
    print("""
    def sum_with_while_loop(list_of_nums):
        total = 0
        index = 0
        while index < len(list_of_nums):
            total += list_of_nums[index]
            index += 1
        return total
    """)
    input("Press Enter to continue...")

    print("Step 4: Using Reduce from functools")
    print("This method uses the reduce function to calculate the sum of the list.")
    print("Code:")
    print("""
    from functools import reduce

    def sum_with_reduce(list_of_nums):
        return reduce(lambda x, y: x + y, list_of_nums)
    """)
    input("Press Enter to continue...")

    print("Step 5: Using Numpy for Summation")
    print("This method uses the numpy library to calculate the sum of the list.")
    print("Code:")
    print("""
    import numpy as np

    def sum_with_numpy(list_of_nums):
        return np.sum(list_of_nums)
    """)
    input("Press Enter to continue...")

    print("Step 6: Full Code Example")
    print("Here is the full code combining all methods:")
    print("""
    # Additional Examples of Summing Methods in Python

    # Example 1: Using List Comprehension
    def sum_with_comprehension(list_of_nums):
        return sum([num for num in list_of_nums])

    # Example 2: Using a While Loop
    def sum_with_while_loop(list_of_nums):
        total = 0
        index = 0
        while index < len(list_of_nums):
            total += list_of_nums[index]
            index += 1
        return total

    # Example 3: Using Reduce from functools
    from functools import reduce

    def sum_with_reduce(list_of_nums):
        return reduce(lambda x, y: x + y, list_of_nums)

    # Example 4: Using Numpy for Summation
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
    """)
    input("Press Enter to complete the lesson...")
    print("\033[1;36mLesson completed!\033[0m")

# Function to generate random examples for Functions Lesson
def functions_lesson():
    print("\033[1;34mWelcome to the Functions Lesson!\033[0m")
    print("Step 1: What are Functions?")
    print("Functions are reusable blocks of code that perform a specific task. They help in organizing and reusing code.")
    input("Press Enter to continue...")

    print("Step 2: Anatomy of a Function")
    print("A function typically has a name, parameters, a body, and a return statement.")
    print("Code:")
    print("""
    def greet(name):
        return f"Hello, {name}!"
    """)
    input("Press Enter to continue...")

    print("Step 3: Types of Functions")
    print("1. Built-in Functions: Provided by Python, e.g., len(), print().")
    print("2. User-defined Functions: Created by the user.")
    print("3. Lambda Functions: Anonymous functions defined using the lambda keyword.")
    input("Press Enter to continue...")
    print("Step 4: Full Code Example")
    print("Here is a full example demonstrating different types of functions:")
    print("""
    # Example of a User-defined Function
    def add(a, b):
        return a + b

    # Example of a Lambda Function
    multiply = lambda x, y: x * y

    # Using Built-in Functions
    numbers = [1, 2, 3, 4, 5]
    print("Length of list:", len(numbers))
    print("Sum of list:", sum(numbers))

    # Using User-defined and Lambda Functions
    print("Addition:", add(10, 5))
    print("Multiplication:", multiply(10, 5))
    """)
    input("Press Enter to complete the lesson...")
    print("\033[1;36mLesson completed!\033[0m")

# Function to handle New Function Lesson
def new_function_lesson():
    print("\033[1;34mWelcome to the New Function Lesson!\033[0m")
    print("Step 1: Learn how to create and use new functions in Python.")
    input("Press Enter to continue...")
    print("Step 2: Functions allow you to encapsulate logic and reuse it.")
    input("Press Enter to continue...")
    print("Step 3: Let's write a new function in Python.")
    print("Code:")
    print("    def new_function(param):")
    print("        return param * 2")
    input("Press Enter to continue...")
    print("\033[1;36mLesson completed! You learned about creating new functions.\033[0m")

# Function to handle Recursion Lesson
def recursion_lesson():
    print("\033[1;34mWelcome to the Recursion Lesson!\033[0m")
    print("Step 1: What is Recursion?")
    print("Recursion is a technique where a function calls itself to solve smaller instances of a problem.")
    input("Press Enter to continue...")

    print("Step 2: Key Concepts")
    print("1. Base Case: The condition under which the recursion stops.")
    print("2. Recursive Case: The part of the function where it calls itself to solve a smaller problem.")
    input("Press Enter to continue...")

    print("Step 3: Example - Factorial Calculation")
    print("Code:")
    print("""
    def factorial_recursive(n):
        if n == 0 or n == 1:  # Base case
            return 1
        else:
            return n * factorial_recursive(n - 1)  # Recursive case
    """)
    input("Press Enter to continue...")

    print("Step 4: Example - Fibonacci Sequence")
    print("Code:")
    print("""
    def fibonacci_recursive(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    """)
    input("Press Enter to continue...")

    print("Step 5: Advantages and Disadvantages")
    print("Advantages:")
    print("- Simplifies code for problems with a natural recursive structure.")
    print("- Makes the code more readable for certain problems.")
    print("Disadvantages:")
    print("- Can lead to high memory usage due to the function call stack.")
    print("- May be less efficient than iterative solutions for some problems.")
    input("Press Enter to continue...")

    print("Step 6: Practice Problems")
    print("1. Write a recursive function to calculate the sum of all elements in a list.")
    print("2. Implement a recursive function to reverse a string.")
    print("3. Create a recursive function to find the greatest common divisor (GCD) of two numbers.")
    input("Press Enter to complete the lesson...")
    print("\033[1;36mLesson completed!\033[0m")

# Function to randomly select lessons
LESSONS = [
    "Factorial",
    "Fibonacci",
    "Authorization",
    "Additional Examples",
    "Functions",
    "New Function",
    "Recursion"
]

def choose_random_lessons():
    print("\033[1;34mRandomly selecting lessons for you...\033[0m")
    selected_lessons = random.sample(LESSONS, k=random.randint(1, len(LESSONS)))
    print(f"\033[1;32mSelected lessons: {', '.join(selected_lessons)}\033[0m")
    return selected_lessons

# Function to handle multiple lessons step by step
def handle_lessons(selected_lessons):
    for lesson in selected_lessons:
        if lesson == "Factorial":
            factorial_lesson()
        elif lesson == "Fibonacci":
            fibonacci_lesson()
        elif lesson == "Authorization":
            authorization_lesson()
        elif lesson == "Additional Examples":
            additional_examples_lesson()
        elif lesson == "Functions":
            functions_lesson()
        elif lesson == "New Function":
            new_function_lesson()
        elif lesson == "Recursion":
            recursion_lesson()

# Function to play the game with menu selection
def play_game():
    user_data = get_or_create_user()
    while True:
        print("\033[1;34mChoose a lesson from the menu:\033[0m")
        lesson_choice = choose_lesson()
        if lesson_choice == 1:
            factorial_lesson()
        elif lesson_choice == 2:
            fibonacci_lesson()
        elif lesson_choice == 3:
            authorization_lesson()
        elif lesson_choice == 4:
            additional_examples_lesson()
        elif lesson_choice == 5:
            functions_lesson()
        elif lesson_choice == 6:
            new_function_lesson()
        elif lesson_choice == 7:
            recursion_lesson()
        elif lesson_choice == 8:
            print("\033[1;31mExiting the game. Goodbye!\033[0m")
            break

# Main function to run the game
if __name__ == "__main__":
    print("\033[1;34mCoded by Nico Kuehn\033[0m")
    play_game()

# Coded by Nico Kuehn