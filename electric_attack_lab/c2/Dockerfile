FROM python:3.10-slim
WORKDIR /app
RUN pip install flask
COPY c2_server.py .
CMD ["python", "c2_server.py"]
