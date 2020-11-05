#Libraries

#server loop
def ayud():
     import pygame
     import sys
     import funcionesgenerales
     sonidoboton=pygame.mixer.Sound('sound/boton.wav')
     ayu=pygame.display.set_mode((1152,700))
     titayuda=pygame.image.load('img/btnayuda.png')
     cursor1=funcionesgenerales.Cursor()
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     int1=pygame.image.load('img/int1.png')
     int2=pygame.image.load('img/int2.png')

     mifuente=pygame.font.SysFont("Consolas",40)
     running_ayuda=True
     while running_ayuda:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    running_ayuda=False
                    pygame.quit()
                    sys.exit()
               if event.type==pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton1.rect):
                         sonidoboton.play()
                         running_ayuda=False
          ayu.fill((50,150,200))
          ayu.blit(int1,(10,220))
          ayu.blit(int2,(600,150))
          ayu.blit(titayuda,(450,10))
          cursor1.update()
          boton1.update(ayu,cursor1)
          pygame.display.update()
               
