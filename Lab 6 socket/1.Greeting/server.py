import os
from socket import *
 
serverPort = 8080

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))

serverSocket.listen(1)

connectionSocket, addr = serverSocket.accept()

message = "Hello my clinet"

connectionSocket.send(message.encode())

connectionSocket.close()

serverSocket.close()

