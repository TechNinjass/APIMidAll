FROM python:3.10.6-slim-buster

WORKDIR /flaskr/

COPY ./requirements.txt /flaskr/

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

CMD ["python", "-m", "flask", "run","--host=0.0.0.0","--port=5000" ]

