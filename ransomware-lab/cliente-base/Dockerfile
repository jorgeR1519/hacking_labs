FROM alpine:3.18
RUN apk add --no-cache curl openssl mailx
WORKDIR /data
# Archivos de ejemplo
RUN echo "info pública" > doc1.txt
RUN echo "procesos judiciales" > doc2.txt
COPY startup.sh /usr/local/bin/startup.sh
RUN chmod +x /usr/local/bin/startup.sh
CMD ["/usr/local/bin/startup.sh"]
