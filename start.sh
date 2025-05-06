#!/bin/bash

# Function to display a message and ask for user confirmation
ask_permission() {
    echo -e "\033[1;34m$1\033[0m"
    read -p "Do you want to proceed? (yes/no): " choice
    case "$choice" in
        yes|YES|y|Y) return 0 ;;
        no|NO|n|N) return 1 ;;
        *) echo "Invalid input. Please enter 'yes' or 'no'."; ask_permission "$1" ;;
    esac
}

# Step 1: Check for Python installation
if ! command -v python3 &> /dev/null; then
    echo -e "\033[1;31mPython3 is not installed. Please install Python3 to proceed.\033[0m"
    exit 1
fi

# Step 2: Create a virtual environment
if ask_permission "A virtual environment is recommended to isolate dependencies. Create one now?"; then
    if [ ! -d "venv" ]; then
        python3 -m venv venv
        echo -e "\033[1;32mVirtual environment created successfully.\033[0m"
    else
        echo -e "\033[1;33mVirtual environment already exists.\033[0m"
    fi
    echo -e "\033[1;34mActivating the virtual environment...\033[0m"
    source venv/bin/activate
else
    echo -e "\033[1;33mProceeding without a virtual environment.\033[0m"
fi

# Step 3: Install dependencies
if ask_permission "Install required dependencies (e.g., colorama for colorful output)?"; then
    pip install --upgrade pip
    pip install colorama
    echo -e "\033[1;32mDependencies installed successfully.\033[0m"
else
    echo -e "\033[1;33mSkipping dependency installation.\033[0m"
fi

# Step 4: Run the main script
if ask_permission "Run the main script (exercise_game.py) now?"; then
    python3 exercise_game.py
else
    echo -e "\033[1;33mYou can run the script later by executing: python3 exercise_game.py\033[0m"
fi

# Step 5: Deactivate virtual environment (if activated)
if [ -n "$VIRTUAL_ENV" ]; then
    deactivate
    echo -e "\033[1;34mVirtual environment deactivated.\033[0m"
fi

# Coded by Nico Kuehn

exit 0