FROM python:3.11-alpine


COPY ./ ./mailer_service
WORKDIR /mailer_service
EXPOSE 5150
RUN python -m venv venv && pip install -r requirements.txt && source venv/bin/activate

CMD python3 main.py