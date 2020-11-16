#Libraries
import pygame
from decimal import Decimal, ROUND_HALF_UP
import sys
import numpy as np
import pandas as pd
#Redondea un numero decimal a entero
def round_well(num):
     return Decimal(num).quantize(0,ROUND_HALF_UP)
#Clase cursor, creado para detectar colision de este con un rectangulo
class Cursor(pygame.Rect):
     def __init__(self):
          pygame.Rect.__init__(self,0,0,1,1)
     def update(self):
          self.left,self.top=pygame.mouse.get_pos()
#Clase boton, el boton posee 2 imagenes diferentes para dar un efecto
class Boton(pygame.sprite.Sprite):
     #Se usa get_rect para obtener un rectangulo colisionable y relizar la funcion de un boton
     def __init__(self,imagen1,imagen2,x=200,y=200):
          self.imagen_normal=imagen1
          self.imagen_seleccion=imagen2
          self.imagen_actual=self.imagen_normal
          self.rect=self.imagen_actual.get_rect()
          self.rect.left,self.rect.top=(x,y)
     #Produce un efecto de boton, ademas de mostrar el boton en determinada pantalla
     def update(self,pantalla,cursor):
          if cursor.colliderect(self.rect):
               self.imagen_actual=self.imagen_seleccion
          else: self.imagen_actual=self.imagen_normal

          pantalla.blit(self.imagen_actual,self.rect)
     def update2(self,pantalla,adminmusic):
          if adminmusic.estadodetener()==True:
               self.imagen_actual=self.imagen_normal
          elif adminmusic.getpausa()==True:
               self.imagen_actual=self.imagen_normal
          else:
               self.imagen_actual=self.imagen_seleccion
          pantalla.blit(self.imagen_actual,self.rect)
#--------------------------------------------------------
#Clase barco, posee diversas funciones como: crear, mover, obtener posicion en un tablero, siendo un objeto de suma importancia
class Barco(pygame.sprite.Sprite):
     #crea un barco con dimensiones dependiendo de la imagen, con apoyo de la funcion pygame.surface.get_width para obtener
     #las dimensiones de la imagen
     def __init__(self,imagen1,imagen2,x=200,y=200):
          self.imagen_normal=imagen1
          self.imagen_seleccion=imagen2
          self.imagen_actual=self.imagen_normal
          self.rect=self.imagen_actual.get_rect()
          self.rect.left,self.rect.top=(x,y)
          self.h=round_well(pygame.Surface.get_width(self.imagen_normal)/50)
          self.v=round_well(pygame.Surface.get_height(self.imagen_normal)/50)
          self.confirmado=False
     #Detecta las colisiones con un rectangulo, y muestra el barco en una pantalla
     def update(self,pantalla,cursor):
          if cursor.colliderect(self.rect):
               self.imagen_actual=self.imagen_seleccion
          else: self.imagen_actual=self.imagen_normal

          pantalla.blit(self.imagen_actual,self.rect)
     #Permite el movimiento del barco con el mouse, dejando a este, en una posicion valida del tablero
     def mover(self,cursor,dimension,p_inicio,barcomoviendo):
          if cursor.colliderect(self.rect):
               pass
          else:
               self.rect.left,self.rect.top=pygame.mouse.get_pos()
               #se restringe el espacio de movimiento del barco
               if self.rect.left<10:
                    self.rect.left=10
               if self.rect.top<100:
                    self.rect.top=100
                                                                                                         #if self.rect.left+pygame.Surface.get_width(self.imagen_normal)>570:
          #se corrige la posicion del barco a una valida para el tablero con                             #if self.rect.top+pygame.Surface.get_height(self.imagen_normal)>460:
          #ayuda de bucles intentando encontrar la direccion mas cercana
          if barcomoviendo==False:
               if cursor.colliderect(self.rect):
                    xr,yr=self.rect.left,self.rect.top
                    for i in range(10):
                         for j in range(10):
                              x=i*dimension+p_inicio[0]
                              y=j*dimension+p_inicio[1]
                              if (xr>=x)and(xr<=x+dimension)and(yr>=y)and(yr<=y+dimension):
                                   self.rect.left,self.rect.top=x+10,y+10
                                   
     #permite rotar el barco 90° con ayuda de la funcion pygame.transform.rotate()
     def rotar(self,angulo):
          imagen_actual=pygame.transform.rotate(self.imagen_normal,angulo)
          self.imagen_normal=imagen_actual
          self.imagen_seleccion=pygame.transform.rotate(self.imagen_seleccion,angulo)
          self.imagen_actual=imagen_actual
          #se obtiene un nuevo rectangulo
          self.rect=imagen_actual.get_rect()
          #se iguala la posicion del mouse con la del barco
          self.rect.left,self.rect.top=pygame.mouse.get_pos()
          #se actualizan las dimensiones del barco
          self.h=round_well(pygame.Surface.get_width(self.imagen_normal)/50)
          self.v=round_well(pygame.Surface.get_height(self.imagen_normal)/50)
     #permite dar con las coordenadas del barco en el mapa, aproximando la posicion con
     #posiciones validas conocidas, ademas devuelve las coordenadas en una lista
     def obtenerposicion(self,dimension,p_inicio,actual):
          xr,yr=self.rect.left,self.rect.top
          for i in range(10):
               for j in range(10):
                    x=i*dimension+p_inicio[0]
                    y=j*dimension+p_inicio[1]
                    if (xr>=x)and(xr<=x+dimension)and(yr>=y)and(yr<=y+dimension):
                         actual=[i,j]
          result=[]
                                                                                                                        #result.append(actual)
          for i in range(0,int(self.h)):
               for j in range(0,int(self.v)):
                    result.append([actual[0]+i,actual[1]+j])
        
          return result
     def getconfirmado(self):
          return self.confirmado
     def setconfirmado(self,valor):
          self.confirmado=valor
#permite cargar la musica determianda por una posicion
class Soundtrack():
     def __init__(self):
          self.lista=['music/music.mp3','music/music2.mp3','music/music3.mp3']
          self.estado=pygame.mixer.music.get_busy()
          self.volumen=pygame.mixer.music.get_volume()
          self.circulo=True
          self.nromusica=3
          self.nroactual=1
          self.posicion=0
          self.pausar=False
          self.detener=False
     def anhadir(self,musica):
          self.lista.append(musica)
          self.nromusica=self.nromusica+1
     def continuar(self):
          if self.detener==False:
               pygame.mixer.music.unpause()
     def reproducir(self):
          if self.detener==False and pygame.mixer.music.get_busy()==False:
               pygame.mixer.music.load(self.lista[self.nroactual-1])
               pygame.mixer.music.play()
               pygame.mixer.music.set_pos(self.posicion)
               self.posicion=0
     def circular(self):
          if self.detener==False and self.pausar==False:
               self.estado=pygame.mixer.music.get_busy()
               if self.estado==False:
                    pygame.mixer.music.unload()
                    if self.nroactual==self.nromusica:
                         self.nroactual=1
                    else:
                         self.nroactual=self.nroactual+1
                    pygame.mixer.music.load(self.lista[self.nroactual-1])
                    pygame.mixer.music.play()
     def sdetener(self):
          self.detener=True
          pygame.mixer.music.stop()
     def activar(self):
          self.detener=False
     def saliendopantalla(self):
          if self.pausar==True:
               self.sdetener()
          self.volumen=pygame.mixer.music.get_volume()
          self.posicion=pygame.mixer.music.get_pos()
          pygame.mixer.music.pause()
     def estadodetener(self):
          return self.detener
     def getpausa(self):
          return self.pausar
     def setpausa(self,v):
          self.pausar=v
     def sgteder(self):
          if self.nroactual!=self.nromusica:
               self.nroactual=self.nroactual+1
          else:
               self.nroactual=1
          self.sdetener()
          self.activar()
          self.reproducir()
     def sgteizq(self):
          if self.nroactual!=1:
               self.nroactual=self.nroactual-1
          else:
               self.nroactual=self.nromusica
          self.sdetener()
          self.activar()
          self.reproducir()
class Animacion():
     def __init__(self,imagenes,posicion,pantalla):
          self.lista=imagenes
          self.pos=posicion
          self.pantalla=patalla
     def iniciar(self):
          for i in lista:
               self.pantalla.blit(imagenes[i],pos)
#Clase boton play/pause, el boton posee 2 imagenes diferentes para dar un efecto
class Botonsino(pygame.sprite.Sprite):
     #Se usa get_rect para obtener un rectangulo colisionable y relizar la funcion de un boton
     def __init__(self,imagen1,imagen2,x=200,y=200):
          self.imagen_play=imagen1
          self.imagen_pausa=imagen2
          self.rect=self.imagen_play.get_rect()
          self.rect.left,self.rect.top=(x,y)
          self.estado=False
