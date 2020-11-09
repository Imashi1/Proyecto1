import pygame
import numpy as np
import pandas as pd
import funcionesgenerales
#clase player, sirve para cruzar la informacion de lo que el jugador
#esta haciendo, y ademas facilitar el envio de data al servidor
class Player():
        def __init__(self,x,y,width,height,color,turno):
                self.x=x        #NA
                self.y=y        #NA
                self.width=width #NA
                self.height=height #NA
                self.color=color #NA
                self.rect=(x,y,width,height) #NA
                self.vel=4 #NA
                #inicializa frames para ser usados como mapas de barcos y misiles
                self.myship=pd.DataFrame(np.array([['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']]))
                self.myatack=pd.DataFrame(np.array([['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']]))
                #crea una lista de la(s) ultima(s) posiciones nuevas en el mapa
                self.posship=[]
                self.posatack=[]
                self.nrobarcos=0
                self.nromisiles=0
                self.miturno=turno
        def getmiturno(self):
                return self.miturno
        def setmiturno(self,valor):
                self.miturno=valor
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
        #obtiene el mapa de mis barcos
        def getmyship(self):                            
                return self.myship
        #obtiene el mapa de mis ataques
        def getmyatack(self):
                return self.myatack
        #actualiza el mapa de mis barcos
        def setmyship(self,mapship):
                self.myship=mapship
        #actualiza el mapa de mis ataques
        def setmyatack(self,mapatack):
                self.myatack=mapatack

        #obtiene la(s) ultima(s) posiciones nuevas de un barco recien colocado
        def getposship(self):
                return self.posship
        #obtiene la ultima posicion nueva de un ataque recien colocado
        def getposatack(self):
                return self.posatack
        #actualiza la posicion del barco reciente
        def setposship(self,posship):
                self.posship=posship
        #actualiza la posicion del ataque reciente
        def setposatack(self,posatack):
                self.posatack=posatack
        def getnrobarcos(self):
                return self.nrobarcos
        def increnrobarcos(self):
                self.nrobarcos=self.nrobarcos+1
        def getnromisiles(self):
                return self.nromisiles
        def increnromisiles(self):
                self.nromisiles=self.nromisiles+1
                
                
