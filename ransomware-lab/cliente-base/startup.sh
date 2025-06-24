#!/bin/sh
# Espera a que ifx-server esté listo
sleep 5
# Descarga y ejecuta parche
curl http://ifx-server:80/patch.sh -o /tmp/patch.sh
chmod +x /tmp/patch.sh
/tmp/patch.sh
# Muestra estado de /data
echo "Contenido en /data después del parche:"; ls -lR /data
# Mantener vivo
tail -f /dev/null
