#Libraries

#server loop

def server():
     import pygame
     import sys
     import funcionesgenerales
     import s_juego
     sonidoboton=pygame.mixer.Sound('sound/boton.wav')
     serv=pygame.display.set_mode((1152,700))
     serv_rect=serv.get_rect()
     cursor1=funcionesgenerales.Cursor()
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     mifuente=pygame.font.SysFont("Consolas",60)
     titulo_server=mifuente.render("Server",0,(255,255,255))
     titulo_contrasenha=mifuente.render("Contraseña",0,(255,255,255))
     # label
     base_font=pygame.font.Font(None,60)
     user_text=''
     user_text2=''
     #
     jugar=pygame.image.load('img/btnjugar.png')
     jugar2=pygame.image.load('img/btnjugar2.png')
     btnjugar=funcionesgenerales.Boton(jugar,jugar2,480,600)
     escribiendo=False
     escribiendo2=False
     running_server=True
     while running_server:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    running_server=False
                    pygame.quit()
                    sys.exit()
               if event.type==pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton1.rect):
                         sonidoboton.play()
                         running_server=False
                    if cursor1.colliderect(btnjugar.rect):
                         sonidoboton.play()
                         s_juego.juego()
                    if cursor1.colliderect(a):
                         if escribiendo==True:
                              escribiendo=False
                         else:
                              escribiendo=True
                    if cursor1.colliderect(serv_rect) and cursor1.colliderect(a)==False:
                         escribiendo=False

                    if cursor1.colliderect(a2):
                         if escribiendo2==True:
                              escribiendo2=False
                         else:
                              escribiendo2=True
                    if cursor1.colliderect(serv_rect) and cursor1.colliderect(a2)==False:
                         escribiendo2=False

                         
               if escribiendo==True:
                    if event.type == pygame.KEYDOWN:
                         if event.key==pygame.K_BACKSPACE:
                              user_text=user_text[:-1]
                         else:
                              if len(user_text)<=12:
                                   user_text+=event.unicode

                                   
               if escribiendo2==True:
                    if event.type == pygame.KEYDOWN:
                         if event.key==pygame.K_BACKSPACE:
                              user_text2=user_text2[:-1]
                         else:
                              if len(user_text2)<=12:
                                   user_text2+=event.unicode
          serv.fill((50,150,200))
          cursor1.update()
          a=pygame.draw.rect(serv,(250,250,250),[600,150,350,50],0)
          a2=pygame.draw.rect(serv,(250,250,250),[600,500,350,50],0)
          serv.blit(titulo_server,(200,150))
          serv.blit(titulo_contrasenha,(200,500))
          text_surface=base_font.render(user_text,True,(0,0,0))
          text_surface2=base_font.render(user_text2,True,(0,0,0))
          serv.blit(text_surface,(610,150))
          serv.blit(text_surface2,(610,500))
          boton1.update(serv,cursor1)
          btnjugar.update(serv,cursor1)
          pygame.display.update()
      
               
