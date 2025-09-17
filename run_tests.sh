#!/bin/bash

# Exit immediately if any command fails
set -e

# Path to your virtual environment
VENV_PATH=".venv"

# Check if virtual environment exists
if [ ! -d "$VENV_PATH" ]; then
  echo "❌ Virtual environment not found at $VENV_PATH"
  exit 1
fi

# Activate virtual environment
echo "🔹 Activating virtual environment..."
source "$VENV_PATH/bin/activate"

# Run pytest
echo "🔹 Running test suite..."
pytest -v

# Capture exit code
EXIT_CODE=$?

# Deactivate virtual environment
deactivate

# Return exit code based on pytest results
if [ $EXIT_CODE -eq 0 ]; then
  echo "✅ All tests passed!"
  exit 0
else
  echo "❌ Some tests failed!"
  exit 1
fi
