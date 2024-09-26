FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    python3-pip \
    xvfb \
    libxi6 \
    default-jdk \
    fonts-liberation \
    libappindicator3-1 \
    libnss3 \
    lsb-release \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable && rm -rf /var/lib/apt/lists/*

ENV GOOGLE_CHROME_BIN=/usr/bin/google-chrome
RUN ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /app
RUN python3 --version

COPY requirements_test.txt /app/requirements.txt
RUN pip install -r requirements.txt --break-system-packages

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
