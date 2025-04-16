FROM python:3.12-slim

COPY . /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV AM_I_IN_A_DOCKER_CONTAINER 1

COPY requirements.txt .

RUN mkdir -p /app/logs
RUN pip install --no-cache-dir -r requirements.txt
VOLUME /app/logs
CMD [ "python3","main.py"]