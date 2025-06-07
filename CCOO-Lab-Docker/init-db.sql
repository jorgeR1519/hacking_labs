-- Este script se ejecuta al iniciar el contenedor para crear una base de datos de ejemplo
CREATE DATABASE labdb;

USE labdb;

-- Tabla de ejemplo para demostrar escalada de privilegios a través de credenciales en la DB
CREATE TABLE secretos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dato VARCHAR(255) NOT NULL
);

INSERT INTO secretos (dato) VALUES ('FLAG{este_es_el_flag}');

-- Creamos un usuario 'appuser' con contraseña 'apppass' con permisos limitados
CREATE USER 'appuser'@'%' IDENTIFIED BY 'apppass';
GRANT SELECT ON labdb.secretos TO 'appuser'@'%';
FLUSH PRIVILEGES;
