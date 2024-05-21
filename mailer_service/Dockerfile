FROM python:3.12-alpine


COPY ./ ./mailer_service
WORKDIR /mailer_service
EXPOSE 5150
RUN python -m venv venv && pip install -r requirements.txt

CMD source venv/bin/activate && python3 main.py