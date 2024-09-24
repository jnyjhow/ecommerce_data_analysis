FROM selenium/standalone-chrome:latest

USER root

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/.venv
ENV PATH=/opt/.venv/bin:$PATH

WORKDIR /app
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./src/ws_amazon .
COPY ./drivers ./drivers

RUN chmod 775 -R drivers 

RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

CMD ["tail", "-f", "/dev/null"]
#CMD ["python", "app.py"]
