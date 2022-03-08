#!/bin/bash

echo "Build stage"

# build image
docker build -t $DOCKER_HUB_CREDS_USR/flaskapp:latest .
