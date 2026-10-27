<?php
declare(strict_types=1);

session_start();

$_SESSION['visitas'] = ($_SESSION['visitas'] ?? 0) + 1;

header('Content-Type: application/json; charset=utf-8');

echo json_encode([
    'php' => PHP_VERSION,
    'sapi' => PHP_SAPI,
    'session_active' => session_status() === PHP_SESSION_ACTIVE,
    'session_cookie_name' => session_name(),
    'visitas' => $_SESSION['visitas'],
], JSON_PRETTY_PRINT);
