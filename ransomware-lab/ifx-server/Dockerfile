FROM httpd:2.4-alpine
# Fija un ServerName para suprimir la advertencia de nombre de dominio
RUN echo "ServerName localhost" >> /usr/local/apache2/conf/httpd.conf
# Copia el parche malicioso al directorio público del servidor HTTP
COPY patch.sh /usr/local/apache2/htdocs/patch.sh
