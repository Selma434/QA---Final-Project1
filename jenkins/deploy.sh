#!/bin/bash

echo "Deploy stage"

# deploy using docker stack
docker stack deploy --compose-file docker-compose.yaml final-project