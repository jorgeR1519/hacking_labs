<?php
// Vulnerabilidad XSS en listado
$users = $conn->query("SELECT id, username FROM users");
echo '<ul>';
while($u = $users->fetch_assoc()) {
    // Link con parámetro sin sanitizar
    echo "<li><a href=\"?id={$u['id']}\">{$u['username']}</a></li>";
}
echo '</ul>';
?>
