import socket
import json

class AbcClient:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect((host, port))

    def send(self, word):
        data = {"word": word}
        msg = json.dumps(data)
        self.sock.send(msg.encode("utf8"))

    def receive(self):
        data, _ = self.sock.recvfrom(1024)
        data = json.loads(data.decode("utf8"))
        return data["word"]

    def connect(self):
        data = {"hello": ""}
        msg = json.dumps(data)
        self.sock.send(msg.encode("utf8"))

    def end(self):
        data = {"gameover": ""}
        msg = json.dumps(data)
        self.sock.send(msg.encode("utf8"))