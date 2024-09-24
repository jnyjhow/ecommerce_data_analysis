FROM python:3.12-slim
#python:3.12-slim-bullseye

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    xvfb

RUN Xvfb :99 & \
    export DISPLAY=:99

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -f -y && \
    rm google-chrome-stable_current_amd64.deb

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt
#RUN pip install selenium

COPY ./src/examples/selenium_example.py /app/selenium_example.py
COPY ./drivers /app/drivers
RUN chmod 775 -R drivers 

RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#CMD ["python3", "selenium_example.py"]
#python3 selenium_example.py
CMD ["tail", "-f", "/dev/null"]
