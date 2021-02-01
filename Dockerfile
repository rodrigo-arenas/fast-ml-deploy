FROM tiangolo/uvicorn-gunicorn:python3.8-slim

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive
ENV MODULE_NAME=app
ENV GRACEFUL_TIMEOUT=3800
ENV TIMEOUT=3800

ADD requirements.txt .

RUN apt-get update && apt-get install --no-install-recommends --yes gnupg \
    gcc \
    g++ \
    && apt-get clean \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache

COPY . .
