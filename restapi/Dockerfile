FROM python:3.8.1-alpine3.11

ENV FLASK_APP=restapi/app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

WORKDIR /var/www/app

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess -m flask run -h 0.0.0.0 -p 5000