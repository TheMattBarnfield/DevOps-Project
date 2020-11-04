FROM python:3.9.0-slim-buster as base

EXPOSE 5000

RUN apt-get update \
    && apt-get install -y curl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /app
COPY . .

RUN poetry install

FROM base as prod

ENTRYPOINT poetry run gunicorn --bind 0.0.0.0:5000 "app:create_app(None)"

FROM base as dev

ENTRYPOINT poetry run flask run --host=0.0.0.0