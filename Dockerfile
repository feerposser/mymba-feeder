FROM python:3.7

LABEL MAINTAINER = "Fernando Posser Pinheiro | feerposser"

ENV PYTHONBUFFERED 1
ENV DEBUG 0
ENV DATABASE_NAME mymbafeederdb
ENV DATABASE_USER root
ENV DATABASE_PASSWORD root
ENV DATABASE_HOST mysql
ENV DATABASE_PORT 3306

WORKDIR /app

COPY . /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt