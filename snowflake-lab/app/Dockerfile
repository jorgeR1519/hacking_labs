FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Vulnerabilidad deliberada: credenciales en código
ENV DB_PASSWORD="Admin123"
ENV API_KEY="SNOWFLAKE_SIM_2024_KEY"

EXPOSE 8080

CMD ["python", "app.py"]
