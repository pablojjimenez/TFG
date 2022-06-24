FROM python:3.8-slim AS base
FROM base AS builder
ARG port
ENV PORT=$port

RUN apt update && \
    apt install -y --no-install-recommends build-essential
RUN pip install poetry
RUN python -m venv /venv
COPY . /.

RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

ENV PATH="/venv/bin:$PATH"
EXPOSE $PORT
CMD uvicorn app:app --host 0.0.0.0 --port $PORT
