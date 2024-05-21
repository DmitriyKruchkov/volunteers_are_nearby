FROM python:3.12


COPY ./ ./mailer_service
WORKDIR /mailer_service
EXPOSE 5150
RUN python -m pip install --no-cache-dir poetry==1.8.2 \
    && poetry config virtualenvs.in-project true \
    && poetry install --only main --no-interaction --no-ansi --no-root

CMD python3 main.py