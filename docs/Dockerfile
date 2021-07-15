FROM node:lts-alpine as build-stage
WORKDIR /code
COPY package*.json ./
RUN npm install
COPY . /code

EXPOSE 8081
CMD ["npm", "run", "start"]
