from socket import *
HOST = '127.0.0.1'
PORT = 5000

s = socket(AF_INET, SOCK_STREAM)

s.connect((HOST, PORT))
while 1:
    data = s.recv(1024)
    print(data)
