import os
import psutil
import socket

server_address = ('localhost', 8888)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)
print('Server listening on {}:{}'.format(*server_address))
client_socket, client_address = server_socket.accept()

def child_process():
    while True:
        data = client_socket.recv(1024)
        if not data:
            exit()
        print("Friend said: ",data.decode())
    

def main(): 
    child_pid = os.fork()
    
    if child_pid == 0: # running in the child process.
        child_process()
    else: # running in the parent process.
        while True:
            msg = input("You said: ")
            client_socket.send(msg.encode())
            if msg == "bye":
                child = psutil.Process(child_pid)
                child.terminate()
                break
        os.wait()  # Wait for the child process to finish.

if __name__ == "__main__":
    main()

client_socket.close() 
server_socket.close()
