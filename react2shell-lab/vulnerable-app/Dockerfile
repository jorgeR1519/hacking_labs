FROM node:18-alpine
WORKDIR /app
COPY package.json package-lock.json* ./
# npm ci instalará dependencias (incluye las versiones definidas en package.json)
RUN npm ci --production --legacy-peer-deps
COPY . .
EXPOSE 8080
CMD ["node", "server.js"]
