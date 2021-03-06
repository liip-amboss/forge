# create backend container
FROM python:3.8-buster
ARG build_env
ADD requirements /requirements/
RUN set -ex \
    && apt-get update \
    && apt-get install build-essential --no-install-recommends -y \
    && pip install uwsgi==2.0.17

RUN if [ "$build_env" = "build-staging" ] ; then pip install -r requirements/dev.txt; else pip install -r requirements/base.txt; fi
# copy code into container
RUN mkdir /code
ADD . /code/

RUN mkdir /uploads
RUN chown 1000 /uploads

WORKDIR /code
RUN SECRET_KEY=none DEBUG=False python manage.py collectstatic --noinput

EXPOSE 8000

ENV UWSGI_WSGI_FILE=/code/app/wsgi.py UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

RUN chmod a+x docker-entrypoint.sh

CMD ["/code/docker-entrypoint.sh"]
