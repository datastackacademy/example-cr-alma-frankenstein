#!/bin/bash
# start mariadb docker container with empty database named spotify
docker run --name mariadb \
    -p 127.0.0.1:3306:3306 \
    -e MYSQL_ROOT_PASSWORD=mysql \
    -v $(pwd)/data:/docker-entrypoint-initdb.d \
    -v ch2gdb:/var/lib/mysql \
    --rm -d \
    mariadb:latest