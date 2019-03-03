FROM alpine:3.5
RUN apk add --update py2-pip
RUN apk add --update bash

RUN pip install pika

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
ADD producer.py /usr/src/app

CMD ["python", "/usr/src/app/producer.py"]
