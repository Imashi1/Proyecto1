def opci(adminmusic):
     """Pantalla ayuda: Recibe el administrador de la musica para que se mantenga funcionando, y además lo retorna"""
     import pygame
     import sys
     import os
     import funcionesgenerales
     """inicializa el sonido para los botones"""
     sonidoboton=pygame.mixer.Sound('sound/boton.wav')
     opciones=pygame.display.set_mode((1152,700))
     cursor1=funcionesgenerales.Cursor()
     """se define imagenes y rectangulo para el scrooll musica"""
     base=pygame.image.load('img/basemusica.png')
     scroll=pygame.image.load('img/scroll.png')
     rectscroll=scroll.get_rect()
     rectscroll.left,rectscroll.top=int(160*pygame.mixer.music.get_volume()+700),100 #(y)=0,5/80(x-850)
     """carga de imagenes botones musica"""
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     btnpararmusica=pygame.image.load('img/conmusica.png')
     btnactivarmusica=pygame.image.load('img/sinmusica.png')
     btnpausar=pygame.image.load('img/pausar.png')
     btnder=pygame.image.load('img/sgteder.png')
     btnizq=pygame.image.load('img/sgteizq.png')
     """creacion de botones musica"""
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     btnmusicaon=funcionesgenerales.Boton(btnpararmusica,btnpararmusica,630,85)
     btnmusicaoff=funcionesgenerales.Boton(btnactivarmusica,btnpausar,980,85)
     btnsgteder=funcionesgenerales.Boton(btnder,btnder,1040,85)
     btnsgteizq=funcionesgenerales.Boton(btnizq,btnizq,910,85)
     """se carga un fuente para el texto "sonido""""
     mifuente=pygame.font.SysFont("Consolas",60)
     titulo_sonido=mifuente.render("sonido",0,(255,255,255))
     """se inicializa un estado scroll moviendo"""
     moverscroll=False
     """se reproduce la musica., si la anterior se ha terminado"""
     adminmusic.reproducir()
     """se inicializa el estado corriendo pantalla"""
     running_opc=True
     while running_opc:
          """reproduce la musica que sigue"""
          adminmusic.circular()
          for event in pygame.event.get():
               """finaliza el programa del juego"""
               if event.type==pygame.QUIT:
                    running_opc=False
                    pygame.quit()
                    sys.exit()
               if event.type==pygame.MOUSEBUTTONDOWN:
                    #print(os.listdir("music"))
                    """reproduce la musica siguiente a la derecha"""
                    if cursor1.colliderect(btnsgteder.rect):
                         adminmusic.sgteder()
                         adminmusic.setpausa(False)
                    """reproduce la musica siguiente a la izquierda"""
                    if cursor1.colliderect(btnsgteizq.rect):
                         adminmusic.sgteizq()
                         adminmusic.setpausa(False)
                    """retrocedemos a la pantalla del menu"""
                    if cursor1.colliderect(boton1.rect):
                         sonidoboton.play()
                         running_opc=False
                    """detenemos la musica actual"""
                    if cursor1.colliderect(btnmusicaon.rect):
                         adminmusic.sdetener()
                    """iniciamos la musica"""
                    if cursor1.colliderect(btnmusicaoff.rect):
                         if adminmusic.estadodetener()==True:
                              adminmusic.activar()
                              adminmusic.setpausa(False)
                              adminmusic.reproducir()
                         elif adminmusic.getpausa()==True:
                              pygame.mixer.music.unpause()
                              adminmusic.setpausa(False)
                         else:
                              pygame.mixer.music.pause()
                              adminmusic.setpausa(True)
               """modificamos el estado del scrollmoviendo"""
                    if cursor1.colliderect(rectscroll):
                         moverscroll=True
               if event.type==pygame.MOUSEBUTTONUP:
                    if cursor1.colliderect(rectscroll):
                         moverscroll=False
                    else:
                         moverscroll=False
                         
          """define el color de fondo de la pantalla y se agregan textos, scroll"""
          opciones.fill((50,150,200))
          opciones.blit(titulo_sonido,(250,85))
          opciones.blit(base,(700,105))
          opciones.blit(scroll,rectscroll)
          cursor1.update()
          """permite y restringe el movimiento del scroll
          y al mismo tiempo baja o sube el volumen"""
          if moverscroll:
               buf=pygame.mouse.get_pos()
               if buf[0]>=700 and buf[0]<=860:
                    rectscroll.left=buf[0]
                    pygame.mixer.music.set_volume((1/160)*(buf[0]-700)) #(y)=0,5/80(x-850)
               elif buf[0]<700:
                    rectscroll.left=700
                    pygame.mixer.music.set_volume(0)
               elif buf[0]>860:
                    rectscroll.left=860
                    pygame.mixer.music.set_volume(1)
          """se muestran los botones de musica"""
          btnmusicaon.update(opciones,cursor1)
          btnsgteder.update(opciones,cursor1)
          btnsgteizq.update(opciones,cursor1)
          btnmusicaoff.update2(opciones,adminmusic)
          """se muestra el boton "regresar""""
          boton1.update(opciones,cursor1)
          """carga los elementos del update"""
          pygame.display.update()
     adminmusic.saliendopantalla()
     return adminmusic
