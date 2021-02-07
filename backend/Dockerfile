FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3 python3-pip curl

# Install dependencies.
COPY requirements.txt /
RUN pip3 install -r requirements.txt

# Copy files.
COPY app.py /
COPY config.py /

EXPOSE 8000

# Healthcheck
HEALTHCHECK CMD curl --fail http://127.0.0.1:8000/status || exit 1  

# Run app server.
CMD gunicorn -b 0.0.0.0:8000 app:app
