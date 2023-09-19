FROM python:3.11.4

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && pip install --upgrade --no-cache-dir pip \
    && pip install --no-cache-dir poetry

COPY ./pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

RUN apt-get install curl

COPY ./ ./
RUN chmod 777 ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]