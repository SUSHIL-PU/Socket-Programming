import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1027))
s.listen(5)
while True:
    client, addr = s.accept()
    print(f'Connected to {addr}')

    Input = input('Enter the message to be sent to the client')
    msg = bytes(Input,"utf-8")
    client.send(msg)
    
    clt_msg = client.recv(1024)
    print(clt_msg.decode())

    client.close() 