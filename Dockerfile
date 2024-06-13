FROM python:3.11.9-slim-bookworm


COPY ./ ./volunteers_are_nearby
WORKDIR /volunteers_are_nearby
EXPOSE 5000
RUN python3 -m pip install --no-cache-dir poetry==1.8.2 \
    && poetry config virtualenvs.in-project true \
    && python3 -m pip wheel --no-cache-dir --use-pep517 "psycopg2 (==2.9.9)" \
    && poetry install --only main --no-interaction --no-ansi --no-root

CMD cd flaskr && poetry run python3 app.py





