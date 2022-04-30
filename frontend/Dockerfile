# source: https://typeofnan.dev/how-to-serve-a-react-app-with-nginx-in-docker/

# Name the node stage "builder"
FROM node:14-alpine AS builder
# Set working directory
WORKDIR /app

COPY react-app/package.json react-app/package-lock.json ./
RUN npm i --no-optional

# Copy all files from current directory to working dir in image
COPY react-app/ .

# build the app
RUN npm run build

# nginx state for serving content
FROM nginx:alpine
# Set working directory to nginx asset directory
WORKDIR /usr/share/nginx/html
# Remove default nginx static assets
RUN rm -rf ./*
# Copy static assets from builder stage
COPY --from=builder /app/build .

COPY nginx.conf /etc/nginx/conf.d/default.conf
# Containers run nginx with global directives and daemon off
ENTRYPOINT ["nginx", "-g", "daemon off;"]