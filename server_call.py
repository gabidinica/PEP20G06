from communictor import Server
from communictor import Client

server = Server("localhost", 8080)
client=Client("localhost",8080)

print(server.prime)
print(server.base)
server.start()
client.start()
