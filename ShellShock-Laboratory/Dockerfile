FROM debian:jessie

ENV DEBIAN_FRONTEND=noninteractive

# Repos viejos para Jessie
RUN echo "deb http://archive.debian.org/debian jessie main contrib non-free" > /etc/apt/sources.list && \
    echo "deb http://archive.debian.org/debian-security jessie/updates main contrib non-free" >> /etc/apt/sources.list && \
    apt-get -o Acquire::Check-Valid-Until=false -o Acquire::AllowInsecureRepositories=true update && \
    apt-get -o Acquire::Check-Valid-Until=false -o Acquire::AllowInsecureRepositories=true install -y --allow-unauthenticated \
        apache2 curl wget build-essential git

# Descarga y compila bash vulnerable 4.3
RUN cd /tmp && \
    wget http://ftp.gnu.org/gnu/bash/bash-4.3.tar.gz && \
    tar xzf bash-4.3.tar.gz && \
    cd bash-4.3 && \
    ./configure && make && make install

# Verifica versión vulnerable
RUN bash --version

# Habilitar módulo CGI
RUN a2enmod cgi

# Crear script vulnerable en /usr/lib/cgi-bin
RUN echo '#!/bin/bash\n\
echo "Content-type: text/plain"\n\
echo\n\
echo "Shellshock test CGI"\n\
env\n\
' > /usr/lib/cgi-bin/test.sh && chmod +x /usr/lib/cgi-bin/test.sh

# Puerto
EXPOSE 80

CMD ["apache2ctl", "-D", "FOREGROUND"]
