ARG PHP_VERSION=8.2.34
FROM php:${PHP_VERSION}-apache-bookworm

COPY config/lab.ini /usr/local/etc/php/conf.d/zz-lab.ini
COPY config/prefork.conf /etc/apache2/mods-available/mpm_prefork.conf
COPY app/ /var/www/html/
RUN php -l /var/www/html/index.php && php -l /var/www/html/oom.php

HEALTHCHECK --interval=10s --timeout=3s --start-period=10s --retries=5 \
  CMD php -r '$r = @file_get_contents("http://127.0.0.1/?format=json"); exit($r === false ? 1 : 0);'
