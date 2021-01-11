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
"""se crea un socket para mantener conectado el servidor con los clientes"""
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
intentarconectar()                                                
"""se inicializan 2 jugadores para realizar el juego"""
players=inicializarjugadores()
def threaded_client(conn, player):
    """se define un hilo de clientes para recibir y enviar informacion de uno a otro"""
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        data = pickle.loads(conn.recv(2048))
        if data.gethacercambio()!=False:
            players[player]=data
        players[player].setnrobloques(data.getnrobloques())
        players[player].setnroturno(data.getnroturno())
        
        if (players[0].getponersolobarcos()==False and players[1].getponersolobarcos()==False) and (players[0].getnrobloques()==0 or players[1].getnrobloques()==0) and (players[0].getnroturno()==players[1].getnroturno()):
            if players[0].getnrobloques()==0 and players[1].getnrobloques()!=0:
                players[0].setfin(2)
                players[1].setfin(1)
            elif players[0].getnrobloques()!=0 and players[1].getnrobloques()==0:
                players[0].setfin(1)
                players[1].setfin(2)
            else:
                players[0].setfin(3)
                players[1].setfin(3)
        if player==1:
            if players[1].gethacercambio()==True:
                players[1].sethacercambio(False)
                if players[1].getmiturno()==True:
                    players[1].setmiturno(False)
                    players[0].setmiturno(True)
                else:
                    players[1].setmiturno(True)
                    players[0].setmiturno(False)
        else:
            if players[0].gethacercambio()==True:
                players[0].sethacercambio(False)
                if players[0].getmiturno()==True:
                    players[0].setmiturno(False)
                    players[1].setmiturno(True)
                else:
                    players[0].setmiturno(True)
                    players[1].setmiturno(False)
        if not data:
            pass
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
        
