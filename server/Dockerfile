FROM python:3.9-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD waitress-serve --host 0.0.0.0 --port 5000 --expose-tracebacks app:app