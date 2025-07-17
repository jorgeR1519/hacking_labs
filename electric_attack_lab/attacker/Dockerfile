FROM kalilinux/kali-rolling

# Instala Nmap, Metasploit y Python venv
RUN apt update && apt install -y \
    nmap \
    metasploit-framework \
    python3-venv \
    python3-pip \
  && rm -rf /var/lib/apt/lists/*

# Crea un venv en /opt/venv e instala librerías dentro de él
RUN python3 -m venv /opt/venv \
 && /opt/venv/bin/pip install --upgrade pip \
 && /opt/venv/bin/pip install requests pymodbus asyncua

# Asegura que usamos ese venv por defecto
ENV PATH="/opt/venv/bin:${PATH}"

# Copia y da permiso al entrypoint
COPY entrypoint.sh /entrypoint.sh
COPY attack.py /attack.py
RUN chmod +x /entrypoint.sh attack.py

ENTRYPOINT ["/entrypoint.sh"]
