import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 2021
sock.connect((socket.gethostname(), port))
print('Connected with the server')

filename = input('Enter the name of the incoming file   :  ')
file_name = open(filename, 'w')
file_data = sock.recv(1024)
file_name.write(file_data.decode('utf-8'))
file_name.close()
print('File received')