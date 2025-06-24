FROM python:3.11-alpine

WORKDIR /app

# Instala Flask
RUN pip install --no-cache-dir flask

# Copiamos la app y la web
COPY app.py .
COPY www ./www

EXPOSE 80
CMD ["python", "app.py"]
