#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate

# Check if activation was successful
if [ $? -ne 0 ]; then
    echo "Error occurred trying to activate the virtual environment."
    exit 1
fi

# Install requirements from requirements.txt
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found."
fi

# Install specific PyTorch and Torchvision versions for CPU
pip install torch==1.12.1+cpu torchvision==0.13.1+cpu --extra-index-url https://download.pytorch.org/whl/cpu

# Clone the Salesforce BLIP repository
git clone https://github.com/salesforce/BLIP scripts/BLIP

# Check if the clone was successful
if [ $? -ne 0 ]; then
    echo "Error occurred trying to clone the BLIP repository."
    exit 1
fi

echo "Setup complete."
