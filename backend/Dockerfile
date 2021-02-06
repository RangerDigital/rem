FROM ubuntu:latest

RUN apt update
RUN apt install -y python3 python3-pip

# Install dependencies.
COPY requirements.txt /
RUN pip3 install -r requirements.txt

# Copy files.
COPY app.py /
COPY config.py /

EXPOSE 8000

# Run app server.
CMD gunicorn -b 0.0.0.0:8000 app:app
