FROM python:3.10-slim
WORKDIR /app
RUN pip install asyncua
COPY server.py .
CMD ["python", "server.py"]
