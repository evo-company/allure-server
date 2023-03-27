FROM node:19.8.1 as dependencies

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./

RUN npm install --legacy-peer-deps --no-audit

FROM node:19.8.1-alpine as builder

WORKDIR /app
COPY --from=dependencies /app /app
COPY . .

ENV NODE_ENV production
RUN npm run build .

FROM nginx:1.19.3-alpine

WORKDIR /ui
COPY etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
RUN sed -ri 's/^pid[^;]+;$/pid \/tmp\/nginx.pid;/g' /etc/nginx/nginx.conf
COPY --from=builder /app/dist ./dist
