## Workflow
![](https://media.geeksforgeeks.org/wp-content/uploads/20220330131350/StatediagramforserverandclientmodelofSocketdrawio2-448x660.png)

## Running
Start clients and the server as seperate processes and the processes will communicate.
A simple way would be start two terminals on the same machine and run `python3 server.py` and `python3 client.py` in each so that the behaviours of each process could be monitored seperately.

Alternatively, rename 'localhost' to the server's IP in both scripts and run `client.py` and `server.py` on different machines. `ping` the server's IP and `curl` the server's port to test.

## Later
chat app layer

buffer input



## References: 

https://docs.python.org/3/library/socket.html

https://realpython.com/python-sockets/?continueFlag=15c65df5e495a04816b3bfb2a052bc03

https://www.geeksforgeeks.org/socket-programming-cc/


