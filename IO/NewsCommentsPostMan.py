import socket

class PostMan(object):
    def __init__(self):
        self.mailBox = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    def PutOneLetter(self, ipAddr, port, letter):
        encoded_letter = letter.encode("utf-8")
        try:
            self.mailBox.sendto(encoded_letter, (ipAddr, port))
        except:
            print("sending Failed")
            return False
        else:
            response = self.mailBox.recvfrom(1024)
            if not response:
                print("sending Failed")
                return False
            return True

