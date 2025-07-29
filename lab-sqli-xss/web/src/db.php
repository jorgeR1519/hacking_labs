<?php
$host = 'db';
$user = 'vulnuser';
$pass = 'vulnpass';
$db   = 'elconfidencial';
$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}
?>
