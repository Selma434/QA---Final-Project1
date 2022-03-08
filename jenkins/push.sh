#!/bin/bash

echo "Push stage"

# push image to docker hub

docker push $DOCKER_HUB_CREDS_USR/flaskapp:latest