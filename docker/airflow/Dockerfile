FROM apache/airflow:2.10.2

USER root

RUN apt-get update && apt-get install -y \
    curl \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry install --no-root

COPY src/ws_mercado_livre /opt/airflow/ws_mercado_livre
COPY src/ws_amazon /opt/airflow/ws_amazon
COPY ./drivers /opt/airflow/drivers
RUN chmod 775 -R /opt/airflow/drivers 

#USER airflow
