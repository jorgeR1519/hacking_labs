<?php
include 'db.php';

// Vulnerabilidad SQLi: parámetro GET ?id=
$id = $_GET['id'] ?? '';

// Consulta sin sanitizar
$query = "SELECT id, username, bio FROM users WHERE id = '$id'";
$result = $conn->query($query);

?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>El Confidencial - Perfil de Usuario</title>
</head>
<body>
    <h1>Perfil</h1>
    <?php if ($row = $result->fetch_assoc()): ?>
        <p><strong>ID:</strong> <?= htmlspecialchars($row['id']) ?></p>
        <p><strong>Usuario:</strong> <?= htmlspecialchars($row['username']) ?></p>
        <p><strong>Bio:</strong> <?= $row['bio'] /* XSS vulnerable */ ?></p>
    <?php else: ?>
        <p>Usuario no encontrado.</p>
    <?php endif; ?>

    <h2>Lista de Usuarios</h2>
    <?php include 'templates/user_list.php'; ?>
</body>
</html>
