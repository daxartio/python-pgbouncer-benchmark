FROM python:3.10-slim

RUN pip install poetry && poetry config virtualenvs.create false

WORKDIR /opt/app

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry install
