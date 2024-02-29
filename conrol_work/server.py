import socket
import json

class AbcServer:
    remote = ()
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((host, port))

    def _send(self, msg):
        self.sock.sendto(msg.encode('utf8'), self.remote)

    def _receive(self):
        data, self.remote = self.sock.recvfrom(1024)
        return data.decode('utf8')
    
    def send(self, word: str):
        data = {'word': word}
        msg = json.dumps(data)
        self._send(msg)

    def connect(self):
        msg = ''
        while msg != 'hello':
            msg = self.receive()

    def end(self):
        data = {'gameover': ''}
        msg = json.dumps(data)
        self._send(msg)
        

    def receive(self):
        msg = self._receive()
        data = json.loads(msg)
        if 'word' in data:
            return data['word']
        elif 'gameover' in data:
            return ''
        elif 'hello' in data:
            return 'hello'
        else:
            print('AbcServer:: Bad data received')
