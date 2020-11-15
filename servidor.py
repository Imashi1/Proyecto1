#Libraries

#server loop

def server(adminmusic):
     import pygame
     import sys
     import funcionesgenerales
     import s_juego
     sonidoboton=pygame.mixer.Sound('sound/boton.wav')
     #se define una pantalla para el registro de servidor
     serv=pygame.display.set_mode((1152,700))
     serv_rect=serv.get_rect()
     cursor1=funcionesgenerales.Cursor()
     #se carga imagen del boton "regresar" y crear el boton
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     #se carga una fuente, y renderizar textos
     mifuente=pygame.font.SysFont("Consolas",60)
     titulo_server=mifuente.render("Server",0,(255,255,255))
     titulo_contrasenha=mifuente.render("Contraseña",0,(255,255,255))
     #se crea una fuente e inicializan 2 cadenas de texto
     base_font=pygame.font.Font(None,60)
     user_text=''
     user_text2=''
     #se carga y crea el boton jugar
     jugar=pygame.image.load('img/btnjugar.png')
     jugar2=pygame.image.load('img/btnjugar2.png')
     btnjugar=funcionesgenerales.Boton(jugar,jugar2,480,600)
     #se inicializan estados de estar escribiendo
     escribiendo=False
     escribiendo2=False
     adminmusic.reproducir()
     #se inicializa el estado corriendo registro servidor
     running_server=True
     while running_server:
          adminmusic.circular()
          for event in pygame.event.get():
               #finaliza el programa del juego
               if event.type==pygame.QUIT:
                    running_server=False
                    pygame.quit()
                    sys.exit()
               if event.type==pygame.MOUSEBUTTONDOWN:
                    #se regresa al menu principal
                    if cursor1.colliderect(boton1.rect):
                         sonidoboton.play()
                         running_server=False
                    #iniciamos la pantalla del juego
                    if cursor1.colliderect(btnjugar.rect):
                         sonidoboton.play()
                         s_juego.juego()
                    #detecta si el cursor colisiono con el primer campo de texto
                    if cursor1.colliderect(a):
                         if escribiendo==True:
                              escribiendo=False
                         else:
                              escribiendo=True
                    #redefine el estado escribiendo primer campo de texto
                    if cursor1.colliderect(serv_rect) and cursor1.colliderect(a)==False:
                         escribiendo=False
                    #detecta si el cursor colisiono con el segundo campo de texto
                    if cursor1.colliderect(a2):
                         if escribiendo2==True:
                              escribiendo2=False
                         else:
                              escribiendo2=True
                    #redefine el estado escribiendo segundo campo de texto
                    if cursor1.colliderect(serv_rect) and cursor1.colliderect(a2)==False:
                         escribiendo2=False

               #permite escribir en el primer campo de texto  ###################################################
               if escribiendo==True:
                    if event.type == pygame.KEYDOWN:
                         if event.key==pygame.K_BACKSPACE:
                              user_text=user_text[:-1]
                         else:
                              if len(user_text)<=11:
                                   user_text+=event.unicode
               #permite escribir en el segundo campo de texto
               if escribiendo2==True:
                    if event.type == pygame.KEYDOWN:
                         if event.key==pygame.K_BACKSPACE:
                              user_text2=user_text2[:-1]
                         else:
                              if len(user_text2)<=11:
                                   user_text2+=event.unicode  ##########################################
          #define el color de fondo de la pantalla
          serv.fill((50,150,200))
          cursor1.update()
          #muestra los campos de texto
          a=pygame.draw.rect(serv,(250,250,250),[600,150,350,50],0)
          a2=pygame.draw.rect(serv,(250,250,250),[600,500,350,50],0)
          #muestra texto a la pantalla
          serv.blit(titulo_server,(200,150))
          serv.blit(titulo_contrasenha,(200,500))
          #inicializan los textos que van en los campos de texto
          text_surface=base_font.render(user_text,True,(0,0,0))
          text_surface2=base_font.render(user_text2,True,(0,0,0))
          #muestra los textos que van en los campos de texto
          serv.blit(text_surface,(610,150))
          serv.blit(text_surface2,(610,500))
          #muestra de boton "regresar", jugar
          boton1.update(serv,cursor1)
          btnjugar.update(serv,cursor1)
          #carga los elementos del update
          pygame.display.update()
     adminmusic.saliendopantalla()
     return adminmusic
               
