import pygame
from decimal import Decimal, ROUND_HALF_UP
import sys
import time
import os
import numpy as np
import pandas as pd
def round_well(num):
     """Funcion que: recibe un numero decimal, Retorna el numero redondeado """
     return Decimal(num).quantize(0,ROUND_HALF_UP)
class Cursor(pygame.Rect):
     """Clase cursor: Permite la colision del cursor con un rectangulo x """
     def __init__(self):
          """Funcion que: asigna al cursor, un rectangulo de tamaño de 1x1 pixel """
          pygame.Rect.__init__(self,0,0,1,1)
     def update(self):
          """Funcion que: obtiene las coordenadas del mouse"""
          self.left,self.top=pygame.mouse.get_pos()
class Boton(pygame.sprite.Sprite):
     """Clase boton: Diseña un rectangulo, donde se puede colocar imagenes de fondo, y realizar algunos efectos de seleccion con la colision del cursor"""
     def __init__(self,imagen1,imagen2,x=200,y=200):
          """Funcion que: recibe 2 imagenes para imagen normal y imagen seleccion, inicializa un rectangulo para que sea colisionable"""
          self.imagen_normal=imagen1
          self.imagen_seleccion=imagen2
          self.imagen_actual=self.imagen_normal
          self.rect=self.imagen_actual.get_rect()
          self.rect.left,self.rect.top=(x,y)
     def update(self,pantalla,cursor):
          """Funcion que: muestra el boton, Produce el intercambio de imagenes del boton al colisionar con el mouse"""
          if cursor.colliderect(self.rect):
               self.imagen_actual=self.imagen_seleccion
          else: self.imagen_actual=self.imagen_normal

          pantalla.blit(self.imagen_actual,self.rect)
     def update2(self,pantalla,adminmusic):
          """Funcion que: muestra el boton, Produce el intercambio de imagenes del boton al colisionar y presionar con el mouse"""
          if adminmusic.estadodetener()==True:
               self.imagen_actual=self.imagen_normal
          elif adminmusic.getpausa()==True:
               self.imagen_actual=self.imagen_normal
          else:
               self.imagen_actual=self.imagen_seleccion
          pantalla.blit(self.imagen_actual,self.rect)
class Barco(pygame.sprite.Sprite):
     """Clase barco: Permite el manejo de un barco o misil, por medio del tablero"""
     def __init__(self,imagen1,imagen2,x=200,y=200,tipobarco=0):
          """Funcion que: crea un rectangulo con las dimensiones de la imagen"""
          self.tipo=tipobarco
          self.imagen_normal=imagen1
          self.imagen_seleccion=imagen2
          self.imagen_actual=self.imagen_normal
          self.rect=self.imagen_actual.get_rect()
          self.rect.left,self.rect.top=(x,y)
          self.h=round_well(pygame.Surface.get_width(self.imagen_normal)/50)
          self.v=round_well(pygame.Surface.get_height(self.imagen_normal)/50)
          self.confirmado=False
     def gettipobarco(self):
          return self.tipo
     def update(self,pantalla,cursor):
          """Funcion que: muestra el objeto, Permite detectar la colision del objeto, y mostrarlo en la pantalla"""
          if cursor.colliderect(self.rect):
               self.imagen_actual=self.imagen_seleccion
          else: self.imagen_actual=self.imagen_normal

          pantalla.blit(self.imagen_actual,self.rect)
     def mover(self,cursor,dimension,p_inicio,barcomoviendo,nfilas,ncolumn):
          """Funcion que: permite el movimiento del objeto con el mouse, denjandolo en una posicion valida del tablero (restringe el movimiento en el tablero) con ayuda de bucles"""
          if cursor.colliderect(self.rect):
               pass
          else:
               self.rect.left,self.rect.top=pygame.mouse.get_pos()
               if self.rect.left<p_inicio[0]:
                    self.rect.left=p_inicio[0]
               if self.rect.top<p_inicio[1]:
                    self.rect.top=p_inicio[1]

                    
               if self.rect.left>=p_inicio[0]+(nfilas*(dimension+2))-(pygame.Surface.get_width(self.imagen_normal)):
                    self.rect.left=p_inicio[0]+(nfilas*(dimension+2))-(pygame.Surface.get_width(self.imagen_normal))

                    
               if self.rect.top>=p_inicio[1]+(ncolumn*(dimension+2))-(pygame.Surface.get_height(self.imagen_normal)):
                    self.rect.top=p_inicio[1]+(ncolumn*(dimension+2))-(pygame.Surface.get_height(self.imagen_normal))
          if barcomoviendo==False:
               if cursor.colliderect(self.rect):
                    xr,yr=self.rect.left,self.rect.top
                    for i in range(nfilas):
                         for j in range(ncolumn):
                              x=i*dimension+p_inicio[0]
                              y=j*dimension+p_inicio[1]
                              if (xr>=x)and(xr<=x+dimension)and(yr>=y)and(yr<=y+dimension):
                                   self.rect.left,self.rect.top=x+10,y+10
     def superposicionb(self,listabarcos,listamisiles,listamisilesrival,botonconfirmarjugada):
          valor=False
          for i in (listabarcos[:-1]):
               if (self.rect).colliderect(i.rect):
                    valor=True
          for j in (listamisiles):
               if (self.rect).colliderect(j.rect):
                    valor=True
          for k in (listamisilesrival):
               if (self.rect).colliderect(k.rect):
                    valor=True
          if self.rect.colliderect(botonconfirmarjugada.rect):
               valor=True
          return valor
     def superposicionb2(self,listaizq,botonconfirmarjugada):###
          valor=False
          for i in (listaizq[:-1]):
               if (self.rect).colliderect(i.rect):
                    valor=True
          if self.rect.colliderect(botonconfirmarjugada.rect):
               valor=True
          return valor
     def superposicionm(self,listabarcos,listamisiles,listamisilesrival,botonconfirmarjugada):
          valor=False
          for i in (listabarcos):
               if (self.rect).colliderect(i.rect):
                    valor=True
          for j in (listamisiles[:-1]):
               if (self.rect).colliderect(j.rect):
                    valor=True
          if self.rect.colliderect(botonconfirmarjugada.rect):
               valor=True
          return valor
     def superposicionm2(self,listader,botonconfirmarjugada):###
          valor=False
          for j in (listader[:-1]):
               if (self.rect).colliderect(j.rect):
                    valor=True
          if self.rect.colliderect(botonconfirmarjugada.rect):
               valor=True
          return valor
     def rotar(self,angulo):
          """Funcion que: permite la rotacion del objeto en 90° de su posicion actual"""
          imagen_actual=pygame.transform.rotate(self.imagen_normal,angulo)
          self.imagen_normal=imagen_actual
          self.imagen_seleccion=pygame.transform.rotate(self.imagen_seleccion,angulo)
          self.imagen_actual=imagen_actual
          self.rect=imagen_actual.get_rect()
          self.rect.left,self.rect.top=pygame.mouse.get_pos()
          self.h=round_well(pygame.Surface.get_width(self.imagen_normal)/50)
          self.v=round_well(pygame.Surface.get_height(self.imagen_normal)/50)
     def obtenerposicion(self,dimension,p_inicio,actual,nfilas,ncolumn):
          """Funcion que: permite obtener la posicion del barco en el mapa, ademas retorna esa posicion"""
          xr,yr=self.rect.left,self.rect.top
          for i in range(nfilas):
               for j in range(ncolumn):
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
          """Funcion que: retorna el estado sobre si se confirmo la posicion del objeto, retorna True si esta confirmada y False si no"""
          return self.confirmado
     def setconfirmado(self,valor):
          """Funcion que: permite actualizar el estado de confirmacion de la posicion del objeto"""
          self.confirmado=valor
class Soundtrack():
     """Clase soundtrack: Permite la administracion de una lista de musica entre las pantallas del juego"""
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
          """Funcion que: permite añadir musica a la lista"""
          self.lista.append(musica)
          self.nromusica=self.nromusica+1
     def continuar(self):
          """Funcion que: continua la musica actual despues de haberla pausado"""
          if self.detener==False:
               pygame.mixer.music.unpause()
     def reproducir(self):
          """Funcion que: permite reproducir la musica actual si no se ha detenido"""
          if self.detener==False and pygame.mixer.music.get_busy()==False:
               pygame.mixer.music.load(self.lista[self.nroactual-1])
               pygame.mixer.music.play()
               pygame.mixer.music.set_pos(self.posicion)
               self.posicion=0
     def circular(self):
          """Funcion que: permite la reproduccion de la lista ciclicamente"""
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
          """Funcion que: permite detener la musica actual"""
          self.detener=True
          pygame.mixer.music.stop()
     def activar(self):
          """Funcion que: pone en False el estado de detener"""
          self.detener=False
     def saliendopantalla(self):
          """Funcion que: permite la continuacion de la musica de una pantalla a una anterior"""
          if self.pausar==True:
               self.sdetener()
          #self.nroactual=self.nroactual-1
          self.volumen=pygame.mixer.music.get_volume()
          self.posicion=pygame.mixer.music.get_pos()
          pygame.mixer.music.pause()
     def estadodetener(self):
          """Funcion que: retorna el estado de detener, True si esta detenido, False si no"""
          return self.detener
     def getpausa(self):
          """Funcion que: retorna el estado de pausa, True si esta pausado, False si no"""
          return self.pausar
     def setpausa(self,v):
          """Funcion que: actualiza el estado de pausa de la musica"""
          self.pausar=v
     def sgteder(self):
          """Funcion que: permite la reproduccion de la musica siguiente de la derecha"""
          if self.nroactual!=self.nromusica:
               self.nroactual=self.nroactual+1
          else:
               self.nroactual=1
          self.sdetener()
          self.activar()
          self.reproducir()
     def sgteizq(self):
          """Funcion que: permite la reproduccion de la muscia siguiente de la izquierda"""
          if self.nroactual!=1:
               self.nroactual=self.nroactual-1
          else:
               self.nroactual=self.nromusica
          self.sdetener()
          self.activar()
          self.reproducir()
class Animacion(pygame.sprite.Sprite):
     """Clase Animacion: usa frames para crear efecto gif"""
     def __init__(self,directorio,x=200,y=200):
          """Funcion que: recibe una lista de los frames, y la posicion en la pantalla"""
          self.contador=0
          self.lista=[]
          for i in range(len(os.listdir(directorio))):
               self.lista.append(directorio+os.listdir(directorio)[i])
          self.iniciar=False
          self.rect=(pygame.image.load(self.lista[0])).get_rect()
          self.rect.left,self.rect.top=(x,y)
     def activar(self):
          self.contador=0
          self.iniciar=True
     def parar(self):
          self.inciar=False
     def getiniciar(self):
          return self.iniciar
     def update1(self,velocidad,pantalla):
          if len(self.lista)>velocidad+self.contador and self.iniciar==True:
               self.contador=self.contador+velocidad
          else:
               self.contador=0
          pantalla.blit(pygame.image.load(self.lista[int(self.contador)]),self.rect)
     def update2(self,velocidad,pantalla):
          if len(self.lista)>velocidad+self.contador and self.iniciar==True:
               self.contador=self.contador+velocidad
          else:
               self.contador=0
               self.iniciar=False
          pantalla.blit(pygame.image.load(self.lista[int(self.contador)]),self.rect)

               
