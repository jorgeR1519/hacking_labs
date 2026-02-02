# ❄️ Caso Snowflake – Filtraciones masivas de datos (2024–2026)


## 🧠 Descripcion :


El incidente de seguridad relacionado con **Snowflake** consistió en el acceso no autorizado a cuentas de la plataforma utilizadas por diversas empresas globales. Los atacantes no vulneraron directamente la infraestructura de Snowflake, sino que explotaron credenciales comprometidas de usuarios que no contaban con mecanismos de autenticación **multifactor (MFA)**.


## 🧫 Requisitos Previos

- Docker 20.10 o superior
- Docker Compose 2.0 o superior
- Git (para clonar el repositorio)
- Python 3.11+ (opcional, para scripts locales)


## 🧪 Instalación

1. Clona el repositorio:

```bash
   git clone https://github.com/tu-usuario/snowflake-lab.git
   cd snowflake-lab
```


2. Verifica que tengas la estructura de directorios:

```
snowflake-lab/
├── docker-compose.yml
├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── attacker/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── attack_scripts/
│       └── simulate_attack.py
└── scripts/
    ├── init-db.sql
    └── generate-data.py
```

3. Construye y levanta las imágenes de Docker:


```bash

docker-compose build

docker-compose up -d

```


4. Accede a los servicios:

- Aplicación vulnerable: http://localhost:8080

- Panel de monitoreo (Grafana): http://localhost:3000 (usuario: admin, contraseña: admin)

- Base de datos: localhost:5432 (usuario: admin, contraseña: Admin123, base de datos: snowflake_sim)


## 🛠️ Realizacion del ataque manual 


1. Prueba de login sin MFA:

```bash

curl -X POST http://localhost:8080/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"Admin123"}'
```

2. Accede a datos sensibles (necesita cookie de sesión):

```bash
# Obtén la cookie de sesión
SESSION=$(curl -s -X POST http://localhost:8080/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"Admin123"}' -c - | grep session | awk '{print $NF}')

curl -X GET http://localhost:8080/data -H "Cookie: session=$SESSION"

```
Opción 3: Script Todo-en-Uno

```bash

# Descargar script de ejecución completa
curl -L https://raw.githubusercontent.com/tu-usuario/snowflake-lab/main/scripts/run_complete_attack.sh -o run_lab.sh
chmod +x run_lab.sh
./run_lab.sh
```

3. Accede directamente a la base de datos:

```bash

docker exec snowflake-db psql -U admin -d snowflake_sim -c "SELECT * FROM customer_data;"

```

## 🔍 Análisis Forense


1. Revisión de Logs

```bash
# Logs de la aplicación vulnerable
docker logs vulnerable-app | grep -i "SECURITY\|ERROR\|LOGIN"


# Logs del atacante
docker logs attacker-sim

# Logs de la base de datos
docker logs snowflake-db | tail -50

```


2. Análisis de la Base de Datos

```bash

# Ver tablas existentes
docker exec snowflake-db psql -U admin -d snowflake_sim -c "\dt"

# Revisar logs de seguridad
docker exec snowflake-db psql -U admin -d snowflake_sim -c "SELECT * FROM security_logs ORDER BY event_time DESC LIMIT 10;"

# Contar datos comprometidos
docker exec snowflake-db psql -U admin -d snowflake_sim -c "SELECT 'customer_data' as table, COUNT(*) as records FROM customer_data UNION ALL SELECT 'financial_records', COUNT(*) FROM financial_records;"

```


3. Reporte del Ataque

```bash

# Ver reporte generado
cat scripts/attack_report.json

# Formatear JSON
python -m json.tool scripts/attack_report.json
```

4. Dashboard de Monitoreo

```bash

# Acceder a Grafana
echo "Dashboard disponible en: http://localhost:3000"
echo "Usuario: admin"
echo "Contraseña: admin"

```