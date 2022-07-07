FROM python:3.8-slim

ARG port
ARG host
ARG workers

ENV PORT=$port
ENV HOST=$host
ENV WORKERS=$workers

RUN apt update && \
    apt install -y --no-install-recommends build-essential
RUN pip install poetry

COPY config/*.py ./config/
COPY graphql_services/*.py ./graphql_services/
COPY data/*.csv ./data/
COPY managers/*.py  ./managers/
COPY models/*.py ./models/
COPY models/openapi_models/*.py ./models/openapi_models/
COPY repositories/*.py ./repositories/
COPY services/*.py ./services/
COPY poetry.lock pyproject.toml app.py ./

RUN poetry export -f requirements.txt | /bin/pip install -r /dev/stdin

ENV PATH="/venv/bin:$PATH"
CMD uvicorn app:app --host $HOST --port $PORT --workers $WORKERS
