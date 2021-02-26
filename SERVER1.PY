import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print(socket.gethostname())
s.bind((socket.gethostname(), 1026))
s.listen(5)
while True:
    clt, addr = s.accept()
    print(f'connection to {addr} established')
    Input = input('Enter your message to be sent to the user ')
    clt.send(bytes(Input,"utf-8")) 
    clt.close()
    

  