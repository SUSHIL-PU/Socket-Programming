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

    print("\nWaiting for client...")
    framesToSend = [fullMessage[i:i+4] for i in range(0, len(fullMessage), 4)]
    print(framesToSend)
    clt, addr = s.accept()
    print("\nClient connection received " + str(addr))

    delay = 0.5
    #delay is the delay time, means within 0.5 sec of time receiver has to ACK back.

    for i in range(len(framesToSend)):
        messageToSend = framesToSend[i]
        print("\nSending Frame Number " + str(i))

        # Encoding data
        encodedMessage = DataLinkLayer(messageToSend).encode()
        print("\nEncoded input to  : " + str(encodedMessage))


        while True:
            # Sending encoded data
            clt.send(encodedMessage.encode('utf-8'))

            #time1 is the time when message is sent.
            sendTime = time.time()
            print('sending time  : ' + str(sendTime))

            print("--------------------------------------")
       
            #ACKNOWLEDGEMENT receiving...
            ack = clt.recv(1024)
            receiveTime = time.time()
            print('REceived Time  : ' + str(receiveTime))
            if((sendTime + delay) < receiveTime):
                print('ACKNOWLEDGEMENT delay...so Sending the frame '+ str(i) + ' again')
                continue
            print(ack.decode('utf-8'))
            print('\nAcknowlwdgement received\n')
            break

        if(i<len(framesToSend)):
            Input = input('Press 1 to send the next frame   : ')
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