# Function Lessons Game

Welcome to the **Function Lessons Game**! This interactive Python program is designed to teach you various programming concepts through engaging lessons and exercises. The game tracks your progress, remembers your name, and provides a personalized learning experience.

## Features

- **Interactive Lessons**: Learn about factorials, Fibonacci sequences, authorization, additional examples, and functions step by step.
- **Randomized Lessons**: Each session offers a unique set of lessons to keep the learning experience fresh and engaging.
- **Progress Tracking**: Your name and completed lessons are saved in a JSON file, along with timestamps for when each lesson was completed.
- **Dynamic Feedback**: The program provides hints and feedback for invalid inputs, ensuring a smooth learning process.
- **Colorful Output**: Enjoy a visually appealing interface with color-coded instructions and results.

## How It Works

1. **Start the Game**: Run the `exercise_game.py` script to begin.
2. **Enter Your Name**: The program will ask for your name and save it for future sessions.
3. **Choose Lessons**: You can either select specific lessons or let the program randomly choose for you.
4. **Learn Step by Step**: Each lesson is broken down into manageable steps, complete with code examples and explanations.
5. **Track Your Progress**: Your completed lessons and timestamps are saved in the `user_data.json` file.

## Lessons Available

1. **Factorial**: Learn how to calculate factorials using iterative and recursive methods.
2. **Fibonacci**: Understand the Fibonacci sequence and how to implement it in Python.
3. **Authorization**: Explore basic and advanced authorization techniques, including lockout mechanisms.
4. **Additional Examples**: Dive into various programming examples to enhance your skills.
5. **Functions**: Master the fundamentals of functions in Python, including recursion and built-in functions.

## File Structure

- `exercise_game.py`: Main script to run the game.
- `user_data.json`: Stores user data, including name, completed lessons, and timestamps.
- `new_function.py`: Contains utility functions used in the game.
- `factorial_examples.py`, `fibonacci_examples.py`, `authorize.py`, `additional_examples.py`: Lesson-specific scripts.
- `README.md`: This file.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/nicokuehn-dci/function_lessons.git
   ```
2. Navigate to the project directory:
   ```bash
   cd function_lessons
   ```
3. Run the main script:
   ```bash
   python3 exercise_game.py
   ```

## Requirements

- Python 3.6 or higher
- Linux or any compatible operating system

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for new features, bug fixes, or improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

Created by Nico Kuehn as part of an interactive learning project. Happy coding!
