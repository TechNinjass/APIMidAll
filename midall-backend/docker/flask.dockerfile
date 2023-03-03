FROM python:3.10.6-slim-buster

WORKDIR /flaskr/

COPY ./requirements.txt /flaskr/

WORKDIR /flaskr/

RUN pip install -r requirements.txt

CMD ["python", "-m", "flask", "run"]