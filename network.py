import socket
import pickle
from player import Player

#clase network, fundamental para facilitar el envio de informacion de
#la funcion del cliente, al servidor y al revez
class Network:
        def __init__(self):
                self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                #ip del servidor
                self.server='localhost'
                self.port=5555
                self.addr=(self.server,self.port)
                #inicializa p con la funcion connect() para recibir data
                self.p=self.connect()
                #obtiene data, en este caso, la clase jugador
        def getP(self):
                return self.p
                #se intenta conectar el network con el servidor
        def connect(self):
                try:
                        self.client.connect(self.addr)
                        return pickle.loads(self.client.recv(2048))
                except:
                        pass
                #se intenta enviar data de tamaño maximo de 2048bytes
        def send(self, data):
                try:
                        self.client.send(pickle.dumps(data))
                        return pickle.loads(self.client.recv(2048))
                except socket.error as e:
                        print(e)

