FROM python:3.8.1-alpine3.11

ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

RUN pip install flask ptvsd

WORKDIR /var/www/app

EXPOSE 5000

CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess -m flask run -h 0.0.0.0 -p 5000