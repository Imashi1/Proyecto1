#Libraries
from screens import servidor
from screens import s_opciones
from screens import s_ayuda
import funcionesgenerales
import pygame
import sys
pygame.init()
#menu loop
def menup():
     #pantalla menu
     menu=pygame.display.set_mode((1152,700))
     #
     pygame.display.set_caption("Battleship")
     icon=pygame.image.load('img/icon.png')
     pygame.display.set_icon(icon)
     #
     cursor1=funcionesgenerales.Cursor()
     #el barco del fondo
     ship1=pygame.image.load('img/ship.png')
     ship2=pygame.image.load('img/n.png')
     #imagen de botones
     unov1=pygame.image.load('img/btn1vs1.png')
     unov12=pygame.image.load('img/btn1vs12.png')
     opciones=pygame.image.load('img/btnopciones.png')
     opciones2=pygame.image.load('img/btnopciones2.png')
     ayuda=pygame.image.load('img/btnayuda.png')
     ayuda2=pygame.image.load('img/btnayuda2.png')
     salir=pygame.image.load('img/btnsalir.png')
     salir2=pygame.image.load('img/btnsalir2.png')
     
     #titulo menu
     mifuente=pygame.font.SysFont("Italic",96)
     titulo_menu=mifuente.render("BATTLESHIP",0,(255,255,255))
     #los botones
     btn1v1=funcionesgenerales.Boton(unov1,unov12,30,580)
     btnopciones=funcionesgenerales.Boton(opciones,opciones2,310,580)
     btnayuda=funcionesgenerales.Boton(ayuda,ayuda2,590,580)
     btnsalir=funcionesgenerales.Boton(salir,salir2,870,580)
     running_menu=True
     while running_menu:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    running_menu=False
                    pygame.quit()
                    sys.exit()

               if event.type==pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(btn1v1.rect):
                         servidor.server()
                    if cursor1.colliderect(btnopciones.rect):
                         s_opciones.opci()
                    if cursor1.colliderect(btnayuda.rect):
                         s_ayuda.ayud()
                    if cursor1.colliderect(btnsalir.rect):
                         running_menu=False
                         pygame.quit()
                         sys.exit()
               
          menu.fill((50,150,200))            
          menu.blit(titulo_menu,(340,13))
          menu.blit(ship1,(180,60))
          menu.blit(ship2,(0,557))
          cursor1.update()
          btn1v1.update(menu,cursor1)
          btnopciones.update(menu,cursor1)
          btnayuda.update(menu,cursor1)
          btnsalir.update(menu,cursor1)
          pygame.display.update()
          
        
menup()
