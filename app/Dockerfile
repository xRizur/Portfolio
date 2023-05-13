#Using the python alpine image
FROM python:alpine

ENV CONTAINER_HOME=/var/www

ADD . $CONTAINER_HOME

WORKDIR $CONTAINER_HOME

RUN pip install -r $CONTAINER_HOME/requirements.txt