import socket
from player import Player
from _thread import *
import pickle
def inicializarjugadores():
    """Funcion que: inicializa los jugadores, el primero con turno True, y el otro con turno False, retorna los jugadores inicializados"""
    players=[Player(0,0,50,50,(255,0,0),True),Player(100,100,50,50,(0,0,255),False)]
    return players
def intentarconectar():
    """Funcion que: intenta conectar el servidor con algun cliente"""
    try:
        s.bind((server,port))
    except socket.error as e:
        str(e)
    """se restringe los clientes activos a solo 2"""
    s.listen(2)
    print("waiting for a connection, server started")

server ='26.5.27.101'
port = 5555
auxplayer=Player(0,0,50,50,(255,0,0),True)
"""se crea un socket para mantener conectado el servidor con los clientes"""
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
intentarconectar()                                                #play5er1 = [Player(0,0,50,50,(255,0,0))]
                                                                #player2 = [Player(100,100,50,50,(0,0,255))]
                                                                #players = player1 + player2
                                                                #players-= player
                                                                #currentplayer-=1
"""se inicializan 2 jugadores para realizar el juego"""
players=inicializarjugadores()
def threaded_client(conn, player):
    """se define un hilo de clientes para recibir y enviar informacion de uno a otro"""
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        data = pickle.loads(conn.recv(2048))
        players[player]=data
        if not data:
            print("Disconnected")
            break
        else:
            if player ==1:
                reply=players[0]
            else:
                reply=players[1]
            print("Recieved:",data)
            print("Sending: ",reply)
        conn.sendall(pickle.dumps(reply))
    print("Lost connection")
    conn.close()
"""se inicializa un contador numero de jugador"""
currentPlayer = 0
"""se mantiene en espera para intentar conectar algun jugador"""
while True:
    conn,addr = s.accept()
    print("connected to:",addr)
    start_new_thread(threaded_client,(conn,currentPlayer))
    """se incrementa el numero de jugador"""
    currentPlayer +=1
        
