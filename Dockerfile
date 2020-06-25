FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./app /app