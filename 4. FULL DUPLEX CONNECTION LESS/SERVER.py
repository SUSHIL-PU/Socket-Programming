import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((socket.gethostname(), 1039))
while True:
    data, addr = s.recvfrom(1024)
    print(data.decode())
    print(addr)

    Input = input('Enter the message to be send to the Client')
    msg = bytes(Input,"utf-8")
    s.sendto(msg, addr)
    
      