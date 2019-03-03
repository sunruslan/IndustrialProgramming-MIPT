#!/usr/bin/env python
import pika
import sys
from time import sleep
import datetime


sleep(30)

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672))
channel = connection.channel()

channel.queue_declare(queue='randomNumbersQueue')

def callback(ch, method, properties, body):
    print('Consumer received number {} at {}'.format(body, datetime.datetime.now().time()))

channel.basic_consume(callback, queue='randomNumbersQueue', no_ack=True)

try:
    while True:
        channel.start_consuming()
finally:
    channel.stop_consuming()
