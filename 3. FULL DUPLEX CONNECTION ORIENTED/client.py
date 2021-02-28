import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1027))

msg_ser = s.recv(1024)
print(msg_ser.decode())

Input = input('Enter the message to be sent to the Server')
message =  bytes(Input,"utf-8")
s.send(message)


