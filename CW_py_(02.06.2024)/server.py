import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_addr = ('localhost', 7777)

msg = ''
my_sock.bind(my_addr)

while msg != 'exit':

    data, addr = my_sock.recvfrom(1024)

    print(f"Recieved: '{data.decode('utf-8')}, from {addr}")

