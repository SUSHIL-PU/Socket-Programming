import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

Input = input('Enter the message to be sent to the Server')
message = bytes(Input,"utf-8")
s.sendto(message, (socket.gethostname(), 1039))
msg, addr = s.recvfrom(1024)
print(msg.decode()) 
print(addr)
s.close()    
    