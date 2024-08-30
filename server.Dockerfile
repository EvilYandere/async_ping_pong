FROM python:3.10-bullseye

RUN mkdir -p /app/log

WORKDIR /app

COPY app/server.py .
COPY app/logger.py .

CMD ["python", "server.py"]
