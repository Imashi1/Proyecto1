import socket
from _thread import *
from player import Player
import pickle
server = "192.168.0.3"
port = 5555
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.bind((server,port))
except socket.error as e:
    str(e)
s.listen(2)
print("waiting for a connection, server started")
#player1 = [Player(0,0,50,50,(255,0,0))]
#player2 = [Player(100,100,50,50,(0,0,255))]
#players = player1 + player2
#players-= player
#currentplayer-=1
players=[Player(0,0,50,50,(255,0,0)),Player(100,100,50,50,(0,0,255))]
def threaded_client(conn, player):
        conn.send(pickle.dumps(players[player]))
        reply = ""
        while True:
                try:
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
                except:
                        break
        print("Lost connection")
        conn.close()
currentPlayer = 0
while True:
        conn,addr = s.accept()
        print("connected to:",addr)
        start_new_thread(threaded_client,(conn,currentPlayer))
        currentPlayer +=1
