#!/bin/bash

reg_user=$1
reg_password=$2
reg=$3
project_path=$4
docker_server_tag=$5
cd /srv/app/deploy

echo "Pulling the docker images"
echo ${reg_password} | docker login -u ${reg_user} --password-stdin ${reg}
docker pull ${reg}/${project_path}:backend_${docker_server_tag}
docker pull ${reg}/${project_path}:frontend_${docker_server_tag}
docker pull ${reg}/${project_path}:docs_${docker_server_tag}

echo "Starting the docker containers"
docker-compose up -d

echo "Migrating the backend"
docker-compose exec -T backend python manage.py migrate_schemas

echo "Pruning the images"
docker system prune -a -f
docker logout ${reg}
