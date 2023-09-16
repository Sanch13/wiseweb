FROM python:3.11.5-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /wiseweb

COPY /wiseweb /wiseweb

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
