import socket

class Processor(object):
    def __init__(self):
        self.mailBox = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def BindMailBox(self, ipAddr, port):
        try:
            self.mailBox.bind((ipAddr, port))
        except:
            print("binding port %d failed" % port)
            return False
        else:
            return True

    def ReceivLetter(self):

        self.mailBox.listen(5)
        postMan, addr = self.mailBox.accept()
        letter = postMan.recv(1000)
        postMan.close()
        return letter.decode("utf-8")
