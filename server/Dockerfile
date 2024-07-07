FROM python:3

WORKDIR /app
COPY . /app/

RUN apt update -y && apt install -y pipx
RUN pipx ensurepath

RUN pipx install poetry
ENV PATH="$PATH:/root/.local/bin"

RUN poetry install --no-root
CMD poetry run uvicorn main:app --host 0.0.0.0 --port 8080
EXPOSE 8080