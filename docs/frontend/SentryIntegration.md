# Sentry Integration   

## Setup

Follow [sentry setup instructions][sentry setup instructions] for up to date instructions. See below for quick setup

1. Install sentry client
    ```bash 
    npm install --save @sentry/vue @sentry/tracing
    ```
2. Configure sentry client: 
   
   [main.js][main.js]
    ```js
    const MONITORED_ENVIRONMENTS = ["staging", "production"]; // Which environments to monitor
    if (MONITORED_ENVIRONMENTS.includes(process.env.NODE_ENV)) {
      Sentry.attachErrorHandler(Vue, {  // Without this errors wont show in the console
        logErrors: true
      });
    
      Sentry.init({
        Vue,
        environment: process.env.NODE_ENV,   // Sentry will group events by environment
        dsn: process.env.VUE_APP_SENTRY_DSN,   // Set in frontend/.env
        integrations: [
          new BrowserTracing({
            routingInstrumentation: Sentry.vueRouterInstrumentation(router),
            tracingOrigins: [process.env.VUE_APP_API_URL]
          })
        ],
        tracesSampleRate: 1.0,
        release: process.env.VUE_APP_RELEASE_TAG,  // Group events by release
      });
    }
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
      needs: ["Pytest", "flake8", "Test Frontend"]
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
3. Set release tag as vue env variable:   
   
    [frontend/Dockerfile.frontend][frontend dockerfile]
    ```Dockerfile{2,4}
    FROM node:14 as frontend-builder
    ARG release_tag=staging
    ARG env=production
    ENV VUE_APP_RELEASE_TAG=$release_tag
    ...
    ```

### Source Maps
By providing sentry with sourcemaps we can inspect the source code from within events. This makes identifying the problem
easier, as we can see the line it occured on in our source code rather than just the compiled code.

See [sentry source maps docs][sentry source maps] for a list of all approaches to providing sentry with source maps.

### Forge Source Maps Config
In Forge we upload the sourcemaps during the docker build phase. By avoiding doing it in the frontend, 
we can avoid bundling the SENTRY_AUTH_TOKEN in our app.

1. Once the image is built we extract the sourcemaps and save them as artefacts:  

    [gitlab-tasks.yml][gitlab-tasks.yml]
    ```yml {6-11} 
    .docker-build: &docker-build
      image: $DOCKER_IMAGE
      tags:
        - docker-privileged
      ...
        # Extract sourcemaps from docker image if frontend image
        - if [ "${DOCKERFILE}" == "Dockerfile.frontend" ]; then mkdir sourcemaps && docker cp $(docker create --rm ${IMAGE_TAG}):/usr/share/caddy/js/. sourcemaps ; fi
      artifacts:
        paths:
          - sourcemaps/
        expire_in: 1 week
    ```
2. Then during the release stage we upload them to Sentry using the sentry-cli:  

    [gitlab-ci.yml][gitlab-ci.yml]
    ```yml {12-14}
    # Create new sentry release and send sourcemaps
    Update Sentry:
      stage: release
      image: getsentry/sentry-cli
      ...
      script:
        - export SENTRY_AUTH_TOKEN=$SENTRY_AUTH_TOKEN
        - export SENTRY_ORG=$SENTRY_ORG
        - export SENTRY_PROJECT=$SENTRY_PROJECT
        - echo "Creating new sentry release with tag $RELEASE_TAG..."
        - sentry-cli releases new $RELEASE_TAG
        - echo "Uploading sourcemaps files to Sentry..."
        - ls ${CI_PROJECT_DIR}/sourcemaps
        - sentry-cli releases files $RELEASE_TAG upload-sourcemaps ${CI_PROJECT_DIR}/sourcemaps
        - echo "Finalizing sentry release and setting commits..."
        - sentry-cli releases finalize $RELEASE_TAG
        - sentry-cli releases set-commits --auto $RELEASE_TAG
        - echo "Finalized release, set commits and uploaded sourcemaps for release $RELEASE_TAG"
      tags:
        - docker
    ```

[sentry setup instructions]: https://docs.sentry.io/platforms/javascript/guides/vue/
[sentry releases]: https://docs.sentry.io/product/releases/
[frontend dockerfile]: https://gitlab.liip.ch/liip/forge/-/blob/master/frontend/Dockerfile.frontend
[main.js]: https://gitlab.liip.ch/liip/forge/-/blob/master/frontend/src/main.js
[gitlab-tasks.yml]: https://gitlab.liip.ch/liip/forge/-/blob/master/.gitlab-tasks.yml
[gitlab-ci.yml]: https://gitlab.liip.ch/liip/forge/-/blob/master/.gitlab-ci.yml
[sentry source maps]: https://docs.sentry.io/platforms/javascript/sourcemaps/