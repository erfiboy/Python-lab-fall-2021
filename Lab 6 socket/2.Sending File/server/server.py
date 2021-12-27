import os
from socket import *
from pathlib import Path

file_path = os.path.abspath(os.path.dirname(__file__))

file_path += "/data.txt"

data = "" 

f = open(file_path, "r")

data = f.read()

f.close()
  
serverPort = 8082

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))

serverSocket.listen(1)

connectionSocket, addr = serverSocket.accept()

connectionSocket.send(data.encode())

connectionSocket.close()

serverSocket.close()