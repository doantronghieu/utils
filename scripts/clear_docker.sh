#!/bin/bash

docker system prune -a -f -y
docker container prune -f -y
docker buildx prune -f
docker network prune -f -y
