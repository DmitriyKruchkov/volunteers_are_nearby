FROM python:3.11.9


COPY ./ ./volunteers_are_nearby
WORKDIR /volunteers_are_nearby
EXPOSE 5000
RUN pip install -r requirements.txt

CMD cd flaskr && python3 app.py





