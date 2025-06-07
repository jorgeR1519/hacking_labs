<?php
// vuln.php
// Vulnerable a Path Traversal: incluye archivos arbitrarios según ?page=...
if (isset($_GET['page'])) {
    $page = $_GET['page'];
    $file = __DIR__ . '/' . $page;

    if (file_exists($file)) {
        include($file);
    } else {
        // Intentamos incluir fuera de webroot (realpath)
        $fileOutside = realpath(__DIR__ . '/' . $page . '.php');
        if ($fileOutside && file_exists($fileOutside)) {
            include($fileOutside);
        } else {
            echo "<pre>Archivo no encontrado: $file</pre>";
        }
    }
} else {
    echo "<pre>Parámetro 'page' no provisto.</pre>";
}
?>
