import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8888)
server_socket.bind(server_address)

server_socket.listen(5)

client_socket, client_address = server_socket.accept()

client_socket.send(b'Hello, world!')

server_socket.close()