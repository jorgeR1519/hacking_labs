CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50),
  bio TEXT
);
INSERT INTO users (username, bio) VALUES
('admin', 'Administrador del sistema'),
('victim', '<script>alert("XSS")</script>');
