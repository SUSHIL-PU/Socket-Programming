import socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 2021

try:
    clientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = clientSocket.recv(1024)
print(Response.decode())

while True:
    Input = input("Say something\n")
    clientSocket.send(str.encode(Input))
    response = clientSocket.recv(1024)
    print(response.decode("utf-8"))
clientSocket.close()