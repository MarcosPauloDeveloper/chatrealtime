import socket
import threading

HOST = '127.0.0.1'
PORT = 8004

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

room = {}


def broadcast(sala, msg):
    for r in room[sala]:
        if isinstance(msg, str):
            msg = msg.encode()
        r.send(msg)


def send_messsage(nome, sala, cliente):
    while True:
        message = client.recv(1024)
        mensagem = f'{nome}: {message.decode()}\n'
        broadcast(sala, mensagem)


while True:
    client, addr = server.accept()
    client.send(b'Sala')
    client_room = client.recv(1024).decode()
    client_name = client.recv(1024).decode()
    if client_room not in room.keys():
        room[client_room] = []
    room[client_room].append(client)
    print(f'{client_name} se conectou na sala {client_room}.')
    broadcast(client_room, f"{client_name} entrou na sala!")
    thread = threading.Thread(target=send_messsage, args=('nome', 'sala', 'cliente'))
    thread.start()
