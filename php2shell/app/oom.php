<?php
declare(strict_types=1);

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    header('Allow: POST');
    exit('Utiliza POST para ejecutar el ejercicio local.');
}
error_log('PHP2SHELL_LAB controlled_oom begin pid=' . getmypid());
// Asignacion fija: supera los 16 MiB del laboratorio, sin parametros externos.
// Es un ejercicio de manejo de errores, no una cadena de explotacion de los CVE.
$buffer = str_repeat('L', 32 * 1024 * 1024);
http_response_code(500);
exit('Configuracion inesperada: la asignacion debia exceder memory_limit.');
