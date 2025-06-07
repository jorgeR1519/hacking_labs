# Dockerfile totalmente revisado
FROM ubuntu:16.04

ENV DEBIAN_FRONTEND=noninteractive

# 1) Instalar Apache, PHP (y su módulo para Apache), MariaDB, compiladores, etc.
RUN apt-get update && \
    apt-get install -y \
      apache2 \
      php7.0 \
      libapache2-mod-php7.0 \
      php7.0-mysql \
      mariadb-server \
      build-essential \
      git \
      vim \
      wget \
    && rm -rf /var/lib/apt/lists/*

# 2) Habilitar el módulo PHP para Apache
RUN a2enmod php7.0

# 3) Iniciar MariaDB, configurar root para mysql_native_password y rootpwd
#    de modo que luego www-data pueda conectar con contraseña.
RUN service mysql start && \
    mysql -e "USE mysql; \
             UPDATE user \
               SET plugin = 'mysql_native_password', \
                   Password = PASSWORD('rootpwd') \
             WHERE User = 'root' AND Host = 'localhost'; \
             DELETE FROM user WHERE User=''; \
             DROP DATABASE IF EXISTS test; \
             FLUSH PRIVILEGES;"

# 4) Copiar el script de inicialización de la BD
COPY init-db.sql /docker-entrypoint-initdb.d/

# 5) Crear carpeta de uploads dentro de DocumentRoot
RUN mkdir -p /var/www/html/uploads

# 6) Copiar la web vulnerable y el PoC
COPY index.php   /var/www/html/index.php
COPY upload.php  /var/www/html/upload.php
COPY vuln.php    /var/www/html/vuln.php
COPY exploit.c   /home/exploit/exploit.c

# 7) Ajustar permisos
RUN chown -R www-data:www-data /var/www/html && \
    chown -R www-data:www-data /var/www/html/uploads && \
    chmod 755 /home/exploit && \
    chmod 644 /home/exploit/exploit.c

# 8) Exponer HTTP
EXPOSE 80

# 9) Arrancar MySQL y Apache al levantar el contenedor
CMD service mysql start && service apache2 restart && tail -f /dev/null
