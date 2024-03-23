import pika

# Establecer la conexión con el servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar una cola llamada 'cola_ruby_mensajes'
channel.queue_declare(queue='cola_ruby_mensajes')

print(' [*] Esperando mensajes. Para salir, presione CTRL+C')

# Callback para procesar los mensajes recibidos
def callback(ch, method, properties, body):
    print(" [x] Recibido '{}' desde Python".format(body.decode()))

# Suscribirse a la cola y procesar los mensajes recibidos
channel.basic_consume(queue='cola_ruby_mensajes', on_message_callback=callback, auto_ack=True)

# Comenzar a escuchar los mensajes
channel.start_consuming()
