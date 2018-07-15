from socket import *
class ChatServer:
    def __init__(self, host, port):
        #startvars
        self.PORT = port
        self.HOST = host
        self.RECV_BUFFER = 4096
        self.CONNECTION_LIST = []
        #connection
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen(10)
        #append ser.socket
        self.CONNECTION_LIST.append(self.server_socket)
        print('[+]ChatServer startet on port:%s' %str(self.PORT))#debug
        #main
        self.looping()
        self.server_socket.close()
    def broadcast_data(self, sock, msg):
        for socket in self.CONNECTION_LIST:
            if socket != self.server_socket and self.server_socket != sock:
                try :
                    socket.send("msg")
                except :
                    socket.close()
                    self.CONNECTION_LIST.remove(socket)
    def looping(self):
        read_sockets = self.CONNECTION_LIST
        write_sockets = []
        error_sockets = []
        while True:
            for sock in read_sockets:
                if sock == self.server_socket:
                    sockfd, addr = self.server_socket.accept()
                    self.CONNECTION_LIST.append(sockfd)
                    print("Client (%s, %s) connected" % addr)
                    self.broadcast_data(sockfd, "[%s:%s] entered room\n" % addr)
                else:
                    try:
                        data = sock.recv(RECV_BUFFER)
                        if data:
                            self.broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)
                    except:
                        self.broadcast_data(sock, "[i]Client[%s, %s] is offline" % addr)
                        print("[i]Client[%s, %s] is offline" % addr)
                        sock.close()
                        self.CONNECTION_LIST.remove(sock)
                        continue


server = ChatServer('127.0.0.1', 5000)
