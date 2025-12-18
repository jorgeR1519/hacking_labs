# 🧪 React2Shell Lab (Simulado)

Repositorio dedicado al almacenamiento de **laboratorios prácticos de ciberseguridad ofensiva**, enfocados en técnicas y vectores de ataque utilizados en escenarios reales.  
Cada laboratorio está diseñado para ser **reproducible**, **controlado** y **ético**, usando principalmente **Docker**.

---

## 📌 Descripción del laboratorio

Este laboratorio simula un escenario inspirado en **React Server Components (RSC)** y ataques de tipo **React2Shell / XSS → Exfiltration**, permitiendo analizar:

- Flujo de datos no confiables
- Abuso de renderizado del lado servidor
- Exfiltración de información mediante payloads JavaScript
- Detección y análisis forense de payloads maliciosos

⚠️ **Nota:**  
Este laboratorio **NO ejecuta código malicioso real**. Todo el comportamiento es **simulado** con fines educativos.

---

## 🧱 Arquitectura del laboratorio

El entorno se compone de **dos contenedores Docker**:

### 🔴 Vulnerable App (Simulada)
- Node.js + Express
- Expone un endpoint que **registra payloads**
- Emula un endpoint RSC vulnerable
- Guarda los datos recibidos para análisis

### 🟢 Exfil Server
- Python + Flask
- Simula un servidor atacante
- Recibe datos exfiltrados vía `fetch()` o peticiones GET
- Guarda la información recibida en archivos JSON


## 🚀 Puesta en marcha

### 📦 Requisitos
- Docker
- Docker Compose
- Linux (probado en Kali Linux)

### ▶️ Levantar el laboratorio

```bash
docker compose up --build
```

### ▶️  Servicios expuestos:

- Vulnerable App → http://localhost:8080

- Exfil Server → http://localhost:9000


### 📂 Ver datos exfiltrados

```bash
docker exec -it r2s_exfil ls /app/received

docker exec -it r2s_exfil cat /app/received/exfil_XXXX.json
```

# 🕵️‍♂️ Objetivos de aprendizaje

- Comprender riesgos en flujos RSC

- Analizar exfiltración vía JavaScript

- Practicar análisis forense de payloads

- Diseñar detecciones y mitigaciones

- Aprender a construir laboratorios Docker ofensivos


## 🔐 Uso ético

Este laboratorio fue creado exclusivamente para fines educativos.
No debe usarse contra sistemas reales sin autorización expresa.