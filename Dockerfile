FROM python:3.12-alpine


COPY ./ ./volunteers_are_nearby
WORKDIR /volunteers_are_nearby
EXPOSE 5000
RUN python -m pip install --no-cache-dir poetry==1.8.2 \
    && poetry config virtualenvs.in-project true \
    && poetry install --only main --no-interaction --no-ansi --no-root

CMD cd flaskr && poetry run python3 app.py





