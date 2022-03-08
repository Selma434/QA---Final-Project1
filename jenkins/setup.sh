#!/bin/bash

echo "Setup stage"

#apt dependencies
sudo apt update
sudo apt install -y curl jq
sudo apt install python3 python3-venv python3-pip -y

# docker login
docker login --username $DOCKER_HUB_CREDS_USR --password $DOCKER_HUB_CREDS_PSW