FROM python:3.11.3-slim-buster

COPY main.py app/
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install Flask

ENTRYPOINT ["python3", "main.py"]
