import socket
HOST = '127.0.0.1'
PORT = 8004
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

msg = client.recv(1024)
if msg == b'Sala':
    client.send(b'Jogos')
    client.send(b'Marcos')
