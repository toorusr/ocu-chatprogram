from socket import *
from threading import *


class ChatClient:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port

        self.client_socket = socket(AF_INET, SOCK_STREAM)
        try:
            self.client_socket.connect((self.HOST, self.PORT))
        except:
            print('[!] No connection')
            exit()
        self.username_input()

        self.msg_send()

    def username_input(self):
        username = input('[>]Choose an username: ')
        self.username = username

    def msg_send(self):
        while True:

            msg_input = input('[>]%s(you): ' %self.username)
            if msg_input != '':
                #try:
                self.client_socket.send(bytes(msg_input, 'utf-8'))
                #except:
                #   print('[!] Could not send message')

    def looping(self):
        while True:
            data = self.client_socket.recv(1024)
            if data != '':
                print(data)

    def threading(self):
        start_new_thread(self.looping)
        start_new_thread(self.msg_send)

ChatClient('127.0.0.1', 5000)        
