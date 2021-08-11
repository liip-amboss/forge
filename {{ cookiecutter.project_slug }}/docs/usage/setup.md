# Project setup

## Pontsun
The Forge project is designed to work with Pontsun, a local development environment maintained by Liip. Before you can use Forge you have to make sure you have Pontsun configured and running.
How to get started with Pontsun: https://github.com/liip/pontsun

## Forge
Once you have Ponstun up and running you can start the Forge docker containers. 
1. Make a copy of the `.env.dist` file and name it `.env`.
2. Adapt the environment variables to your needs
3. Run `INITIAL=1 docker-compose up` (if you use the fish shell you can run `set -x INITIAL 1; docker-compose up`)
    - If the backend fails to start, check that your user has permissions on the backend/.venv folder
    - To also setup the default data, run `make migrate` after containers are up
    - If you are all set up, reset the install flag `INITIAL=0`

All your services are now available on the urls you added in .env:
* The vue website frontend on: FRONTEND_URL
* The django rest api on: BACKEND_URL
* The vue style guide on: STYLEGUIDE_URL
* The documentation on: DOCS_URL
* PGAdmin on: PGADMIN_URL
 
## Add git config                                                                
```                                                                             
mkdir -p .git/hooks/ && ln -f templates/git/hooks/commit-msg .git/hooks/commit-msg
``` 
