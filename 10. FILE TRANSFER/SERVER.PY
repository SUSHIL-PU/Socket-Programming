import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 2021
sock.bind((socket.gethostname(), port))
sock.listen(5)
print('Socket is waiting for client connection...')
while True:
    conn, addr = sock.accept()
    print('Connected to ' + str(addr))

    filename = input('Enter the filename to be sent    : ')
    fileToSent = open(filename, 'r')
    file_data = fileToSent.read(1024)
    conn.send(file_data.encode('utf-8'))
    print('File sent successfully')
    conn.close()
