import socket

class PostMan(object):
    def __init__(self):
        self.mailBox = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def PutLetters(self, ipAddr, port, letters):
        try:
            self.mailBox.connect((ipAddr, port))
        except ConnectionRefusedError:
            print("connection to: %s::%d refused" % (ipAddr, port))
            return
        else:
            for letter in letters:
                self.mailBox.sendall(letter.encode('utf-8'))
                reply = self.mailBox.recv(1024)
                if not reply:
                    break
        self.mailBox.close()

