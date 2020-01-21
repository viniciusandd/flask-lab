FROM python:3.8.1-alpine3.11

ENV FLASK_APP=app/app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

RUN pip install flask

WORKDIR /var/www/app

EXPOSE 5000

CMD flask run -h 0.0.0.0 -p 5000