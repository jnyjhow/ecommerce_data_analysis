FROM python:3.12-slim AS builder

RUN apt-get update && apt-get install -y \
    curl && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
#RUN pip install poetry

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes -f requirements.txt --output requirements.txt

FROM selenium/standalone-chrome:latest

USER root

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/.venv
ENV PATH=/opt/.venv/bin:$PATH

WORKDIR /app
RUN pip install --upgrade pip

#COPY requirements.txt .
COPY --from=builder /app/requirements.txt ./
RUN pip install -r requirements.txt

COPY ./src/ws_amazon .

RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

CMD ["tail", "-f", "/dev/null"]
#CMD ["python", "app.py"]
