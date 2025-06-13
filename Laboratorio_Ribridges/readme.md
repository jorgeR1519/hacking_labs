# RIBridges Realistic Hacking Lab

Este laboratorio simula una brecha de seguridad realista en el portal RIBridges (Rhode Island), incluyendo un ataque de phishing a empleados de Deloitte, autenticación sin MFA y exfiltración de datos sensibles.

## Estructura del proyecto

```
/ribridges-realistic-lab
├── Dockerfile
├── docker-compose.yml
├── init.sh              # Script de inicialización
├── init-db.js           # Crear base de datos SQLite
├── vendor-auth.js       # Servicio de autenticación (phishing + /auth)
├── portal-api.js        # API de RIBridges simulada (/residents)
├── phishing-email.html  # Página de phishing
└── package.json
```

## Requisitos

- **Docker** o **Podman** con soporte Compose
- Node.js (para editar/inspeccionar, pero no necesario para ejecutar)
- `curl` para probar los endpoints

## 1. Configuración del entorno

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/ribridges-realistic-lab.git
   cd ribridges-realistic-lab
   ```
2. Crea la base de datos y dependencias:
   ```bash
   npm install
   ```

## 2. Levantar los servicios

Con Docker Compose:

```bash
docker-compose up --build
```

Con Podman Compose:

```bash
podman-compose up --build
```

Verás en los logs:

```
DB initialized
Vendor Auth running on 3000
DB initialized
Portal API running on 3001
```

## 3. Flujo del ataque paso a paso

### 3.1 Phishing de credenciales

1. Abre el navegador en:\
   `http://localhost:3000`
2. Verás el formulario de phishing. Ingresa:
   - **Usuario:** `deloitte_user`
   - **Contraseña:** `Deloitte#123`
3. Haz clic en **Ingresar**. Deberías ver `Credenciales recibidas.`

### 3.2 Obtener token de autenticación

En otra terminal ejecuta:

```bash
curl -X POST http://localhost:3000/auth
```

Recibirás un JSON con el token, por ejemplo:

```json
{"token":"ZGVsb2l0dGVfdXNlcjpEZWxvaXR0ZSMxMjM="}
```

### 3.3 Acceso y exfiltración de datos

Usa el token para llamar al endpoint vulnerable:

```bash
curl -H "Authorization: Bearer ZGVsb2l0dGVfdXNlcjpEZWxvaXR0ZSMxMjM=" \
     http://localhost:3001/residents
```

Respuesta esperada:

```json
[
  {"name":"Alice Johnson","ssn":"123-45-6789","bank_account":"1111222233334444"},
  {"name":"Bob Smith","ssn":"987-65-4321","bank_account":"4444333322221111"}
]
```

En los logs del servicio verás:

```
Exfiltrated: [ ... ]
```

## 4. Detener y limpiar

Para parar los contenedores:

```bash
# Docker
docker-compose down
# Podman
podman-compose down
```

Limpiar pods, contenedores y redes (solo Podman):

```bash
podman pod prune --force
podman ps -a | grep ribridges | awk '{print $1}' | xargs podman rm -f
podman network prune --force
```

## 5. Extensiones sugeridas

- Añadir **MFA** en `/auth`.
- Introducir un IDS (e.g. Suricata) entre redes `vendor_net` y `portal_net`.
- Implementar firma HMAC en el token.
- Analizar tráfico con Wireshark.

---

*Desarrollado por Jorge Enrique Renteria Mosquera | Proyecto educativo de ciberseguridad*

