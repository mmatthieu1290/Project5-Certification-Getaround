FROM python:3.9-alpine

COPY . /app/

CMD python /app/app.py