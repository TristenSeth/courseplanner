# syntax=docker/dockerfile:1
FROM python:3.9-alpine3.14

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 5000
CMD [ "python3", "-m", "flask", "run" ]