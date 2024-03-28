#!/usr/bin/env bash
if [ ! -d "venv" ]; then
    # Create a virtual environment named venv inside the backend directory
    python3 -m venv backend/venv
fi
source backend/venv/bin/activate.fish
cd backend
python3 runserver.py