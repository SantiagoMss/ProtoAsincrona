require 'bunny'

# Conexión con el servidor RabbitMQ
connection = Bunny.new(hostname: "localhost")
connection.start

# Abre un canal
channel = connection.create_channel

# Se declara una cola llamada 'cola_mensajes'
queue = channel.queue('cola_mensajes')

puts ' [*] Esperando mensajes. Para salir, presione CTRL+C'

begin
  # Suscribirse a la cola y procesar los mensajes recibidos
  queue.subscribe(block: true) do |delivery_info, properties, body|
    puts " [x] Recibido '#{body}' desde Ruby"
  end
rescue Interrupt => _
  connection.close
  exit(0)
end
