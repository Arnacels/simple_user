FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY ./app ./
RUN python -m pip install -r requirements.txt
ENV PYTHONPATH=/app