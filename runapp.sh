#!/bin/bash

# Navigate to the backend directory
cd ./backend

# Check if venv directory already exists
if [ ! -d "venv" ]; then
    # Create a virtual environment named venv inside the backend directory
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Check if requirements are already installed
if ! pip freeze | grep -q -F -r -x -f requirements.txt; then
    # Install required Python packages
    pip install -r requirements.txt
    echo "Requirements installed."
else
    echo "Requirements are already installed."
fi

# Check if requirements installation was successful
if [ $? -eq 0 ]; then
    # Run the Flask server
    python runserver.py
else
    echo "Error: Setup failed. Please check the logs for details."
fi

# Deactivate the virtual environment
# deactivate
