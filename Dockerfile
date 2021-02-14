# FROM tiangolo/uvicorn-gunicorn:python3.6-alpine3.8

# RUN pip install --no-cache-dir fastapi

FROM python:3
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./ /code