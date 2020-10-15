#Libraries

#opciones loop
def juego():
     import pygame
     import sys
     sys.path.insert(0,'../')
     import funcionesgenerales
     battleship=pygame.display.set_mode((1152,700))
     cursor1=funcionesgenerales.Cursor()
     mapad=pygame.image.load('img/mapa.png')
     mapai=pygame.image.load('img/mapa.png')
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     barco_portaavion=pygame.image.load('img/barco43.png')
     x=0
     y=0
     running_juego=True
     while running_juego:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    running_juego=False
                    pygame.quit()
                    sys.exit()
               if event.type==pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton1.rect):
                         running_juego=False
                    
          battleship.fill((50,150,200))
          battleship.blit(mapai,(10,100))
          battleship.blit(mapad,(590,100))
          battleship.blit(barco_portaavion,(x,y))
          cursor1.update()
          boton1.update(battleship,cursor1)
          pygame.display.update()
               
