# CI/CD
Forge includes a [gitlab-ci.yml][gitlab-ci.yml] which includes stages named test-build, deploy and release.   
[gitlab-tasks.yml][gitlab-tasks.yml] includes commonly used tasks for building images and deploying.
All applications are dockerized and are deployed to either a host running docker-compose or to a kubernetes cluster.

## test-build
This stage includes all testing, linting and docker image building. Testing and linting is run on every push.
If the branch is a deploy branch then image building also takes place. 
Deploy branches include; Merge Requests, develop and master.

[Testing](./testing.md)

## deploy
#### Docker compose
Forge deploys staging and production to hosts running docker-compose. Deployment is done via SSH.  
The deploy folder is sent to the host. This folder contains the docker-compose file and any needed config files for the app to run.
Once the deploy folder is copied deploy.sh is run to fetch new images and restart the docker-compose services.

#### Kubernetes
All merge requests are auto deployed to a kubernetes cluster if available.   
See [Review Apps](./reviewapps.md) for more details.

## release
Release stage is only run on deploy to staging or production. This stage creates a new tag, creates a gitlab release,
a sentry release, and uploads sourcemaps to sentry to enhance issues with the source code.

[gitlab-tasks.yml]: https://gitlab.liip.ch/liip/forge/-/blob/master/.gitlab-tasks.yml
[gitlab-ci.yml]: https://gitlab.liip.ch/liip/forge/-/blob/master/.gitlab-ci.yml