require 'bunny'

# Conexión con el servidor RabbitMQ
connection = Bunny.new(hostname: "localhost")
connection.start

# Abre un canal
channel = connection.create_channel

# Se declara una cola llamada 'cola_ruby_mensajes'
queue = channel.queue('cola_ruby_mensajes')

# Mensaje a enviar
mensaje = "Hola desde Ruby"

# Enviar el mensaje a la cola
channel.default_exchange.publish(mensaje, routing_key: queue.name)

puts " [x] Enviado '#{mensaje}' desde Ruby"

# Cerrar la conexión
connection.close
