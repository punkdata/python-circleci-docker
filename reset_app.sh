#!/bin/bash

############################
# Reset the hellow_world app on a server
#
# Use:  ssh -o StrictHostKeyChecking=no root@hello.dpunks.org "./reset_app.sh"  replace with our server hostname
#
#############################

echo "Removing Hello World to Docker Container"
docker stop hello_world
echo "Stoping Hello World in Docker Container"
docker ps -a