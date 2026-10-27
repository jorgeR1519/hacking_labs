### Análisis del tratamiento OOM en PHP 8.2.35

El análisis de `Zend/zend_alloc.c` identificó dos mecanismos de recuperación ante errores de memoria.

- **Con contexto de ejecución:** PHP utiliza `zend_throw_unwind_exit()` para iniciar la salida mediante una excepción interna.
- **Sin contexto de ejecución:** PHP utiliza `zend_bailout()` para abortar la solicitud.

Además, el parche restaura `EG(current_execute_data)`, limpia `EG(opline_before_exception)` y actualiza el estado del error OOM.

**Conclusión:** PHP 8.2.35 modifica el tratamiento de los errores de memoria para reducir el riesgo de inconsistencias internas. Las pruebas realizadas en el laboratorio todavía no demuestran explotación de los CVE.