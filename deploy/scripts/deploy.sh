#!/bin/bash

reg_user=$1
reg_password=$2
reg=$3
project_path=$4
docker_image_name=$5
cd $HOME/srv/app/

echo "Pulling the docker images"
echo ${reg_password} | docker login -u ${reg_user} --password-stdin ${reg}
docker pull ${reg}/${project_path}/backend:${docker_image_name}
docker pull ${reg}/${project_path}/frontend:${docker_image_name}
docker pull ${reg}/${project_path}/docs:${docker_image_name}
docker pull ${reg}/${project_path}/styleguide:${docker_image_name}

echo "Starting the docker containers"
docker-compose up -d

echo "Migrating the backend"
docker-compose exec -T backend python manage.py migrate

echo "Pruning the images"
docker system prune -a -f
docker logout ${reg}
