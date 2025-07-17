
# Laboratory SCADA/ICS Attack Simulation


🧪El 28 de abril de 2025 se produjo un apagón masivo en la península ibérica como consecuencia de una caída súbita de 15 000 MW en apenas 5 segundos, lo que provocó la interrupción del suministro eléctrico a gran escala en España y Portugal. Este evento, sin precedentes en la región, afectó servicios esenciales, transporte, comunicaciones y redes industriales.🔐🛠️


## ⚙️ Requisitos

+ Docker y Docker Compose instalados.
+ Acceso a terminal Bash.


## 🚀 Cómo levantar el laboratorio

1. Clona el repositorio:

```bash
    git clone  https://github.com/tu-usuario/Laboratorio_Telefonica.git
    cd electric_attack_lab
```

2. Construye y levanta todos los servicios:

```bash
    docker-compose up --build -d
```

3.Verifica que los contenedores estén "Up":

```bash
    docker-compose ps
```

4. Abre la interfaz SCADA (Node-RED) en tu navegador:

```bash
    http://localhost:1880
```

5.Desde el contenedor atacante, escanea y valida:

```bash
    docker exec -it attacker bash
    nmap -sS -sV -Pn -p 502,4840,1880,8080 rtu opcua scada c2
```

6. Observa el ataque automático con logs:

```bash
    docker logs -f attacker
```



## 🤖 Detalles de los servicios

- scada: Node-RED con flujos para HTTP POST /inject.

- opcua: Servidor OPC UA simulado. Variable Voltage en ns=2;i=1.

- rtu: Servidor Modbus/TCP, registro 0 leído/escrito.

- c2: Servidor Flask que recibe beacons y responde comandos.

- attacker: Contenedor atacante con Python, nmap, pymodbus, asyncua, requests.


## 🛠️ Scripts de ataque
1. attack.py: realiza en bucle cada 10s:

+ Sobreescribe el registro 0 del RTU (Modbus).

+ Modifica la variable Voltage del OPC UA.

+ Dispara flujo en SCADA vía HTTP POST.

+ Envía beacon al C2.

En consola se vera asi :

```bash
docker logs -f attacker

[*] Iniciando ataque automático cada 10s
[*] Modbus: escribiendo 0 en registro 0
[*] OPC UA: valor actual 400.0, escribiendo 350.0
[*] SCADA: POST /inject → 200
[*] C2 beacon → {'cmd': 'sleep 10'}
[*] Modbus: escribiendo 0 en registro 0
[*] OPC UA: valor actual 350.0, escribiendo 300.0
[*] SCADA: POST /inject → 200
[*] C2 beacon → {'cmd': 'sleep 10'}
[*] Modbus: escribiendo 0 en registro 0
[*] OPC UA: valor actual 300.0, escribiendo 250.0
[*] SCADA: POST /inject → 200
[*] C2 beacon → {'cmd': 'sleep 10'}
[*] Modbus: escribiendo 0 en registro 0
```


## 🛡️ Advertencia

Este laboratorio simula técnicas utilizadas por actores maliciosos. Está destinado exclusivamente para entornos de laboratorio, propósitos académicos o pruebas de concienciación. No lo utilices en redes de producción ni contra usuarios reales.