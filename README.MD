# <h1 align="center">Forge</h1>
<p align="center">Forge is a easy to use combination of the most modern frameworks to create custom
web-applications.
The frontend is based on vue.js and tailwind while the backend is based on django.
All components run in docker containers, so there is no need to install anything
else than docker to use forge. However, to run forge locally you will need pontsun.</p>

![Build Status](https://gitlab.liip.ch/liip/forge/badges/master/pipeline.svg)

## Contribution
Feel free to create an MR on our gitlab instance to contribute to this project: https://gitlab.liip.ch/liip/forge/
## Local Setup
1. Install and run [pontsun][pontsun].

2. Start docker compose.
    ```bash
    # Copy template env file
    cp .env.dist .env

    # Start containers
    docker-compose up

    # Run django migrations_
    docker-compose exec backend python manage.py migrate
    ```
3. If you used default env files for pontsun and forge the following urls should be available:
Frontend: http://forge.docker.test
Docs: http://docs.forge.docker.test
Styleguide: http://styleguide.forge.docker.test
backend: http://api.forge.docker.test/admin

## Documentation and Styleguide
Styleguide: https://styleguide.forge.bedev.liip.ch/
Documentation: https://docs.forge.bedev.liip.ch

## Want to help?
Want to file a bug, contribute some code, or improve documentation? Excellent! 
Read up on our guidelines for [contributing][contributing].

[contributing]: https://gitlab.liip.ch/liip/forge/-/blob/master/CODE_OF_CONDUCT.md
[pontsun]: https://github.com/liip/pontsun/tree/main
