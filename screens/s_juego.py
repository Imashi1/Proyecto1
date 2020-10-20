#Libraries
#opciones loop
def juego():
     from network import Network
     from player import Player
     import pygame
     import sys
     sys.path.insert(0,'../')
     import funcionesgenerales
     
     #
     battleship=pygame.display.set_mode((1152,700))
     def redrawWindow(battleship,player,player2):
          player.draw(battleship)
          player2.draw(win)
          pygame.display.update()
     cursor1=funcionesgenerales.Cursor()
     mapad=pygame.image.load('img/mapa.png')
     mapai=pygame.image.load('img/mapa.png')
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     
     n=Network()
     p=n.getP()
     clock=pygame.time.Clock()
     #game loop
     running_juego=True
     while running_juego:
          clock.tick(60)
          p2=n.send(p)
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    running_juego=False
                    pygame.quit()
                    sys.exit()
               if event.type==pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton1.rect):
                         running_juego=False
                    
                    
                    
          p.move()
          battleship.fill((50,150,200))
          battleship.blit(mapai,(10,100))
          battleship.blit(mapad,(590,100))
          cursor1.update()
          boton1.update(battleship,cursor1)
          redrawWindow(battleship,p,p2)
               
