FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /opt/api

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY . /opt/api/

RUN poetry install
CMD ["/bin/bash", "-cxv", "poetry install && gunicorn api.main:app -w 4 -k uvicorn.workers.UvicornWorker"]
