# syntax=docker/dockerfile:1
FROM node:18-bullseye-slim
ENV NODE_ENV=production

# Default location for subsequent commands
WORKDIR /app

# Install packages
COPY package.json ./
COPY yarn.lock ./
RUN yarn install --production --immutable --non-interactive --pure-lockfile --no-cache

# Add code to image
COPY ./server.js ./server.js

# Start server
CMD node ./server.js
