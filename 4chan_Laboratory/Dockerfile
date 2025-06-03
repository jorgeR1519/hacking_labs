FROM ubuntu:14.04

RUN apt-get update && apt-get install -y \
    ghostscript \
    netcat \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY process.sh /process.sh
COPY fake.pdf /fake.pdf

CMD ["sh", "/process.sh"]
