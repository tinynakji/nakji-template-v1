# Build step #1: build the React front end
FROM node:16-alpine as build-step
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH

# Install; do this early so this layer is cached
COPY react_app/package.json ./
COPY react_app/yarn.lock  ./
RUN yarn install

# ARG API_PATH; annoying
ARG API_PATH=$API_PATH
RUN echo "The API_PATH variable value is $API_PATH"
ENV API_PATH=$API_PATH
# ENV NEXT_PUBLIC_URL=http://0.0.0.0:3000

# Build after setting env vars
COPY react_app/src ./src
COPY react_app/public ./public
COPY react_app/next.config.js ./next.config.js
RUN yarn build

EXPOSE 3000
CMD ["yarn", "start"]

# Build step #2: build an nginx container
# FROM nginx:stable-alpine
# COPY --from=build-step /app/build /usr/share/nginx/html
# COPY deployment/nginx.default.conf /etc/nginx/conf.d/default.conf