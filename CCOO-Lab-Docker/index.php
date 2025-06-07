<?php
// index.php
// Página principal que enlaza a las funciones disponibles
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Laboratorio Path Traversal (Upload)</title>
</head>
<body>
    <h1>Lab: Path Traversal + Upload</h1>
    <p>Bienvenido. Usa las siguientes opciones:</p>
    <ul>
        <li><a href="upload.php">Subir tu propia web shell (o cualquier PHP)</a></li>
        <li><a href="vuln.php?page=home">Explorar Path Traversal</a></li>
        <li>Prueba de Path Traversal, por ejemplo: <code>?page=../../etc/passwd</code> o <code>?page=../uploads/nombre_de_tu_shell</code></li>
    </ul>
</body>
</html>
