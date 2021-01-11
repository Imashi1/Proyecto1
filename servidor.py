
def server(adminmusic):
     """Pantalla registro servidor: Recibe el administrador de la musica para que se mantenga funcionando, y además lo retorna"""
     import pygame
     import sys
     import funcionesgenerales
     import s_juego
     import s_juego2
     """inicializamos el sonido para botones"""
     sonidoboton=pygame.mixer.Sound('sound/boton.wav')
     serv=pygame.display.set_mode((1152,700))
     serv_rect=serv.get_rect()
     cursor1=funcionesgenerales.Cursor()
     """se carga imagen del boton "regresar" y crear el boton"""
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     """se carga una fuente, y renderizar textos"""
     mifuente=pygame.font.SysFont("Consolas",50)
     titulo_server=mifuente.render("Servidor",0,(255,255,255))
     titulo_contrasenha=mifuente.render("Contraseña",0,(255,255,255))
     """se crea una fuente e inicializan 2 cadenas de texto"""
     base_font=pygame.font.SysFont("Consolas",30)
     base_font2=pygame.font.SysFont("Consolas",30)
     user_text=''
     user_text2=''
     """se carga y crea el boton jugar"""
     jugar=pygame.image.load('img/btnjugar.png')
     jugar2=pygame.image.load('img/btnjugar2.png')
     btnjugar=funcionesgenerales.Boton(jugar,jugar2,480,450)
     vscom=pygame.image.load('img/vscom.png')
     vscom2=pygame.image.load('img/vscom2.png')
     btnvscom=funcionesgenerales.Boton(vscom,vscom2,480,600)
     """se inicializan estados de estar escribiendo en un campo"""
     escribiendo=False
     escribiendo2=False
     sinconexion=0
     """se reproduce la musica, si la anterior se ha terminado"""
     adminmusic.reproducir()
     """se inicializa el estado corriendo registro servidor"""
     running_server=True
     while running_server:
          """reproduce la musica que sigue"""
          adminmusic.circular()
          for event in pygame.event.get():
               """finaliza el programa del juego"""
               if event.type==pygame.QUIT:
                    running_server=False
                    pygame.quit()
                    sys.exit()
               if event.type==pygame.MOUSEBUTTONDOWN:
                    """se regresa al menu principal"""
                    if cursor1.colliderect(boton1.rect):
                         sonidoboton.play()
                         running_server=False
                    """iniciamos la pantalla del juego"""
                    if cursor1.colliderect(btnjugar.rect)and len(user_text)!=0 and len(user_text)!=0:
                         sinconexion=0
                         sonidoboton.play()
                         adminmusic.sdetener()
                         sinconexion=s_juego.juego(user_text,int(user_text2))
                         adminmusic.activar()
                         adminmusic.reproducir()
                         
                    if cursor1.colliderect(btnjugar.rect)and (len(user_text)==0 or len(user_text)==0):
                         sinconexion=2
                    if cursor1.colliderect(btnvscom.rect):
                         sonidoboton.play()
                         adminmusic.sdetener()
                         s_juego2.juego()
                         adminmusic.activar()
                         adminmusic.reproducir()
                    """redefine el estado escribiendo primer campo de texto"""
                    if cursor1.colliderect(serv_rect) and cursor1.colliderect(a)==True:
                         escribiendo=True
                    else:
                         escribiendo=False
                    """redefine el estado escribiendo segundo campo de texto"""
                    if cursor1.colliderect(serv_rect) and cursor1.colliderect(a2)==True:
                         escribiendo2=True
                    else:
                         escribiendo2=False

               """permite escribir en el primer campo de texto"""
               if escribiendo==True:
                    if event.type == pygame.KEYDOWN:
                         if event.key==pygame.K_BACKSPACE:
                              user_text=user_text[:-1]
                         else:
                              if len(user_text)<=15:
                                   user_text+=event.unicode
               """permite escribir en el segundo campo de texto"""
               if escribiendo2==True:
                    if event.type == pygame.KEYDOWN:
                         if event.key==pygame.K_BACKSPACE:
                              user_text2=user_text2[:-1]
                         else:
                              if len(user_text2)<=15:
                                   letra=event.unicode
                                   if letra.isdigit():
                                        user_text2+=event.unicode  
          """define el color de fondo de la pantalla"""
          serv.fill((50,150,200))
          cursor1.update()
          """muestra los campos de texto"""
          a=pygame.draw.rect(serv,(250,250,250),[600,200,350,50],0)
          a2=pygame.draw.rect(serv,(250,250,250),[600,340,350,50],0)
          """muestra texto a la pantalla"""
          serv.blit(titulo_server,(200,200))
          serv.blit(titulo_contrasenha,(200,340))
          """inicializan los textos que van en los campos de texto"""
          text_surface=base_font.render(user_text,True,(0,0,0))
          text_surface2=base_font.render(user_text2,True,(0,0,0))
          if user_text=="" and escribiendo==False:
               text_surface=base_font2.render("Digite el servidor",True,(0,0,0))
          if user_text2=="" and escribiendo2==False:
               text_surface2=base_font2.render("Digite la contraseña",True,(0,0,0))
          if sinconexion==-1:
               text_surface3=base_font2.render("IP y puerto invalidos!!",True,(255,0,0))
               serv.blit(text_surface3,(30,640))
          if sinconexion==2:
               text_surface3=base_font2.render("Rellene los campos",True,(255,0,0))
               serv.blit(text_surface3,(30,640))
          """muestra los textos que van en los campos de texto"""
          serv.blit(text_surface,(610,200))
          serv.blit(text_surface2,(610,340))
          """muestra de boton "regresar", jugar"""
          boton1.update(serv,cursor1)
          btnjugar.update(serv,cursor1)
          btnvscom.update(serv,cursor1)
          """carga los elementos del update"""
          pygame.display.update()
     adminmusic.saliendopantalla()
     return adminmusic
               
