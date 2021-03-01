import socket
import time
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 2021
    s.connect((socket.gethostname(), port))
    
    # Getting received message from server
    binarybit = ""
    i = 0
    while True:
        receivedMessage = s.recv(1024)
        if(receivedMessage.decode('utf-8')==''):
            break
        print('Received frame : ' + receivedMessage.decode('utf-8'))
        binarybit = binarybit + str(receivedMessage.decode('utf-8'))

        #sending the ACKNOWLEDGEMENT...
        ack = 'ACK NUMBER ' + str(i)
        s.send(ack.encode('utf-8'))
        i = i + 1

    s.close()

    print('\n...Decoding the frames...\n')

    FullFrame = [binarybit[i:i+8] for i in range(0, len(binarybit), 8)]
    message = ''
    for frame in FullFrame:
        #Convert to base 2 decimal integer
        deciFrame = int(frame, 2)
        ascii_character = chr(deciFrame)
        message = message + ascii_character
    print(message)


# Calling main function
if __name__ == "__main__":
    main()