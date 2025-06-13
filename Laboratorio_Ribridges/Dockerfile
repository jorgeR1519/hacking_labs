# usa Debian slim para evitar crashes de sqlite
FROM node:18-slim

WORKDIR /app

# Instala dependencias de producción
COPY package.json package-lock.json ./
RUN npm ci --only=production

# Copia todo el código
COPY . .

# Da permisos al init
RUN chmod +x init.sh

# Exponer puertos
EXPOSE 3000 3001

# Arranque
ENTRYPOINT ["/app/init.sh"]
