import os
from socket import *
from pathlib import Path


file_path = os.path.abspath(os.path.dirname(__file__))

file_path += "/data.txt" 

serverName = '127.0.0.1'

serverPort = 8081

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

greeting = clientSocket.recv(1024)

print(greeting.decode())
while True:
    req = input("type exit to break the shell\n")
    if req == 'exit':
        break
    clientSocket.send(req.encode())
    resp = clientSocket.recv(1024)
    print(resp.decode())
    

clientSocket.close()