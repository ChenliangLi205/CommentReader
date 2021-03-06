import socket
import time

class Receiver(object):
    def __init__(self, ipAddr, port):
        self.mailBox = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.mailBox.bind((ipAddr, port))

    def ReceiveOneLetter(self):
        data, addr = self.mailBox.recvfrom(1024)
        response = b"OK"
        self.mailBox.sendto(response, addr)
        return data.decode("utf-8")

    def ReceiveLetters(self, q):
        # q: multiprocessing.Queue
        while True:
            data, addr = self.mailBox.recvfrom(1024)
            q.put(data.decode("utf-8"))
            response = b"OK"
            self.mailBox.sendto(response, addr)
