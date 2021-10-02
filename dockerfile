FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /opt/api

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml /opt/api
COPY poetry.lock /opt/api

RUN poetry install