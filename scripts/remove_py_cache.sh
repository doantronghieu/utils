#!/bin/bash

# Define the root directory
ROOT_DIR="/Users/thung/Documents/Me/Coding/"

# Use find command to locate all __pycache__ directories and delete them
find "$ROOT_DIR" -type d -name "__pycache__" -exec rm -rf {} +
