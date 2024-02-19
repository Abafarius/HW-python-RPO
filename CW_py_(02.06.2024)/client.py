import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('192.168.110.119', 7777)


message = "exit"
my_sock.sendto(message.encode("utf-8"), server_addr)
