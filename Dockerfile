FROM tiangolo/uvicorn-gunicorn:python3.8-slim

LABEL maintainer="https://github.com/rodrigoarenas456"

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive
ENV MODULE_NAME=app

ADD requirements.txt .

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache

COPY . .
