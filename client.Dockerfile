FROM python:3.10-bullseye

RUN mkdir -p /app/log

WORKDIR /app

COPY app/client.py .
COPY app/logger.py .

CMD ["python", "client.py"]
