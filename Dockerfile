FROM python:3.6-alpine

RUN mkdir -p /app
WORKDIR /app
COPY . /app
RUN pip install -r requirments.txt
