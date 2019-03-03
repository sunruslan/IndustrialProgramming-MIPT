#!/usr/bin/env python
import pika
from time import sleep
import random
import datetime


sleep(30)

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672))
channel = connection.channel()

channel.queue_declare(queue='randomNumbersQueue')

random.seed(100)

try:
    while True:
    	randomNumber = random.randint(1, 10000)

    	channel.basic_publish(exchange='', routing_key='randomNumbersQueue',
            body=str(randomNumber))
        print("Number {} has been sent at {}".format(randomNumber, datetime.datetime.now().time()))

        sleep(random.randint(1,50))
finally:
    connection.close()
