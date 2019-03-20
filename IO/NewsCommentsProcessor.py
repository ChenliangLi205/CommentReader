import socket

class Receiver(object):
    def __init__(self):
        self.mailBox = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def ReceivLetters(self, ipAddr, port):
        try:
            self.mailBox.bind((ipAddr, port))
        except:
            print("binding %s:%d failed" % (ipAddr, port))
        else:
            self.mailBox.listen(1)
            postMan, addr = self.mailBox.accept()
            letters = []
            while True:
                letter = postMan.recv(1024)
                if not letter:
                    break
                letters.append(letter.decode("utf-8"))
                postMan.sendall(b"You can send letters now")
            self.mailBox.close()
            return letters
