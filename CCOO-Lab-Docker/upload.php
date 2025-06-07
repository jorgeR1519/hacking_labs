<?php
// upload.php
// Permite al usuario subir un archivo PHP a /var/www/uploads

// Directorio de destino para los archivos subidos
$targetDir = __DIR__ . '/uploads/';

$message = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!isset($_FILES['file'])) {
        $message = 'No se recibió ningún archivo.';
    } else {
        $file = $_FILES['file'];

        // Verificamos si ocurrió algún error en la subida
        if ($file['error'] !== UPLOAD_ERR_OK) {
            $message = 'Error al subir el archivo: ' . $file['error'];
        } else {
            // Solo permitimos subir archivos con extensión .php
            $filename = basename($file['name']);
            $ext = strtolower(pathinfo($filename, PATHINFO_EXTENSION));
            if ($ext !== 'php') {
                $message = 'Solo se permiten archivos con extensión .php';
            } else {
                // Movemos el archivo a /var/www/uploads/
                $destination = $targetDir . $filename;
                if (move_uploaded_file($file['tmp_name'], $destination)) {
                    $message = "Archivo subido correctamente como: <strong>{$filename}</strong>";
                } else {
                    $message = 'No se pudo mover el archivo a la carpeta uploads.';
                }
            }
        }
    }
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Subir Web Shell</title>
</head>
<body>
    <h1>Sube tu propia web shell (.php)</h1>
    <?php if ($message): ?>
        <p><?php echo $message; ?></p>
    <?php endif; ?>
    <form action="upload.php" method="post" enctype="multipart/form-data">
        <label for="file">Selecciona un archivo .php:</label><br>
        <input type="file" name="file" id="file" accept=".php" required><br><br>
        <input type="submit" value="Subir">
    </form>
    <hr>
    <p>Una vez subido, puedes incluirlo mediante Path Traversal en <code>vuln.php</code>, por ejemplo:</p>
    <pre>
http://localhost:8080/vuln.php?page=../uploads/tu_shell_sin_extensión
    </pre>
    <p>(Recuerda NO poner “.php” en el parámetro <code>page</code>, porque <code>vuln.php</code> agrega “.php” automáticamente.)</p>
    <p><a href="index.php">Volver al índice</a></p>
</body>
</html>
