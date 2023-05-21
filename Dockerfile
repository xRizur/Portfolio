FROM python:3.7-slim

ENV CONTAINER_HOME=/var/www

COPY app $CONTAINER_HOME/
COPY requirements.txt $CONTAINER_HOME/

WORKDIR $CONTAINER_HOME

RUN pip install -r requirements.txt