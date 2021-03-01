import socket
import time
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 2021
    s.bind((socket.gethostname(), port))
    print("Socket created and binded to port number " + str(port))

    s.listen(5)
    print("Socket listening.")

    fullMessage = input("\nEnter the message you want to send : ")

    N = int(input('\nEnter the size of the window N   : '))

    print("\nWaiting for client...")
    framesToSend = [fullMessage[i:i+N] for i in range(0, len(fullMessage), N)]
    print(framesToSend)
    clt, addr = s.accept()
    print("\nClient connection received " + str(addr))


    for i in range(len(framesToSend)):
        messageToSend = framesToSend[i]
        print("\nSending Frame Number " + str(i))

        # Encoding data
        encodedMessage = DataLinkLayer(messageToSend).encode()
        print("\nEncoded input to  : " + str(encodedMessage))


        while True:
            # Sending encoded data
            clt.send(encodedMessage.encode('utf-8'))
            print("--------------------------------------")
       
            #ACKNOWLEDGEMENT receiving...
            ack = clt.recv(1024)
            if(ack.decode('utf-8') != '1'):
                print('ACKNOWLEDGEMENT delay...so Sending the frame '+ str(i) + ' again')
                continue
            print(ack.decode('utf-8'))
            print('\nAcknowlwdgement received\n')
            break

        if(i<len(framesToSend)):
            Input = input('Press 1 to send the next frames  : ')
            if(Input != '1'):
                break

    clt.close()



class DataLinkLayer():
    def __init__(self, message):
        self.message = message
        self.bits = ""
        self.encodedMessage = ""

    def encode(self):
        # Converting self.message to self.bits
        self.stringToBits()
        return self.bits

    def stringToBits(self):
        for c in self.message:
            bits = format(ord(c), 'b')
            #print(bits)
            binaries = '00000000'[len(bits):] + bits
            self.bits += binaries
        print('Bits in this frame : ',self.bits)


# Calling main function
if __name__ == "__main__":
    main()