FROM python:3.11-alpine

WORKDIR /attacker

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY attack_scripts/ .

# Crear un script de entrada que ejecute el ataque y luego mantenga el contenedor vivo
RUN echo '#!/bin/sh' > /entrypoint.sh && \
    echo 'echo "=== Contenedor de ataque Snowflake ==="' >> /entrypoint.sh && \
    echo 'echo "Para ejecutar el ataque: docker exec attacker-sim python simulate_attack.py"' >> /entrypoint.sh && \
    echo 'echo "Esperando 10 segundos antes de iniciar ataque automático..."' >> /entrypoint.sh && \
    echo 'sleep 10' >> /entrypoint.sh && \
    echo 'python simulate_attack.py' >> /entrypoint.sh && \
    echo 'echo "Ataque completado. Contenedor permanecerá activo."' >> /entrypoint.sh && \
    echo 'echo "Puedes ejecutar nuevamente: docker exec attacker-sim python simulate_attack.py"' >> /entrypoint.sh && \
    echo 'tail -f /dev/null' >> /entrypoint.sh && \
    chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
