FROM python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

CMD FLASK_APP=app python -m flask run --host=0.0.0.0