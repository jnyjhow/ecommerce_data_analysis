FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    xvfb

# RUN apt-get update && \
#     apt-get install -y wget xvfb apt-transport-https ca-certificates curl gnupg --no-install-recommends && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

RUN Xvfb :99 & \
    export DISPLAY=:99

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -f -y && \
    rm google-chrome-stable_current_amd64.deb

#CMD ["google-chrome", "--version"]
#CMD echo "Google Chrome version: $(google-chrome --version)"

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry install --no-root

COPY ./src/ws_amazon /app/
COPY ./drivers /app/drivers

RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

CMD ["tail", "-f", "/dev/null"]
#CMD ["poetry", "run", "python", "app.py"]
