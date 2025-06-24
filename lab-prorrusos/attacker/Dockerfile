FROM alpine:latest
RUN apk add --no-cache curl apache2-utils

COPY run_ddos.sh /opt/run_ddos.sh
COPY defaced.html  /opt/defaced.html
RUN chmod +x /opt/run_ddos.sh

# Ejecutamos el script, y luego mantenemos vivo el contenedor
ENTRYPOINT ["/bin/sh", "/opt/run_ddos.sh"]
