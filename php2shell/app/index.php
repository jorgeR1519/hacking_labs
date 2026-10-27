<?php
declare(strict_types=1);

$info = [
    'lab' => 'php2shell-lab',
    'php' => PHP_VERSION,
    'sapi' => PHP_SAPI,
    'pid' => getmypid(),
    'memory_limit' => ini_get('memory_limit'),
    'session_upload_progress' => ini_get('session.upload_progress.enabled'),
    'patched_baseline' => version_compare(PHP_VERSION, '8.2.35', '>='),
];
if (($_GET['format'] ?? '') === 'json') {
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode($info, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
    exit;
}
header('Content-Type: text/html; charset=utf-8');
?>
<!doctype html>
<html lang="es">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PHP2Shell · laboratorio</title>
<style>
body{font:18px/1.6 system-ui;background:#101822;color:#dce8f2;max-width:850px;margin:60px auto;padding:24px}
h1{color:#7cdbba}pre{background:#1d2b3a;padding:20px;overflow:auto}button{padding:12px;font:inherit;cursor:pointer}a{color:#7cdbba}
</style>
<h1>PHP2Shell · laboratorio Docker</h1>
<p>Comparación de PHP vulnerable y corregido con Apache mod_php.</p>
<pre><?= htmlspecialchars(json_encode($info, JSON_PRETTY_PRINT), ENT_QUOTES, 'UTF-8') ?></pre>
<p>El ejercicio provoca un error de memoria controlado. Un error 500 o un cambio de PID no demuestra corrupción de memoria ni ejecución remota de código.</p>
<form method="post" action="oom.php"><button>Ejecutar ejercicio OOM local</button></form>
<p>Consulta los logs y vuelve a <a href="/">comprobar el servicio</a> después del ejercicio.</p>
</html>
