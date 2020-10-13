#Libraries
from screens import servidor
import pygame
import sys

pygame.init()

#menu loop
def menup():
     #pantalla menu
     menu=pygame.display.set_mode((1152,700))
     #el barco del fondo
     #down=pygame.image.load('img\n.png')
     #ship_Img=pygame.image.load("img\ship_menu.png")

     #titulo menu
     mifuente=pygame.font.SysFont("Italic",96)
     titulo_menu=mifuente.render("BATTLESHIP",0,(255,255,255))
     running_menu=True
     while running_menu:
        for event in pygame.event.get():
          menu.fill((50,150,200))
          menu.blit(titulo_menu,(340,13))
          #menu.blit(down,(0,500))
          #menu.blit(shipImg,(201,102)) #falta arreglar centrado a la mitad
          pygame.display.update()
          if event.type==pygame.QUIT:
               running_menu=False

          if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_LEFT:
                    running_menu=False
                    servidor.server()
        
     
menup()
pygame.quit()
