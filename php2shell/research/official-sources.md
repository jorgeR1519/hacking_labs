
# PHP2Shell — Fuentes oficiales

## 1. Repositorio principal

Proyecto:
PHP Interpreter

Repositorio:
https://github.com/php/php-src

## 2. Vulnerabilidades estudiadas

### CVE-2026-109618

Aviso de seguridad:
https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w

Tema de investigación:
Recuperación de errores de memoria y estado
interno del motor PHP.

### CVE-2026-109619

Aviso de seguridad:
https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp

Tema de investigación:
Estado global y referencias de memoria durante
la recuperación de errores.

## 3. Corrección oficial

Commit:
3584a98bda0f2c0d367255b046798b0d3a221a19

https://github.com/php/php-src/commit/3584a98bda0f2c0d367255b046798b0d3a221a19

Título:
Avoid state corruption via bailout

El mensaje del commit menciona expresamente
CVE-2026-109618 y CVE-2026-109619.

## 4. Comparación de versiones

PHP 8.2.34 frente a PHP 8.2.35:

https://github.com/php/php-src/compare/php-8.2.34...php-8.2.35

## 5. Registro de cambios

PHP 8.2.35 NEWS:

https://github.com/php/php-src/blob/php-8.2.35/NEWS

Fecha de publicación indicada:
22 de octubre de 2026.

El registro confirma la incorporación de las
correcciones de ambos CVE.

## 6. Pruebas oficiales identificadas

- Zend/tests/oom_after_main_script.phpt
- Zend/tests/oom_error_get_last.phpt
- Zend/tests/oom_str_repeat.phpt
- Zend/tests/oom_request_parsing.phpt

Estas pruebas forman parte de los cambios
observados en el repositorio.

No se ha confirmado todavía cuáles son suficientes
para demostrar individualmente la corrección
de cada CVE.

## 7. Criterios de investigación

Cada conclusión debe distinguir entre:

- Información confirmada por fuentes oficiales.
- Resultados observados en Docker.
- Interpretaciones técnicas.
- Comportamientos todavía no demostrados.

No debe afirmarse explotación exitosa sin
evidencia reproducible que la respalde.
