import socket
import pickle
from player import Player
class Network:
        """Clase Network: facilita el envio y recepcion de data, entre el cliente y servidor"""
        def __init__(self,server,port):
                self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                """ip del servidor"""
                self.server=server
                self.port=port
                self.addr=(self.server,self.port)
                """inicializa p con la funcion connect() para recibir data"""
                self.p=self.connect()
        def getP(self):
                """Funcion que: Obtiene un objeto player numero 1 o 2 para comenzar el juego"""
                return self.p
        def connect(self):
                """Funcion que: intenta conectar al cliente con el servidor"""
                try:
                        self.client.connect(self.addr)
                        return pickle.loads(self.client.recv(2048))
                except:
                        return -1
        def send(self, data):
                """Funcion que: primero envia data del jugador y luego recibe data del otro jugador"""
                try:
                        self.client.send(pickle.dumps(data))
                        return pickle.loads(self.client.recv(2048))
                except socket.error as e:
                        print(e)

