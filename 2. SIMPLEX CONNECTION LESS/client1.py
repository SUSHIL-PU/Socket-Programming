import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((socket.gethostname(), 5000))


data, adr = s.recvfrom(1024)
print(data.decode(), adr) 
   
