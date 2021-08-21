FROM python:3.9.4-slim

RUN mkdir /server && apt-get update && pip install poetry && poetry config virtualenvs.create false
WORKDIR /server

COPY ./server/pyproject.toml /server/
COPY ./server/poetry.lock /server/

RUN poetry install

COPY ./server /server
