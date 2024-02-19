import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_addr = ('192.168.110.186', 7777)
my_sock.bind(my_addr)

my_sock.listen(10)

while True:

    client, addr = my_sock.accept()
    data = client.recv(2048)
    request = data.decode()

    print("Got the request: ", request)

    content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        
    </body>
    </html>
    """

    http_msg = f""" HTTP/1.1 200 OK
    content-type:text/html
    content-length:{len(content)}
    """
    response = http_msg + content
    client.send(response.encode("utf-8"))
    print(f"Recieved: '{data.decode('utf-8')}, from {addr}")