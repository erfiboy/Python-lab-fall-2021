import os
from socket import *
from pathlib import Path

file_path = os.path.abspath(os.path.dirname(__file__))

file_path += "/data.txt" 

serverName = '127.0.0.1'

serverPort = 8082

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

greeting = clientSocket.recv(1024)

f = open(file_path, "a")

f.write(greeting.decode())

f.close()

clientSocket.close()