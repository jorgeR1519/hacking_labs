 # Laboratorio de Escalada de Privilegios y Explotación de Vulnerabilidades 🧪 

⚠️ Este laboratorio es una prueba de concepto educativa inspirada en el incidente de CCOO España. Está destinado exclusivamente para fines de aprendizaje y concienciación en seguridad informática.

# 📌 Descripción
Este laboratorio proporciona un entorno vulnerable que simula escenarios reales de escalada de privilegios y explotación de vulnerabilidades. Los participantes podrán practicar técnicas como:

Ejecución remota de comandos (RCE) a través de una webshell PHP.

Acceso a bases de datos MySQL con credenciales almacenadas en texto plano.


#  🧰 Tecnologías Utilizadas
 - Docker: Para la creación y gestión de contenedores.

- Ubuntu 16.04: Sistema operativo base del contenedor.

- Apache2 y PHP 7.0: Servidor web y lenguaje de scripting.

- MariaDB: Sistema de gestión de bases de datos.


# 🚀 Instalación y Ejecución

## 1.Clonar el repositorio:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

## 2.Construir la imagen de Docker:

```bash
docker build -t lab-escalada .
```

## 3.Ejecutar el contenedor:

```bash
docker run --privileged -p 8080:80 --name lab-escalada -d lab-escalada
```

## 4.Acceder al laboratorio:

Abre tu navegador y navega a http://localhost:8080.



# 📜 Licencia
Este proyecto se distribuye bajo la licencia MIT.

# ⚠️ Advertencia
Este laboratorio está diseñado exclusivamente con fines educativos y de concienciación en seguridad informática. No debe ser utilizado para actividades maliciosas o no autorizadas. El autor no se hace responsable del uso indebido de este laboratorio.