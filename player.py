import pygame
import numpy as np
import pandas as pd
import funcionesgenerales
class Player():
        """Clase jugador: almacena informacion del juegador, para enviarlo al otro"""
        def __init__(self,x,y,width,height,color,turno):
                """Funcion que: inicializa el jugador con 2 dataframe como mapas y estado de turno dependiendo del ultimo parametro"""
                """inicializa frames para ser usados como mapas de barcos y misiles"""
                self.myship=pd.DataFrame(np.array([['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']]))
                self.myatack=pd.DataFrame(np.array([['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']]))
                """crea una lista de la(s) ultima(s) posiciones nuevas en el mapa"""
                self.posship=[]
                self.posatack=[]
                self.nrobarcos=0
                self.nromisiles=0
                self.nrobloques=0
                self.miturno=turno
                self.ponersolobarcos=True
                self.confirmacion=False
        def restarnrobloques(self,valor):
                self.nrobloques=self.nrobloques-valor
        def getnrobloques(self):
                return self.nrobloques
        def setponersolobarcos(self,valor):
                self.ponersolobarcos=valor
        def getponersolobarcos(self):
                return self.ponersolobarcos
        def getconfirmacion(self):
                """Funcion que: retorna el estado de si confirmo la jugada actual, True si la confirmo, False, si no"""
                return self.confirmacion
        def setconfirmacion(self,v):
                """Funcion que: actualiza el estado de la jugada actual"""
                self.confirmacion=v
        def getmiturno(self):
                """Funcion que: retorna el estado del turno del jugador, True si le corresponde jugar, False, si no"""
                return self.miturno
        def setmiturno(self,v):
                """Funcion que: actualiza el estado del jugador"""
                self.miturno=v
        def getmyship(self):
                """Funcion que: retorna el mapa o dataframe de los barcos del jugador"""
                return self.myship
        def getmyatack(self):
                """Funcion que: retorna el mapa o dataframe de los misiles del jugador"""
                return self.myatack
        def setmyship(self,mapship):
                """Funcion que: actualiza el mapa de los barcos del jugador"""
                self.myship=mapship
        def setmyatack(self,mapatack):
                """Funcion que: actualiza el mapa de los misiles del jugador"""
                self.myatack=mapatack
        def getposship(self):
                """Funcion que: retorna la ultima o ultimas posiciones barcos nuevas del jugador"""
                return self.posship
        def getposatack(self):
                """Funcion que: retorna la ultima o ultimas posiciones misiles nuevas del jugador"""
                return self.posatack
        def setposship(self,posship):
                """Funcion que: actualiza la posicion del barco reciente"""
                self.posship=posship
                self.nrobloques=self.nrobloques+len(posship)
        def setposatack(self,posatack):
                """Funcion que: actualiza la posicion del misil reciente"""
                self.posatack=posatack
        def getnrobarcos(self):
                """Funcion que: retorna el numero de barcos del jugador"""
                return self.nrobarcos
        def increnrobarcos(self,valor=1):
                """Funcion que: incrementa el numero de barcos del jugador"""
                self.nrobarcos=self.nrobarcos+valor
        def getnromisiles(self):
                """Funcion que: retorna el numero de misiles del jugador"""
                return self.nromisiles
        def increnromisiles(self):
                """Funcion que: incrementa el numero de misiles del jugador"""
                self.nromisiles=self.nromisiles+1
                
                
