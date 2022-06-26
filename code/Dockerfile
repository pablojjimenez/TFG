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

COPY . /.

RUN poetry export -f requirements.txt | /bin/pip install -r /dev/stdin

ENV PATH="/venv/bin:$PATH"
CMD uvicorn app:app --host 0.0.0.0 --port $PORT --workers $WORKERS
