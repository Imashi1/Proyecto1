import pygame
import numpy as np
import pandas as pd
import funcionesgenerales
class Player():
        """Clase jugador: almacena informacion del juegador, para enviarlo al otro"""
        def __init__(self,x,y,width,height,color,turno):
                """Funcion que: inicializa el jugador con 2 dataframe como mapas y estado de turno dependiendo del ultimo parametro"""
                self.x=x        #NA
                self.y=y        #NA
                self.width=width #NA
                self.height=height #NA
                self.color=color #NA
                self.rect=(x,y,width,height) #NA
                self.vel=4 #NA
                """inicializa frames para ser usados como mapas de barcos y misiles"""
                self.myship=pd.DataFrame(np.array([['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']]))
                self.myatack=pd.DataFrame(np.array([['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']]))
                """crea una lista de la(s) ultima(s) posiciones nuevas en el mapa"""
                self.posship=[]
                self.posatack=[]
                self.nrobarcos=0
                self.nromisiles=0
                self.miturno=turno
                self.confirmacion=False
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
        def draw(self,win): #NA
                pygame.draw.rect(win,self.color,self.rect)
        def move(self):         #NA
                keys=pygame.key.get_pressed()                                                           #<-esa funcion es interesante
                if keys[pygame.K_LEFT]:
                        self.x-=self.vel
                if keys[pygame.K_RIGHT]:
                        self.x+=self.vel
                if keys[pygame.K_UP]:
                        self.y-=self.vel
                if keys[pygame.K_DOWN]:
                        self.y+=self.vel
                self.update()
        def update(self):               #NA
                self.rect = (self.x,self.y,self.width,self.height)
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
        def setposatack(self,posatack):
                """Funcion que: actualiza la posicion del misil reciente"""
                self.posatack=posatack
        def getnrobarcos(self):
                """Funcion que: retorna el numero de barcos del jugador"""
                return self.nrobarcos
        def increnrobarcos(self):
                """Funcion que: incrementa el numero de barcos del jugador"""
                self.nrobarcos=self.nrobarcos+1
        def getnromisiles(self):
                """Funcion que: retorna el numero de misiles del jugador"""
                return self.nromisiles
        def increnromisiles(self):
                """Funcion que: incrementa el numero de misiles del jugador"""
                self.nromisiles=self.nromisiles+1
                
                
