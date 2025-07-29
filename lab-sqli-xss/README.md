# 🧪 SQLi + XSS Lab – El Confidencial (Abril 2024)

Este laboratorio reproduce un entorno vulnerable a **inyección SQL (SQLi)** y **Cross-Site Scripting (XSS)** como el descrito en [tresmares.com](https://tresmares.com/principales-ciberataques-en-espana-durante-el-2024/).

## 🔍 Descripción del ataque

- **Vector:** Parámetro `id` en una URL no sanitizada.
- **Técnica:** Inyección SQL + inyección de scripts (XSS) vía campo `bio`.
- **Impacto:** Exposición de datos, ejecución de scripts en cliente.
- **Resultado:** Simulación de fallo de sanitización en CMS.


---

## ⚙️ Requisitos

- Docker
- Docker Compose

---

## 🚀 Instalación

```bash
# Clona el repositorio o descarga el proyecto
git clone https://github.com/tuusuario/lab-sqli-xss.git
cd lab-sqli-xss

# Borra base de datos previa si deseas reiniciar
rm -rf data/mysql

# Levanta el entorno
docker-compose up --build -d

```

Accede en tu navegador a:

- 🌐 http://localhost:8080 → Web vulnerable

- 🔐 http://localhost:8081 → PhpMyAdmin (usuario: root, pass: rootpass)

---


# 🛠️ Pruebas de vulnerabilidad


## 🔍 Inyección SQL (SQLi)

URL:

```bash

http://localhost:8080/?id=1' OR '1'='1

```

## 🔸 Cross-Site Scripting (XSS)

URL:

```bash
http://localhost:8080/?id=2

```

# 👨‍💻 Créditos
Basado en un incidente ficticio del CMS de El Confidencial (abril 2024).
Laboratorio desarrollado para prácticas educativas de ciberseguridad ofensiva.