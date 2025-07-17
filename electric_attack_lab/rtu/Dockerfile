FROM python:3.10-slim
WORKDIR /app

# Instala la versión 2.5.3 de pymodbus para mantener el módulo sync
RUN pip install pymodbus==2.5.3

COPY modbus_rtu.py .
CMD ["python", "modbus_rtu.py"]

