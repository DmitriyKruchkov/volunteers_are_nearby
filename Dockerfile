FROM python:3.11.9-slim-bookworm


COPY ./ ./volunteers_are_nearby
WORKDIR /volunteers_are_nearby
EXPOSE 5000
RUN python3 -m venv venv \
    && ls -al \
    && source venv/bin/activate \
    && python3 -m pip install -r requirements.txt

CMD source venv/bin/activate && cd flaskr && python3 app.py





