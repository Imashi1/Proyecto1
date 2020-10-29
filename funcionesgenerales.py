#Libraries
import pygame
from decimal import Decimal, ROUND_HALF_UP
import sys
import numpy as np
import pandas as pd
def round_well(num):
     return Decimal(num).quantize(0,ROUND_HALF_UP)
class Cursor(pygame.Rect):
     def __init__(self):
          pygame.Rect.__init__(self,0,0,1,1)
     def update(self):
          self.left,self.top=pygame.mouse.get_pos()
class Boton(pygame.sprite.Sprite):
     def __init__(self,imagen1,imagen2,x=200,y=200):
          self.imagen_normal=imagen1
          self.imagen_seleccion=imagen2
          self.imagen_actual=self.imagen_normal
          self.rect=self.imagen_actual.get_rect()
          self.rect.left,self.rect.top=(x,y)
     def update(self,pantalla,cursor):
          if cursor.colliderect(self.rect):
               self.imagen_actual=self.imagen_seleccion
          else: self.imagen_actual=self.imagen_normal

          pantalla.blit(self.imagen_actual,self.rect)
#--------------------------------------------------------
class Barco(pygame.sprite.Sprite):
     def __init__(self,imagen1,imagen2,x=200,y=200):
          self.imagen_normal=imagen1
          self.imagen_seleccion=imagen2
          self.imagen_actual=self.imagen_normal
          self.rect=self.imagen_actual.get_rect()
          self.rect.left,self.rect.top=(x,y)
          self.h=round_well(pygame.Surface.get_width(self.imagen_normal)/50)
          self.v=round_well(pygame.Surface.get_height(self.imagen_normal)/50)
     def update(self,pantalla,cursor):
          if cursor.colliderect(self.rect):
               self.imagen_actual=self.imagen_seleccion
          else: self.imagen_actual=self.imagen_normal

          pantalla.blit(self.imagen_actual,self.rect)
     def mover(self,cursor,dimension,p_inicio,barcomoviendo):
          if cursor.colliderect(self.rect):
               pass
          else:
               self.rect.left,self.rect.top=pygame.mouse.get_pos()
               if self.rect.left<10:
                    self.rect.left=10
               if self.rect.top<100:
                    self.rect.top=100
               #if self.rect.left+pygame.Surface.get_width(self.imagen_normal)>570:
               #if self.rect.top+pygame.Surface.get_height(self.imagen_normal)>460:
          if barcomoviendo==False:
               if cursor.colliderect(self.rect):
                    xr,yr=self.rect.left,self.rect.top
                    for i in range(10):
                         for j in range(10):
                              x=i*dimension+p_inicio[0]
                              y=j*dimension+p_inicio[1]
                              if (xr>=x)and(xr<=x+dimension)and(yr>=y)and(yr<=y+dimension):
                                   self.rect.left,self.rect.top=x+10,y+10
                                   
               
     def rotar(self,angulo):
          imagen_actual=pygame.transform.rotate(self.imagen_normal,angulo)
          self.imagen_normal=imagen_actual
          self.imagen_seleccion=pygame.transform.rotate(self.imagen_seleccion,angulo)
          self.imagen_actual=imagen_actual
          self.rect=imagen_actual.get_rect()
          self.rect.left,self.rect.top=pygame.mouse.get_pos()
          self.h=round_well(pygame.Surface.get_width(self.imagen_normal)/50)
          self.v=round_well(pygame.Surface.get_height(self.imagen_normal)/50)
     def obtenerposicion(self,dimension,p_inicio,actual):
          xr,yr=self.rect.left,self.rect.top
          for i in range(10):
               for j in range(10):
                    x=i*dimension+p_inicio[0]
                    y=j*dimension+p_inicio[1]
                    if (xr>=x)and(xr<=x+dimension)and(yr>=y)and(yr<=y+dimension):
                         actual=[i,j]
          result=[]
          result.append(actual)
          for i in range(0,int(self.h)):
               for j in range(0,int(self.v)):
                    result.append([actual[0]+i,actual[1]+j])
        
          return result
