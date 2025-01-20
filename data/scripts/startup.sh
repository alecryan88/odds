#!/bin/zsh
echo "Running Docker Build..."

pwd 

ls

docker login

docker build data/docker -t test:dev

sleep 2

docker run -it test:dev