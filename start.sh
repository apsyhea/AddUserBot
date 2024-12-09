#!/bin/bash

# Move to the script directory
cd "$(dirname "$0")"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv

    echo "Activating virtual environment..."
    source venv/bin/activate

    echo "Installing dependencies..."
    pip install -r requirements.txt

    echo "Running the program..."
    python3 src/main.py

    echo "Deactivating virtual environment..."
    deactivate
else
    echo "Activating virtual environment..."
    source venv/bin/activate

    echo "Running the program..."
    python3 src/main.py

    echo "Deactivating virtual environment..."
    deactivate
fi

# Pause to see the output before the script closes
read -p "Press [Enter] key to continue..."
