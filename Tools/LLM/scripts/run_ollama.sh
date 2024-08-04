#!/bin/bash

# Get the directory of the script
SCRIPT_DIR=$(dirname "$0")

# Get the parent directory of the script
PARENT_DIR=$(dirname "$SCRIPT_DIR")

# Construct the path to the ollama.docker-compose.yaml file
COMPOSE_FILE="$PARENT_DIR/ollama.docker-compose.yaml"

# Run the docker compose command
docker compose -f "$COMPOSE_FILE" up -d
