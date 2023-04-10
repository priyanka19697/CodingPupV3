FROM python:3.10

ENV PYTHONBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

