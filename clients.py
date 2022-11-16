import socket
import threading
from tkinter import *
import tkinter
from tkinter import simpledialog


class Chat:
    def __int__(self):
        HOST = '127.0.0.1'
        PORT = 8004
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        login = Tk()
        login.withdraw()
        self.janela_carregada = False
        self.ativo = True
        self.nome = simpledialog.askstring('Nome', 'Digite seu nome: ', parent=login)
        self.sala = simpledialog.askstring('Nome', 'Digite a sala que deseja entrar: ', parent=login)


chat = Chat()
