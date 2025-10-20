# Stage 1: Angular build
FROM node:16.20-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build -- --configuration production --base-href=/

# Stage 2: Serve with NGINX
FROM nginx:1.25-alpine

RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /app/dist/generated-ui /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
