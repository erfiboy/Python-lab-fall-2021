import os
from socket import *

import _thread
from time import sleep

def server(connectionSocket, addr, data1, data2):
    greeting_message = "welcome which file do you want?(data1, data2)"
    connectionSocket.send(greeting_message.encode())
    possible_awnser = ['data1','data2']
    while True:
        req = connectionSocket.recv(1024).decode()
        if not req:
            break
        elif req not in possible_awnser:
            resp = "bad request only data1 and data2"
            connectionSocket.send(resp.encode())
            connectionSocket.send(greeting_message.encode())
            sleep(1)
        else:
            if req == 'data1':
                connectionSocket.send(data1.encode())
                break
            else:
                connectionSocket.send(data2.encode())
                break
            
    connectionSocket.close()
            

file_path = os.path.abspath(os.path.dirname(__file__))

file_path1 = file_path + "/data1.txt"
file_path2 = file_path + "/data2.txt"

f = open(file_path1, "r")
data1 = f.read()
f.close()
  
f = open(file_path2, "r")
data2 = f.read()
f.close()  
  
serverPort = 8080
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen()

while(1):
    connectionSocket, addr = serverSocket.accept()

    _thread.start_new_thread(server, (connectionSocket, addr, data1, data2))


serverSocket.close()