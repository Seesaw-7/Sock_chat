import socket, time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8888)

client_socket.connect(server_address) # This procedure contains underlying TCP three way handshake

message = 'Hello from the client!'
client_socket.send(message.encode())

response = client_socket.recv(1024)
print('Received response from server:', response.decode())

client_socket.close()
