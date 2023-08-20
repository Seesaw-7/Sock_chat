import socket

server_address = ('localhost', 8888)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(server_address)

server_socket.listen(1)
print('Server listening on {}:{}'.format(*server_address))

client_socket, client_address = server_socket.accept()

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(data.decode())

client_socket.close() 
server_socket.close()
