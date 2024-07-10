#!/bin/bash

docker system prune -a -f 
docker container prune -f 
docker buildx prune -f
docker network prune -f 