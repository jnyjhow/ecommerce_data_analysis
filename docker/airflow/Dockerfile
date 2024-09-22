FROM apache/airflow:2.10.2

USER root

RUN apt-get update && apt-get install -y \
    curl

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry install --no-root

COPY src/ws_mercado_livre /opt/airflow/ws_mercado_livre
USER airflow
