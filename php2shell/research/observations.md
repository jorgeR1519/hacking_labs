
# PHP2Shell — Observaciones experimentales

## 1. Entorno de laboratorio

Sistema anfitrión:
Windows 11

Plataforma:
Docker

Servidor:
Apache 2.4.68 (Debian)

SAPI:
apache2handler

Versiones comparadas:

- PHP 8.2.34 — localhost:8086
- PHP 8.2.35 — localhost:8087

Configuración de memoria:
memory_limit = 16M

## 2. Verificación inicial

Comando:

py compare.py

Resultados:

[PASS] vulnerable: 8.2.34
[PASS] patched: 8.2.35

Informe generado:
reports/baseline.json

Ambos entornos superaron las seis comprobaciones
de configuración y funcionamiento.

Total:
12/12 comprobaciones superadas.

## 3. Persistencia de sesiones

Comando:

py test_sessions.py

Resultados:

PHP 8.2.34: PASS
PHP 8.2.35: PASS

Interpretación:

Ambas versiones conservan el estado de sesión
entre solicitudes HTTP cuando se reutiliza
la cookie PHPSESSID.

## 4. Prueba controlada de memoria

Comando:

py verify.py

Resultado PHP 8.2.34:

- HTTP 500 durante el ejercicio.
- Error fatal por agotamiento de memoria.
- HTTP 200 después del ejercicio.
- PID observado: 17.

Resultado PHP 8.2.35:

- HTTP 500 durante el ejercicio.
- Error fatal por agotamiento de memoria.
- HTTP 200 después del ejercicio.
- PID observado: 17.

## 5. Evidencias de logs

PHP 8.2.34:

Allowed memory size of 16777216 bytes exhausted
(tried to allocate 33554464 bytes)

PHP 8.2.35:

Allowed memory size of 16777216 bytes exhausted
(tried to allocate 33558528 bytes)

Ambos errores ocurrieron en:

/var/www/html/oom.php

Línea:
12

## 6. Interpretación

El ejercicio intenta reservar aproximadamente
32 MB bajo un límite de memoria de 16 MB.

Ambas versiones rechazan la asignación y
responden con HTTP 500.

Posteriormente, los servicios vuelven a
responder con HTTP 200.

Esto confirma el comportamiento controlado
de agotamiento de memoria y recuperación.

No confirma que el estado interno de PHP
esté libre de corrupción.

## 7. Matriz de resultados

| Prueba | PHP 8.2.34 | PHP 8.2.35 |
|---|---|---|
| Versión correcta | PASS | PASS |
| mod_php | PASS | PASS |
| Sesión activa | PASS | PASS |
| Persistencia de sesión | PASS | PASS |
| Error OOM | Confirmado | Confirmado |
| Recuperación HTTP | PASS | PASS |
| Explotación CVE | No demostrada | No demostrada |

## 8. Conclusión provisional

El laboratorio funciona correctamente como
entorno comparativo de versiones PHP.

Se han demostrado:

- Configuración correcta de ambos contenedores.
- Funcionamiento de sesiones PHP.
- Persistencia de sesiones.
- Errores controlados de memoria.
- Recuperación posterior del servicio.

No se han demostrado:

- Divulgación de direcciones de memoria.
- Corrupción del estado interno.
- Ejecución remota de comandos.
- Activación específica de los CVE.

## 9. Próximos pasos

1. Revisar los cambios oficiales de Zend.
2. Analizar el mecanismo UnwindExit.
3. Estudiar las pruebas de regresión.
4. Incorporar observaciones adicionales.
5. Elaborar un informe técnico final.
