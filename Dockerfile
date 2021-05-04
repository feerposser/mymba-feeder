FROM python:3.7

LABEL MAINTAINER = "Fernando Posser Pinheiro | feerposser"

ENV PYTHONBUFFERED 1
ENV DATABASE_NAME mymbafeeder
ENV DATABASE_USER root
ENV DATABASE_PASSWORD example
ENV DATABASE_HOST mongo
ENV DATABASE_PORT 27017

WORKDIR /app

COPY . /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt