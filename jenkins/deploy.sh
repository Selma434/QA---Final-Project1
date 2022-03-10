#!/bin/bash

echo "Deploy stage"

# deploy using docker stack

scp docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml

ssh jenkins@swarm-manager \
    DATABASE_URI=$DATABASE_URI \
    DOCKER_HUB_CREDS_USR=$DOCKER_HUB_CREDS_USR \
    MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD \
    MYSQL_DATABASE=$MYSQL_DATABASE \
    docker stack deploy --compose-file docker-compose.yaml final-project