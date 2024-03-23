import pika
import sys

# Verificar si se proporciona un mensaje como argumento
if len(sys.argv) < 2:
    print("Por favor, proporciona un mensaje para enviar.")
    sys.exit(1)

# Obtener el mensaje de los argumentos de la línea de comandos
mensaje = ' '.join(sys.argv[1:])

# Establecer la conexión con el servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar una cola llamada 'cola_mensajes'
channel.queue_declare(queue='cola_mensajes')

# Enviar el mensaje proporcionado como argumento
channel.basic_publish(exchange='', routing_key='cola_mensajes', body=mensaje)

print(f" [x] Enviado '{mensaje}'")

# Cerrar la conexión
connection.close()
