FROM python:3.10-slim-bullseye

RUN apt-get update  \
    && apt-get dist-upgrade -y \
    && apt-get install make -y \
    && apt-get install wget -y

WORKDIR /shopping-cart

COPY Makefile .
COPY requirements.txt .

RUN make setup

COPY src ./src/
COPY resources ./resources/
