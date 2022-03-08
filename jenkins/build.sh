#!/bin/bash

echo "Build stage"

# build image for flask app
docker build -t $DOCKER_HUB_CREDS_USR/flaskapp:latest .
