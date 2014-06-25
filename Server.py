import asyncore
import socket
from threading import Thread
import time

__author__ = 'Github: echelon265 | twitter: @zerjioAng'

class ServerUDP(asyncore.dispatcher):

    data = ""

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind(('', port))
        self.listen(1)
        print("Server listening on port "+str(port))

    def handle_accept(self):
        # when we get a client connection start a dispatcher for that
        # client
        socket, address = self.accept()
        print('Connected by', address)
        EchoHandler(socket)

class EchoHandler(asyncore.dispatcher_with_send):

    # dispatcher_with_send extends the basic dispatcher to have an output
    # buffer that it writes whenever there's content

    def handle_read(self):
        raw_data = self.recv(1024)
        data = str(raw_data.decode())
        # minimum content that server receives is --> \n
        data = data[:-1]
        self.out_buffer = "Server >> ".encode()+raw_data

    def handle_read(self):

        raw_data = self.recv(1024)
        data = str(raw_data.decode())
        # minimum content that server receives is --> \n
        data = data[:-1]

        if data == 'quit()':
            print("Closing UDP Server...")
            self.out_buffer = "Closing UDP Server".encode()+raw_data
            self.close()
            print("Server closed")
            exit(0)
        elif len(data)>0:
            print("Client << "+data)
            self.out_buffer = "Server >> ".encode()+raw_data #input("intorduzca algo para enviar: ").encode()

class Server(Thread):

    def __init__(self):
        Thread.__init__(self)
        print("Starting UDP Server service...")

    def run(self):
        s = ServerUDP('', 5007)
        print("Running UDP Server")
        asyncore.loop()

s = Server()
s.start()