FROM ubuntu:latest
RUN apt update

# Install Python 3, Gunicorn.
RUN apt install -y python3 python3-pip gunicorn3

# Install dependencies.
RUN pip3 install flask flask-cors sentry-sdk[flask] redis 

# Copy files.
COPY app.py /
COPY config.py /

EXPOSE 8000

# Run app server.
CMD gunicorn3 -b 0.0.0.0:8000 app:app
