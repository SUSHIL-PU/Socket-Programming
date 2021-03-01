import socket
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 2021
    s.bind((socket.gethostname(), port))
    print("Socket created and binded to port number " + str(port))

    s.listen(5)
    print("Socket listening.")

    fullMessage = input("\nEnter the message you want to send : ")

    print("\nWaiting for client...")
    framesToSend = [fullMessage[i:i+4] for i in range(0, len(fullMessage), 4)]

    c, addr = s.accept()

    for i in range(len(framesToSend)):
        messageToSend = framesToSend[i]
        print("\nSending Frame Number " + str(i))
        print("\nClient connection received " + str(addr))

        # Encoding data
        encodedMessage = DataLinkLayer(messageToSend).encode()
        print("\nEncoded input to  : " + str(encodedMessage))

        # Sending encoded data
        c.send(encodedMessage.encode('utf-8'))

        print("--------------------------------------")
    c.close()



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