
# PHP2Shell — Matriz de análisis de parches

## 1. Objetivo

Analizar las correcciones de seguridad relacionadas con
CVE-2026-109618 y CVE-2026-109619 en PHP.

El laboratorio compara:

- PHP 8.2.34: versión anterior a las correcciones.
- PHP 8.2.35: versión que incorpora las correcciones.
- Apache 2.4.68 con mod_php.
- Docker como entorno de ejecución aislado.

## 2. Commit de seguridad identificado

Repositorio: php/php-src

Commit:
3584a98bda0f2c0d367255b046798b0d3a221a19

Título:
Avoid state corruption via bailout

URL:
https://github.com/php/php-src/commit/3584a98bda0f2c0d367255b046798b0d3a221a19

El mensaje del commit indica dos cambios principales:

1. Sustituir el mecanismo bailout durante OOM
   por UnwindExit.
2. Restablecer correctamente variables globales
   utilizadas durante la inicialización.

El commit identifica ambos CVE como corregidos.

## 3. Matriz de componentes

| Archivo | Responsabilidad | Área de análisis | Estado |
|---|---|---|---|
| Zend/zend_alloc.c | Administración de memoria | Tratamiento de OOM | Pendiente de análisis detallado |
| Zend/zend_execute_API.c | Gestión de ejecución | Recuperación del estado | Pendiente |
| Zend/zend_globals.h | Variables globales | Inicialización y restablecimiento | Pendiente |
| Zend/zend_hash.c | Tablas hash | Gestión de errores de asignación | Pendiente |
| Zend/tests/oom_after_main_script.phpt | Prueba de regresión | Funciones de cierre tras OOM | Identificada |
| Zend/tests/oom_error_get_last.phpt | Prueba de regresión | Estado del último error | Identificada |

Nota: los archivos fueron identificados en la
comparación de versiones y en el commit de seguridad.
La atribución de cambios específicos a cada CVE
requiere revisión adicional.

## 4. Análisis conceptual

### Antes de la corrección

El mecanismo de recuperación de ciertos errores
de memoria podía dejar estado interno inconsistente.

### Después de la corrección

El parche introduce cambios en la recuperación
de errores OOM y en el restablecimiento del estado
global del motor PHP.

### Limitaciones

Un HTTP 500 provocado por memory_limit no demuestra
corrupción de memoria ni explotación de un CVE.

## 5. Próximas investigaciones

- Revisar los cambios de zend_alloc.c.
- Estudiar el mecanismo UnwindExit.
- Examinar las pruebas de regresión oficiales.
- Documentar las diferencias confirmadas.
- Comparar los resultados con el laboratorio Docker.

## 6. Estado

Análisis inicial documentado.

No se ha demostrado divulgación de memoria,
corrupción de memoria ni ejecución remota de código.
