import socket

class PostMan(object):
    def __init__(self):
        self.mailBox = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.assignedMailBox = False

    def AssignMailBox(self, ipAddr, port):
        try:
            self.mailBox.connect((ipAddr, port))
        except:
            print("connection to: %s::%d failed" % (ipAddr, port))
            self.assignedMailBox = False
        else:
            self.assignedMailBox = True

    def PutLetter(self, letter):
        if self.assignedMailBox:
            self.mailBox.sendall(letter)

    def Byebye(self):
        self.mailBox.close()
