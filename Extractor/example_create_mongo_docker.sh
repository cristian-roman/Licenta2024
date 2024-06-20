#!/bin/bash

# Container name
CONTAINER_NAME=mongo-container

# Check if the container is already running
if [ "$(docker ps -q -f name=${CONTAINER_NAME})" ]; then
    # Stop the running container
    docker stop ${CONTAINER_NAME}
fi

# Check if the container exists (including stopped containers)
if [ "$(docker ps -aq -f name=${CONTAINER_NAME})" ]; then
    # Remove the existing container
    docker rm ${CONTAINER_NAME}
fi

# Run a new container with the specified name
docker run -d \
    --name ${CONTAINER_NAME} \
    -e MONGO_INITDB_ROOT_USERNAME=admin \
    -e MONGO_INITDB_ROOT_PASSWORD=admin \
    -p 27017:27017 \
    mongo

