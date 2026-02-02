#!/bin/sh

# Ejecutar el ataque
python simulate_attack.py

# Mantener el contenedor corriendo para poder ejecutar más comandos
tail -f /dev/null
