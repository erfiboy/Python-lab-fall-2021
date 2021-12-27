import os
from socket import *

serverName = '127.0.0.1'

serverPort = 8080

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

greeting = clientSocket.recv(1024)

print(greeting.decode())

clientSocket.close()