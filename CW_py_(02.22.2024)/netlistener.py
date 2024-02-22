import socket
import threading as th

class Listener:
    addr = ()
    sock = None
    running = False

    def __init__(self, port):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        self.addr = (ip, port)
        self.sock.bind(self.addr)

    def worker(self):        
        while self.running:
            data , addr = self.sock.recvfrom(1024)
            msg = data.decode("utf8")
            self.controller.on_msg_recieved(msg, addr[0])
        