FROM docker.io/node:18-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install express
COPY server.js data/ ./
CMD ["node", "server.js"]
