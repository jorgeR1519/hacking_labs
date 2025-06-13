# Laboratorio de Phishing Simulado - Telefónica

Este laboratorio tiene como objetivo simular un escenario realista de phishing, donde un atacante crea una página falsa de acceso a Jira para capturar credenciales de empleados. Está diseñado con fines educativos, para entrenar la capacidad de análisis, detección y respuesta ante este tipo de amenazas.

---

## 🧠 Descripción del escenario

Un atacante ha desplegado una página falsa de acceso a Jira. Los usuarios ingresan su usuario y contraseña creyendo que están accediendo al sistema real, pero las credenciales son capturadas y almacenadas por el atacante. El laboratorio está compuesto por tres contenedores:

- `phishing-page`: Página falsa que imita el acceso a Jira y captura credenciales.
- `jira-mock`: API simulada de Jira que permite el acceso a logs y tickets.
- `evidence-collector`: Contenedor que monitorea en tiempo real el archivo donde se almacenan las credenciales robadas.

---

## ⚙️ Requisitos

- [Podman](https://podman.io/)
- [podman-compose](https://github.com/containers/podman-compose)
- Sistema operativo Linux (recomendado Kali, Parrot, Ubuntu)

---

## 🚀 Cómo levantar el laboratorio

1. Clona este repositorio:

```bash
   git clone https://github.com/tu-usuario/Laboratorio_Telefonica.git
   cd Laboratorio_Telefonica
```

2. Levanta los servicios:

```bash
    podman-compose up --build 
```

3. Accede a la página de phishing desde tu navegador para enviar las credenciales:

```bash
http://localhost:8080   

```

## 🤖 Chat bot (opcional)

Este script (chat_bot.py) simula una conversación con un empleado ficticio que puede revelar información sensible si se le presiona con ciertas preguntas clave. Sirve como parte del entrenamiento para analizar técnicas de ingeniería social.

#  Cómo ejecutarlo

```bash
python3 chat_bot.py
```

| Entrada del usuario | Respuesta del bot                                    |
| ------------------- | ---------------------------------------------------- |
| `hola`              | ¿Qué quieres? / ¿Ahora qué pasa?                     |
| `quiero acceso`     | ¿Para qué lo quieres? / No sé si deba confiar en ti… |
| `credenciales`      | Te entrega las credenciales del sistema simulado     |
| `sistema crítico`   | Advierte sobre la importancia del sistema            |
| `gracias`           | Responde con sarcasmo o sorpresa                     |


Ejemplo:

```bash
Empleado>: ¿Qué quieres? (escribe 'salir' para terminar)
Tú: hola
Empleado>: ¿Ahora qué pasa?
Tú: quiero acceso
Empleado>: ¿Para qué lo quieres?
Tú: credenciales
Empleado>: Aquí tienes las credenciales: {"user":"juan@telefonica.es","pass":"Passw0rd!"}

```



##  🔍 Interacción con la API falsa de Jira
1. Obtener token válido:

```bash
curl -s -X POST http://localhost:3000/login \
  -H "Content-Type: application/json" \
  -d '{"user":"juan@telefonica.es","pass":"Passw0rd!"}'
```

2. Consultar logs:

``` bash
curl -s http://localhost:3000/logs \
  -H "Authorization: Bearer valid-token"
```


3. Consultar tickets:

``` bash
curl -s http://localhost:3000/tickets \
  -H "Authorization: Bearer valid-token"
```









🛡️ Advertencia
Este laboratorio simula técnicas utilizadas por actores maliciosos. Está destinado exclusivamente para entornos de laboratorio, propósitos académicos o pruebas de concienciación. No lo utilices en redes de producción ni contra usuarios reales.