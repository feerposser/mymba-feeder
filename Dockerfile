FROM python:3.7

LABEL MAINTAINER = "Fernando Posser Pinheiro | feerposser"

ENV PYTHONBUFFERED 1
ENV DATABASE_NAME mymbafeeder
ENV DATABASE_USER root
ENV DATABASE_PASSWORD example
ENV DATABASE_HOST mongo
ENV DATABASE_PORT 27017

WORKDIR /opt/mymbafeeder

COPY . /opt/mymbafeeder

# install dependencies
RUN pip install -e .