FROM node:lts-alpine as frontend-builder
WORKDIR /code/src
COPY src ./src
COPY package*.json ./
COPY .eslintrc.js ./
COPY babel.config.js ./
COPY postcss.config.js ./
COPY tailwind.config.js ./
COPY vue.config.js ./
COPY prettier.config.js ./
COPY .env* ./
RUN npm install
RUN npm run build -- --mode dev


FROM caddy:2.1.1-alpine
COPY Caddyfile /etc/caddy/

COPY --from=frontend-builder /code/src/dist /usr/share/caddy/
