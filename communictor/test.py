from communictor import Client, Server
from communictor.utils import crypt_decrypt

# create instances
client = Client(17, 2)
server = Server(23, 4)

# create prime and send it to server
prime = client.generate_prime()
server.get_prime(prime)
print(f'Prime on client: {client.prime}; Prime on server: {server.prime}')

# create base and send it to server
base = client.generate_base()
server.get_base(base)
print(f'Base on client: {client.base}; Base on server: {server.base}')

# generate numbers to send from client and server
client_number = client.generate_local_secret()
server_number = server.generate_local_secret()

# get secret numbers from server and client
client.get_secret(server_number)
server.get_secret(client_number)

print(f'Client number is: {client_number}; Server number is: {server_number}')
print(f'Shared secret is: {client.secret} <->  {server.secret}')

initial_string = 'Text to send to server'
enc = crypt_decrypt(initial_string, client.secret)
print(enc)
dec = crypt_decrypt(enc, server.secret)
print(dec)

encrypted_text=client.encrypt(initial_string)
print(encrypted_text)

decrypted_text=server.decrypt(encrypted_text)
print(decrypted_text)