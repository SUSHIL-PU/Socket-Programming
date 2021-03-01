import socket
from _thread import *

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 2021
threadCount = 0

try:
    serverSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print("Waiting for connection")
serverSocket.listen(5)


def client_thread(connection):
    msg = bytes("from Server side message","utf-8")
    connection.send(msg)
    while True:
        data = connection.recv(2048)
        print(data.decode('utf-8'))
        reply = "hello I am server : " + data.decode("utf-8")
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()



while True:
    client, addr = serverSocket.accept()
    print("Connected to "+ addr[0] + " "+ str(addr[1]))
    start_new_thread(client_thread,(client,))
    threadCount+=1
    print(" ThreadNumber" + str(threadCount)) 

serverSocket.close()

 
