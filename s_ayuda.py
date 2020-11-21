def ayud(adminmusic):
     """Pantalla ayuda: Recibe el administrador de la musica para que se mantenga funcionando, y además lo retorna"""
     import pygame
     import sys
     import funcionesgenerales
     """inicializa el sonido para botones"""
     sonidoboton=pygame.mixer.Sound('sound/boton.wav')
     ayu=pygame.display.set_mode((1152,700))
     titayuda=pygame.image.load('img/btnayuda.png')
     cursor1=funcionesgenerales.Cursor()
     """se crea el boton regresar"""
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     """se crea un barco para realizar un ejemplo del juego"""
     imagenbarco=pygame.image.load('img/barco32.png')
     mapaayud=pygame.image.load('img/mapaayud.png')
     barcoayud=funcionesgenerales.Barco(imagenbarco,imagenbarco,820,270)
     """se cargan las instrucciones del juego"""
     int1=pygame.image.load('img/int1.png')
     """se carga la fuente de letra a utilizar"""
     mifuente=pygame.font.SysFont("Consolas",40)
     """se reproduce la musica, si la anterior se ha terminado"""
     adminmusic.reproducir()
     """se inicializa el estado de corriendo la pantalla ayuda"""
     running_ayuda=True
     while running_ayuda:
          """reproduce la musica que sigue"""
          adminmusic.circular()
          for event in pygame.event.get():
               """se termina la pantalla ayuda y finaliza el programa"""
               if event.type==pygame.QUIT:
                    running_ayuda=False
                    pygame.quit()
                    sys.exit()
               """se retrocede a la pantalla del menu"""
               if event.type==pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton1.rect):
                         sonidoboton.play()
                         running_ayuda=False
          """carga de color de fondo, imagenes y boton regresar"""
          ayu.fill((50,150,200))
          ayu.blit(mapaayud,(750,320))
          barcoayud.update(ayu,cursor1)
          ayu.blit(int1,(10,220))
          ayu.blit(titayuda,(450,10))
          """se carga un cursor para la pantalla"""
          cursor1.update()
          boton1.update(ayu,cursor1)
          """carga los elementos del update"""
          pygame.display.update()
     """se realiza operaciones de musica para regresar a otra pantalla"""
     adminmusic.saliendopantalla()
     return adminmusic  
