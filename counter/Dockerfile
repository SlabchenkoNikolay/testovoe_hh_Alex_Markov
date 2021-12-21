FROM python:latest

WORKDIR /counter

COPY ./requirements.txt .

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

