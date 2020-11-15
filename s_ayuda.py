#Libraries

#server loop
def ayud(adminmusic):
     import pygame
     import sys
     import funcionesgenerales
     #inicializa el sonido para botones
     sonidoboton=pygame.mixer.Sound('sound/boton.wav')
     #define una pantalla
     ayu=pygame.display.set_mode((1152,700))
     titayuda=pygame.image.load('img/btnayuda.png')
     cursor1=funcionesgenerales.Cursor()
     #se crea el boton "regresar"
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     #se cargan las instrucciones del juego
     int1=pygame.image.load('img/int1.png')
     int2=pygame.image.load('img/int2.png')
     #se carga la fuente a utilizar
     mifuente=pygame.font.SysFont("Consolas",40)
     adminmusic.reproducir()
     #se inicializa el estado de "corriendo la pantalla ayuda"
     running_ayuda=True
     while running_ayuda:
          adminmusic.circular()
          for event in pygame.event.get():
               #se termina la pantalla ayuda y finaliza el programa
               if event.type==pygame.QUIT:
                    running_ayuda=False
                    pygame.quit()
                    sys.exit()
               #se retrocede a la pantalla del menu
               if event.type==pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton1.rect):
                         sonidoboton.play()
                         running_ayuda=False
          #carga de color de fondo, imagenes y boton regresar
          ayu.fill((50,150,200))
          ayu.blit(int1,(10,220))
          ayu.blit(int2,(600,150))
          ayu.blit(titayuda,(450,10))
          #se carga un cursor para la pantalla
          cursor1.update()
          boton1.update(ayu,cursor1)
          #carga los elementos del update
          pygame.display.update()
     adminmusic.saliendopantalla()
     return adminmusic  
