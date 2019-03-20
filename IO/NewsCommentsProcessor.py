import socket

class Processor(object):
    def __init__(self):
        self.mailBox = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.binded = False

    def BindMailBox(self, port):
        try:
            self.mailBox.bind(('localhost', port))
        except:
            print("binding port %d failed" % port)
            self.binded = False
        else:
            self.binded = True


    def ReceivLetter(self):
        if self.binded:
            self.mailBox.listen()
            postMan, addr = self.mailBox.accept()
            letter = postMan.recv(1000)
            postMan.close()
            return letter
        return