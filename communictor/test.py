from communictor.comm import Client, Server

client = Client(17, 2)
server = Server(23, 4)

prime = client._prime()
server.get_prime(prime)

client.generate_local_secret()
server.generate_local_secret()

server.get_secret(client.local)
client.get_secret(server.local)

print('Client secret: ', client.secret)
print('Server secret: ', server.secret)

print('Client local: ', client.local)
print('Server local: ', server.local)

print('Client dist: ', client.secret1)
print('Server dist: ', server.secret1)



