# create backend container
FROM python:3.8-buster AS backend-builder
ARG env
ADD requirements /requirements/
RUN set -ex \
    && apt-get update \
    && apt-get install build-essential --no-install-recommends -y \
    && pip install uwsgi==2.0.17

RUN if [ "$env" = "staging" ] ; then pip install -r requirements/dev.txt; else pip install -r requirements/base.txt; fi
# for MEDIA_ROOT
RUN mkdir /uploads
RUN chown 1000 /uploads

FROM python:3.8-buster
ARG release_tag=RELEASE_TAG_MISSING
ENV RELEASE_TAG=$release_tag
EXPOSE 8000
RUN mkdir /code

# copy site-packages with compiled binaries from backend-builder
COPY --from=backend-builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=backend-builder /usr/local/bin/uwsgi /usr/local/bin/uwsgi

# copy code into container
ADD . /code/

WORKDIR /code

RUN EMAIL_URL=email SECRET_KEY=none DEBUG=False python manage.py collectstatic --noinput

ADD ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh

CMD ["/docker-entrypoint.sh"]
