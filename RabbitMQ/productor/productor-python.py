#!/usr/bin/env python
import pika
import sys
import os

# Obtener las credenciales de las variables de entorno
user = os.getenv('RABBITMQ_USER')
password = os.getenv('RABBITMQ_PASS')

# Conectarse a RabbitMQ con las credenciales proporcionadas por las variables de entorno
credentials = pika.PlainCredentials(user, password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "Hola soy nueva"

channel.basic_publish(exchange='logs', routing_key='', body=message)
print(f" [x] Sent {message}")
connection.close()