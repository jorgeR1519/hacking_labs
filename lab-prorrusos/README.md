# Laboratorio: Simulación de Ataques DDoS y Defacement

En marzo–abril 2025, ataques políticos-ideológicos alcanzaron sistemas municipales y consejerías vía grupos prorrusos usando DDoS y defacement elconfidencialdigital.com+2cibersafety.com+2channelpartner.es+2. 


---

## 🧠 Descripción del escenario

Este laboratorio simula un escenario de ciberataques político-ideológicos contra sistemas municipales, implementado totalmente en Docker para facilitar su despliegue y destrucción.



---

## ⚙️ Requisitos

- Docker

- Docker Compose

- Linux/Windows/macOS con terminal capaz de ejecutar comandos Docker

---

## 🚀 Cómo levantar el laboratorio

1. Clona o descarga este repositorio en tu máquina local. :

```bash
   git clone https://github.com/tu-usuario/lab-prorrusos.git
   cd lab-prorrusos/
```

2. Levanta los servicios:

```bash
     docker-compose up --build
```

3. Verifica que los contenedores estén "Up" :

```bash
    docker ps 

```

## 🎯 Descripción de los servicios
🧪 web1 (Flask en puerto 8081)

+ Sirve estáticos desde web1-flask/www/index.html

+ Acepta PUT / para sobrescribir el fichero index.html (simulación de defacement)

🧪 web2 (Nginx en puerto 8082)

+ Sirve estáticos desde web2-nginx/www/index.html

+ No acepta métodos PUT

🧪 attacker (Alpine en red interna)

+ Instala ab (ApacheBench) y curl

+ Ejecuta run_ddos.sh:

+ DDoS interno contra web1 y web2 usando ab

+ Espera y luego lanza curl -X PUT para aplicar defacement en web1

+ Verifica con un GET y deja el contenedor vivo para inspección




##  🔍 Validación de resultados


1. Antes del ataque:

+ Navega a http://localhost:8081 y http://localhost:8082 para ver las páginas originales.

2. Durante el ataque:

+ Observa los logs del contenedor attacker:

```bash

docker logs -f attacker
```

- Verás estadísticas de ab y la salida de curl (200 OK).

o tambien  veras en consola el ataque : 

```bash
attacker  | Iniciando DDoS interno contra web1 y web2…
web1      | 172.20.0.2 - - [24/Jun/2025 10:58:06] "GET / HTTP/1.0" 200 -
web1      | 172.20.0.2 - - [24/Jun/2025 10:58:06] "GET / HTTP/1.0" 200 -
web1      | 172.20.0.2 - - [24/Jun/2025 10:58:06] "GET / HTTP/1.0" 200 -
web1      | 172.20.0.2 - - [24/Jun/2025 10:58:06] "GET / HTTP/1.0" 200 -
web1      | 172.20.0.2 - - [24/Jun/2025 10:58:06] "GET / HTTP/1.0" 200 -
web1      | 172.20.0.2 - - [24/Jun/2025 10:58:06] "GET / HTTP/1.0" 200 -
web1      | 172.20.0.2 - - [24/Jun/2025 10:58:06] "GET / HTTP/1.0" 200 -
web1      | 172.20.0.2 - - [24/Jun/2025 10:58:06] "GET / HTTP/1.0" 200 -
web1      | 172.20.0.2 - - [24/Jun/2025 10:58:06] "GET / HTTP/1.0" 200 -
web1      | 172.20.0.2 - - [24/Jun/2025 10:58:06] "GET / HTTP/1.0" 200 -
```

+ DDOS a la we2 :

```bash
web2      | 172.20.0.2 - - [24/Jun/2025:11:00:27 +0000] "GET / HTTP/1.0" 200 267 "-" "ApacheBench/2.3" "-"
web2      | 172.20.0.2 - - [24/Jun/2025:11:00:27 +0000] "GET / HTTP/1.0" 200 267 "-" "ApacheBench/2.3" "-"
web2      | 172.20.0.2 - - [24/Jun/2025:11:00:27 +0000] "GET / HTTP/1.0" 200 267 "-" "ApacheBench/2.3" "-"
web2      | 172.20.0.2 - - [24/Jun/2025:11:00:27 +0000] "GET / HTTP/1.0" 200 267 "-" "ApacheBench/2.3" "-"
web2      | 172.20.0.2 - - [24/Jun/2025:11:00:27 +0000] "GET / HTTP/1.0" 200 267 "-" "ApacheBench/2.3" "-"
web2      | 172.20.0.2 - - [24/Jun/2025:11:00:27 +0000] "GET / HTTP/1.0" 200 267 "-" "ApacheBench/2.3" "-"
web2      | 172.20.0.2 - - [24/Jun/2025:11:00:27 +0000] "GET / HTTP/1.0" 200 267 "-" "ApacheBench/2.3" "-"

```

+ Defacement a la web1 y atque terminado : 

```bash
attacker  | Pausando otros 5s antes del defacement…
attacker  | Haciendo PUT de defacement a web1…
attacker  |   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
attacker  |                                  Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0* Host web1:80 was resolved.
attacker  | * IPv6: (none)
attacker  | * IPv4: 172.20.0.4
attacker  | *   Trying 172.20.0.4:80...
attacker  | * Connected to web1 (172.20.0.4) port 80
attacker  | * using HTTP/1.x
attacker  | > PUT / HTTP/1.1
attacker  | > Host: web1
attacker  | < 
attacker  | { [20 bytes data]
100   245  100    20  100   225    132   1488 --:--:-- --:--:-- --:--:--  1678
attacker  | * shutting down connection #0
attacker  | Defacement aplicado!Verificando con GET a web1…
attacker  |   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
attacker  |                                  Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0* Host web1:80 was resolved.
attacker  | * IPv6: (none)

100   225  100   225    0     0   5190      0 --:--:-- --:--:-- --:--:--  5921
attacker  | * shutting down connection #0
attacker  | Script terminado. Contenedor attacker seguirá vivo para inspección.

```

3.  Después del defacement:

+ Recarga http://localhost:8081 para ver "¡Este sitio ha sido defaced por Hackers Prorrusos!".

+ web2 (8082) permanece intacta.











🛡️ Advertencia
Este laboratorio simula técnicas utilizadas por actores maliciosos. Está destinado exclusivamente para entornos de laboratorio, propósitos académicos o pruebas de concienciación. No lo utilices en redes de producción ni contra usuarios reales.