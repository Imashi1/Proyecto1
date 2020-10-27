#Libraries
import pygame
import sys
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
     def update(self,pantalla,cursor):
          if cursor.colliderect(self.rect):
               self.imagen_actual=self.imagen_seleccion
          else: self.imagen_actual=self.imagen_normal

          pantalla.blit(self.imagen_actual,self.rect)
     def mover(self,cursor):
          if cursor.colliderect(self.rect):
               pass
          else: self.rect.left,self.rect.top=pygame.mouse.get_pos()
     def rotar(self,angulo):
          imagen_actual=pygame.transform.rotate(self.imagen_normal,angulo)
          self.imagen_normal=imagen_actual
          self.imagen_seleccion=pygame.transform.rotate(self.imagen_seleccion,angulo)
          self.imagen_actual=imagen_actual
          self.rect=imagen_actual.get_rect()
          self.rect.left,self.rect.top=pygame.mouse.get_pos()
