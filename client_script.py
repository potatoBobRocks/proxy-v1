import socket

server_address = ('localhost', 8888)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

data = client_socket.recv(1024)
print("Recieved: ", data.decode('utf-8'))
client_socket.close()