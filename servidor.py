#Libraries

#server loop

def server():
     import pygame
     import sys
     import funcionesgenerales
     import s_juego
  
     serv=pygame.display.set_mode((1152,700))
     cursor1=funcionesgenerales.Cursor()
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     mifuente=pygame.font.SysFont("Italic",96)
     titulo_server=mifuente.render("Server:",0,(255,255,255))
     titulo_contrasenha=mifuente.render("Contraseña:",0,(255,255,255))
     jugar=pygame.image.load('img/btnjugar.png')
     jugar2=pygame.image.load('img/btnjugar2.png')
     btnjugar=funcionesgenerales.Boton(jugar,jugar2,480,600)
     running_server=True
     while running_server:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    running_server=False
                    pygame.quit()
                    sys.exit()
               if event.type==pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton1.rect):
                         running_server=False
                    if cursor1.colliderect(btnjugar.rect):
                         s_juego.juego()
          serv.fill((50,150,200))
          cursor1.update()
          serv.blit(titulo_server,(40,150))
          serv.blit(titulo_contrasenha,(40,500))
          boton1.update(serv,cursor1)
          btnjugar.update(serv,cursor1)
          pygame.display.update()
      
               
