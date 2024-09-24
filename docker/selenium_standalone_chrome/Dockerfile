FROM selenium/standalone-chrome:latest

USER root

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

RUN python3 -m venv /opt/.venv
ENV PATH=/opt/.venv/bin:$PATH

WORKDIR /app
RUN pip install --upgrade pip

COPY requirements.txt /app/
RUN pip install -r requirements.txt
# RUN pip install selenium
# RUN pip install selenium --break-system-packages

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