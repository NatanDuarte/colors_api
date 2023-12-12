FROM python:3.11.7-slim

WORKDIR /app

RUN apt update && apt upgrade

RUN apt-get install ffmpeg libsm6 libxext6 -y \
    && pip install poetry

COPY . .

RUN apt-get -y install libc-dev \
    && apt-get -y install build-essential

RUN poetry install

EXPOSE 10001

CMD ["poetry", "run", "uvicorn", "colors_api.api:app", "--host", "0.0.0.0", "--port", "10001"]