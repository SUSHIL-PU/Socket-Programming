import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
   Input = input('Enter the message to be sent to the client')
   msg = bytes(Input,"utf-8")
   s.sendto(msg, (socket.gethostname(),5000))

