# ================================== BUILDER ===================================
FROM python:3.10-slim-buster AS requirements-stage

ENV PYTHONUNBUFFERED=1

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


# =================================== SERVER ===================================
FROM python:3.10-slim-buster

WORKDIR /app

COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY backend ./

RUN which uvicorn

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--ssl-certfile", "localhost.crt", "--ssl-keyfile", "localhost.key"]

