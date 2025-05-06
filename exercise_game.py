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
    print("7. Exit")
    while True:
        try:
            choice = int(input("\033[1;35mEnter the number of your choice: \033[0m"))
            if choice in range(1, 8):
                return choice
            else:
                print("\033[1;31mInvalid choice. Please select a number between 1 and 7.\033[0m")
        except ValueError:
            print("\033[1;31mInvalid input. Please enter a number.\033[0m")

# Function to handle lessons step by step
def factorial_lesson():
    print("\033[1;34mWelcome to the Factorial Lesson!\033[0m")
    number = random.randint(3, 10)
    print(f"Step 1: A factorial of a number is the product of all positive integers up to that number.")
    print(f"Example: {number}! = {number} * {number-1} * {number-2} * ... * 1")
    input("Press Enter to continue...")
    print("Step 2: Factorials are often used in permutations and combinations.")
    input("Press Enter to continue...")
    print("Step 3: Let's calculate a factorial using Python.")
    print("Code:")
    print("    def factorial(n):")
    print("        if n == 0 or n == 1:")
    print("            return 1")
    print("        else:")
    print("            return n * factorial(n - 1)")
    input("Press Enter to continue...")
    print(f"\033[1;36mLesson completed! You learned about factorials using the number {number}.\033[0m")

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
    operations = ["sum", "product", "average"]
    selected_operation = random.choice(operations)
    numbers = [random.randint(1, 10) for _ in range(5)]
    print(f"Step 1: Let's perform a {selected_operation} operation on the numbers {numbers}.")
    input("Press Enter to continue...")
    print("Step 2: These operations are commonly used in data analysis and statistics.")
    input("Press Enter to continue...")
    print("Step 3: Let's implement the {selected_operation} operation in Python.")
    print("Code:")
    if selected_operation == "sum":
        print("    result = sum(numbers)")
    elif selected_operation == "product":
        print("    result = 1")
        print("    for num in numbers:")
        print("        result *= num")
    elif selected_operation == "average":
        print("    result = sum(numbers) / len(numbers)")
    input("Press Enter to continue...")
    print(f"\033[1;36mLesson completed! You performed a {selected_operation} operation on {numbers}.\033[0m")

# Function to generate random examples for Functions Lesson
def functions_lesson():
    print("\033[1;34mWelcome to the Functions Lesson!\033[0m")
    function_names = ["add", "subtract", "multiply", "divide"]
    selected_function = random.choice(function_names)
    print(f"Step 1: Functions are reusable blocks of code that perform a specific task.")
    print(f"Example: Let's implement a function to {selected_function} two numbers.")
    input("Press Enter to continue...")
    print("Step 2: Functions help in organizing and reusing code.")
    input("Press Enter to continue...")
    print("Step 3: Let's write a Python function to {selected_function} two numbers.")
    print("Code:")
    if selected_function == "add":
        print("    def add(a, b):")
        print("        return a + b")
    elif selected_function == "subtract":
        print("    def subtract(a, b):")
        print("        return a - b")
    elif selected_function == "multiply":
        print("    def multiply(a, b):")
        print("        return a * b")
    elif selected_function == "divide":
        print("    def divide(a, b):")
        print("        return a / b")
    input("Press Enter to continue...")
    print(f"\033[1;36mLesson completed! You implemented a function to {selected_function} two numbers.\033[0m")

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

# Function to randomly select lessons
LESSONS = [
    "Factorial",
    "Fibonacci",
    "Authorization",
    "Additional Examples",
    "Functions",
    "New Function"
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

# Function to play the game with random lessons
def play_game():
    user_data = get_or_create_user()
    while True:
        print("\033[1;34mDo you want to learn random lessons? (yes/no)\033[0m")
        choice = input("\033[1;35mEnter your choice: \033[0m").strip().lower()
        if choice == "yes":
            selected_lessons = choose_random_lessons()
            handle_lessons(selected_lessons)
        elif choice == "no":
            print("\033[1;31mExiting the game. Goodbye!\033[0m")
            break
        else:
            print("\033[1;31mInvalid input. Please enter 'yes' or 'no'.\033[0m")

# Main function to run the game
if __name__ == "__main__":
    play_game()

# Coded by Nico Kuehn