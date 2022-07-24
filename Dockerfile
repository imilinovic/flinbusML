FROM python:3.10.5-bullseye

WORKDIR /app

COPY service /app/service
COPY model /app/model
COPY utils /app/utils
COPY weights /app/weights
COPY tmp /app/tmp
COPY dataset.yaml /app
COPY settings.py /app
COPY start.sh /app
COPY requirements.txt /app
COPY gunicorn_config.py /app

RUN pip install -U -r requirements.txt

RUN apt update
RUN apt install -y libgl-dev

ENTRYPOINT ./start.sh
