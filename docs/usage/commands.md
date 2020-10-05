# Commands
## Use the Makefile to run docker-compose commands
To avoid some typing there is a Makefile that includes the most frequent 
commands to control the application.

- `make start` will start your docker containers
- `make stop` will stop your docker containers
- `make status` will show you the current status of your containers
- `make restart` will run `make stop` and `make start`
- `make clean` will remove your docker containers and all the `*.pyc` files
- `make logs` will show you the tail of all the container logs
- `make migrate` will run migrations inside your `backend` django container
- `make makemigrations` will add missing migrations inside your `backend` django container
- `make superuser` will create a superuser inside your `backend` django container
