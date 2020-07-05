FROM python:3.7-slim

RUN mkdir /app

WORKDIR /app

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
