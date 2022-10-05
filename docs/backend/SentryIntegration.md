# Sentry Integration   

## Setup

Follow [sentry setup instructions][sentry setup instructions] for up to date instructions. See below for quick setup

1. Install sentry client
    ```bash 
    pip install --upgrade sentry-sdk
    ```
2. Configure sentry client: 
   
   [settings.py][settings.py]
    ```python
   ########################
   #       SENTRY         #
   ########################
   SENTRY_DSN = env('SENTRY_DSN', default=None)
   if SENTRY_DSN and ENVIRONMENT in ['staging', 'production']:
       sentry_sdk.init(
           dsn=SENTRY_DSN,
           environment=ENVIRONMENT,
           integrations=[DjangoIntegration()],
           traces_sample_rate=1.0,  # Consider reducing this value in production.
           send_default_pii=True,
           # RELEASE_TAG is generated in the gitlab pipeline and passed to the dockerfile.
           release=env('RELEASE_TAG', default="RELEASE_TAG_MISSING")
       )
    ```

## Config
### Releases
[Official sentry releases docs][sentry releases]

By including a release tag in sentry init, events will grouped by release tag. 
This allows us to identify which deploy an event belongs to.

A release tag is generated in gitlab ci in the release stage.

### Forge Releases Config
1. Create release tag:   
   
    [gitlab-ci.yml][gitlab-ci.yml]
    ```yml
    # Create release tag and store as artifact
    Generate Release Tag:
      stage: prepare
      image: alpine:latest
      rules:
        - if: $CI_COMMIT_TAG
          when: never
        - if: ($CI_COMMIT_BRANCH == $STAGING_BRANCH || $CI_COMMIT_BRANCH == $PROD_BRANCH)
      needs: ["Pytest", "black", "Test Frontend"]
      script:
        - echo "RELEASE_TAG=$CI_COMMIT_SHORT_SHA" >> variables.env
      artifacts:
        reports:
          dotenv: variables.env
      tags:
        - docker-privileged
    ```
    All following jobs will have access to RELEASE_TAG which contains the last short commit hash.
2. Pass release tag to docker build context:   
   
    [gitlab-tasks.yml][gitlab-tasks.yml]
    ```yml
    .docker-build: &docker-build
      ...
        script:
        ...
        - docker build --cache-from ${IMAGE_TAG} --build-arg env=${ENVIRONMENT} --build-arg release_tag=$RELEASE_TAG -t ${IMAGE_TAG} ${APP}/. -f ${APP}/${DOCKERFILE}
        ...
    ```
3. Set release tag as env variable:   
   
    [backend/Dockerfile][backend dockerfile]
    ```Dockerfile{2,4}
      ...
      FROM python:3.8-buster
      ARG release_tag=staging
      ENV RELEASE_TAG=$release_tag
    ...
    ```

[sentry setup instructions]: https://docs.sentry.io/platforms/javascript/guides/vue/
[sentry releases]: https://docs.sentry.io/product/releases/
[settings.py]: https://gitlab.liip.ch/liip/forge/-/blob/master/backend/app/settings.py
[backend dockerfile]: https://gitlab.liip.ch/liip/forge/-/blob/master/backend/Dockerfile
[gitlab-tasks.yml]: https://gitlab.liip.ch/liip/forge/-/blob/master/.gitlab-tasks.yml
[gitlab-ci.yml]: https://gitlab.liip.ch/liip/forge/-/blob/master/.gitlab-ci.yml

