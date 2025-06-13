#!/bin/sh
# Inicializa la base de datos
node init-db.js
# Ejecuta el comando definido en cada servicio
exec "$@"
