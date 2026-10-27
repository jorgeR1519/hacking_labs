# PHP2Shell Lab — Apache / PHP en Docker

Entorno educativo con PHP real vulnerable y una referencia corregida para estudiar **PHP2Shell (CVE-2026-109618 y CVE-2026-109619)**. No sustituye estos fallos por un `eval()` ni por una inyección de comandos inventada.

## Alcance

| Servicio | Runtime | Dirección |
| --- | --- | --- |
| `vulnerable` | PHP 8.2.34 + Apache mod_php | http://127.0.0.1:8086 |
| `patched` | PHP 8.2.35 + Apache mod_php | http://127.0.0.1:8087 |

El proyecto PHP identifica 8.2.35 como versión corregida para ambos avisos. El laboratorio permite inspeccionar el runtime y observar errores de agotamiento de memoria (OOM). **No incluye una cadena RCE ni demuestra por sí mismo corrupción de memoria o explotación de los CVE.** El botón OOM es un ejercicio de manejo de errores en la aplicación; no reproduce necesariamente el contexto interno vulnerable.

Los puertos se publican únicamente en loopback y no se montan carpetas del equipo ni el socket Docker. Se utiliza una red bridge normal para permitir el acceso por los puertos publicados desde Docker Desktop; los contenedores pueden iniciar conexiones salientes. Cada servicio tiene límites de CPU, procesos y memoria. Utiliza un equipo de laboratorio; las imágenes contienen software deliberadamente antiguo.

## Requisitos y arranque

Docker Engine con Compose v2, o Docker Desktop en modo contenedores Linux. Python 3 es opcional para la verificación. La primera construcción necesita Internet para descargar las imágenes oficiales.

```bash
git clone https://github.com/jorgeR1519/hacking_labs.git
cd hacking_labs/php2shell
docker compose config
docker compose up --build -d --wait
docker compose ps
```

Si ya descargaste el repositorio, entra directamente a `php2shell`. Abre las dos direcciones de la tabla y compara versión, SAPI, límite de memoria y PID. No uses `php:latest`: eliminaría la referencia vulnerable.

## Práctica 1: inspeccionar el entorno

```bash
docker compose exec vulnerable php -v
docker compose exec patched php -v
docker compose exec vulnerable apache2ctl -M
```

La página usa el runtime web; `php -v` usa CLI. Para este laboratorio la página debe mostrar `apache2handler`. El servidor integrado `php -S` no reemplaza Apache mod_php.

## Práctica 2: provocar un OOM y analizar los logs

Pulsa el botón de la página o ejecuta:

```bash
curl -i -X POST http://127.0.0.1:8086/oom.php
curl -i -X POST http://127.0.0.1:8087/oom.php
docker compose logs --tail=100 vulnerable patched
```

En PowerShell utiliza `curl.exe` si `curl` es un alias de PowerShell.

El endpoint intenta reservar 32 MiB con `memory_limit=16M`. Busca la marca `PHP2SHELL_LAB controlled_oom` y el error de memoria correspondiente. Puede recibirse HTTP 500 o una interrupción de conexión; revisa después que la página siga disponible. Un único worker facilita correlacionar el PID, pero puede ser reemplazado al fallar.

**La versión corregida también debe rechazar la asignación:** corregir PHP2Shell no elimina el límite de memoria. Ni un HTTP 500 ni la recuperación del servicio permiten distinguir de forma concluyente un runtime vulnerable de uno corregido.

Verificación automatizada de versiones, configuración, petición OOM y recuperación:

```bash
python verify.py
```

El script solo contacta `127.0.0.1:8086` y `127.0.0.1:8087`, sin proxies, y realiza una petición OOM por servicio. No es un escáner de vulnerabilidades. Confirma manualmente los errores en los logs.

## Práctica 3: evaluar la corrección

Compara ambos servicios manteniendo la misma aplicación y configuración. Consulta los avisos oficiales para entender qué comportamiento interno corrige cada parche. La versión mostrada sirve para inventariar este laboratorio; en distribuciones con parches retroportados se debe consultar el aviso del proveedor.

Este entorno se centra en Apache mod_php. No afirma reproducir las condiciones particulares de PHP-FPM ni todas las variantes de ambos fallos. Un laboratorio de RCE completo requeriría una prueba específica, verificable y compatible con el binario y la arquitectura usados; aquí no se promete ese resultado.

## Apagar, limpiar y reconstruir

```bash
docker compose down --remove-orphans
docker compose build --pull
docker compose up -d --wait
```

No hay volúmenes persistentes. `down` elimina los contenedores y sus cambios; las imágenes permanecen en la caché Docker.

## Resolución de problemas

- **Puerto ocupado:** cambia solo el puerto del host en Compose y adapta las constantes del script si quieres usarlo. Conserva `127.0.0.1`.
- **No se encuentra una imagen:** comprueba acceso a Docker Hub y disponibilidad de `php:8.2.34-apache-bookworm` y `php:8.2.35-apache-bookworm`. No reemplaces silenciosamente versiones ni uses una imagen flotante.
- **Contenedor sin salud:** consulta `docker compose logs` y `docker compose ps` antes de continuar.
- **Healthy pero Windows no conecta:** el healthcheck se ejecuta dentro del contenedor y no verifica el puerto publicado en Windows. Si usabas la configuración anterior con `internal: true`, ejecuta `docker compose down --remove-orphans` y después `docker compose up --build -d --wait` para recrear la red bridge. Comprueba `docker compose ps` y `docker compose port vulnerable 80`; debe aparecer `127.0.0.1:8086`.
- **Build para otra arquitectura:** registra arquitectura y etiquetas de imagen al documentar resultados; el comportamiento de memoria puede variar.

## Estado de validación

Los archivos se prepararon el 27 de octubre de 2026. En el equipo de creación Docker y PHP no estaban disponibles: **la construcción, descarga de etiquetas y ejecución de los contenedores están pendientes de validación**. `verify.py` y los comandos anteriores permiten comprobarlos en un equipo con Docker. Las etiquetas fijan versiones, pero no digests; registra los digests después de una construcción validada si necesitas reproducibilidad binaria estricta.

## Referencias oficiales

- [PHP: RCE via OOM corruption — CVE-2026-109618](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w)
- [PHP: RCE via stale global state — CVE-2026-109619](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp)

Practica exclusivamente en este entorno o en sistemas para los que tengas autorización.
