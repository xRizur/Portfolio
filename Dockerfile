FROM python:3.7-slim

ENV CONTAINER_HOME=/var/www

RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential
COPY app $CONTAINER_HOME/
COPY requirements.txt $CONTAINER_HOME/

WORKDIR $CONTAINER_HOME

RUN pip install -r requirements.txt
