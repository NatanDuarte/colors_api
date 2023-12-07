FROM python:3.11.7-slim

WORKDIR /app

RUN apt update && apt upgrade
RUN pip install poetry

COPY . .

RUN apt-get -y install libc-dev
RUN apt-get -y install build-essential

RUN poetry install

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "--reload", "colors_api.api:app", "--port", "8000"]