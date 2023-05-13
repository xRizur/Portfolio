#Using the python alpine image
FROM python:3.7-slim

ENV CONTAINER_HOME=/var/www

ADD app $CONTAINER_HOME

WORKDIR $CONTAINER_HOME

CMD ["ls", "-la"]
RUN pip install -r $CONTAINER_HOME/requirements.txt