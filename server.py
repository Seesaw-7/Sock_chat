import socket

server_address = ('localhost', 8888)


############# socket() to create a socket for the server ###############
# create a communication endpoint for the server

# If the server.py and client.py is run on the same machine, same host, it could use
# 1. AF_LOCAL, allowing communication between processes running on the same host, using file system paths as addresses instead of network addresses.
# 2. AF_INET, communicating between processes on different hosts connected by IPV4, with network protocols like TCP or UDP
# Others

# SOCK_STREAM for TCP and SOCK_DGRAM for UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


############# bind() to bind the socket to the server address and port number ###############
# Once the server socket is bound to the desired address, it will be able to accept incoming connections from clients attempting to connect to that address and port combination.
server_socket.bind(server_address)


############# listen() to to listen incoming client connection requests ###############
# 1 specifies the maximum numbter of pending connections that can be queued for acceptance
# the server socket will queue at most 1 pending connection.
server_socket.listen(1)
print('Server listening on {}:{}'.format(*server_address))


############# accept() to accpet a client connection ###############
client_socket, client_address = server_socket.accept()


############# read() from the clent and write() to the client ###############
# Receive data from the client
# the server will attempt to receive up to 1024 bytes of data from the client in a single call to recv()
# Note that 1024 is the bufSize. Did not find any info about its relationship with reciever window size
# I suppose that flow control should be handled by TCP instead of programmers. So, quite confused here.
# recv() blocks until it receives data or until the connection is closed (by the client? end of file notification sent by client? do not know because python socket api is too high level).


data = client_socket.recv(1024) # revised to recv(2) and only received "He"
print('Received data from client:', data.decode())   

#### The following code does not work. It does not end if client does not close connection
# received_data = b""

# while True:
#     print(1)
#     data = client_socket.recv(10)
#     print(data.decode())
#     if not data: # Connection closed by the client
#         break
#     received_data += data
    
# print('Received data from client:', received_data.decode())   


# Send a response back to the client
response = 'Hello from the server!'
client_socket.sendall(response.encode())

# The server actively close the connection 
client_socket.close() 
server_socket.close()
