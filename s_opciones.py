#Libraries

#opciones loop
def opci():
     import pygame
     import sys
     import funcionesgenerales
     sonidoboton=pygame.mixer.Sound('sound/boton.wav')
     opciones=pygame.display.set_mode((1152,700))
     cursor1=funcionesgenerales.Cursor()
     #scrooll musica
     base=pygame.image.load('img/basemusica.png')
     scroll=pygame.image.load('img/scroll.png')
     rectscroll=scroll.get_rect()
     rectscroll.left,rectscroll.top=int(160*pygame.mixer.music.get_volume()+850),82 #(y)=0,5/80(x-850)
     #imagen botones
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     btnpararmusica=pygame.image.load('img/conmusica.png')
     btnactivarmusica=pygame.image.load('img/sinmusica.png')
     #botones
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     btnmusicaon=funcionesgenerales.Boton(btnpararmusica,btnpararmusica,650,150)
     btnmusicaoff=funcionesgenerales.Boton(btnactivarmusica,btnactivarmusica,750,150) 
     #titulos
     mifuente=pygame.font.SysFont("Consolas",96)
     titulo_sonido=mifuente.render("sonido",0,(255,255,255))
     moverscroll=False
     #
     #opc loop
     running_opc=True
     while running_opc:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    running_opc=False
                    pygame.quit()
                    sys.exit()
               if event.type==pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton1.rect):
                         sonidoboton.play()
                         running_opc=False
                    if cursor1.colliderect(btnmusicaon.rect):
                         pygame.mixer.music.stop()
                         infomenu[1]=0
                    if cursor1.colliderect(btnmusicaoff.rect):
                         pygame.mixer.music.play(1)   
                    if cursor1.colliderect(rectscroll):
                         if moverscroll==False:
                              moverscroll=True
                         else:
                              moverscroll=False
               if cursor1.colliderect(rectscroll)==False:
                         moverscroll=False
          opciones.fill((50,150,200))
          opciones.blit(titulo_sonido,(200,120))
          opciones.blit(base,(850,60))
          opciones.blit(scroll,rectscroll)
          cursor1.update()
          if moverscroll:
               buf=pygame.mouse.get_pos()
               if buf[0]>=850 and buf[0]<=1010:
                    rectscroll.left=buf[0]
                    pygame.mixer.music.set_volume((1/160)*(buf[0]-850)) #(y)=0,5/80(x-850)
               elif buf[0]<850:
                    rectscroll.left=850
                    pygame.mixer.music.set_volume(0)
               elif buf[0]>1010:
                    rectscroll.left=1010
                    pygame.mixer.music.set_volume(1)
               
          btnmusicaon.update(opciones,cursor1)
          btnmusicaoff.update(opciones,cursor1)
          boton1.update(opciones,cursor1)
          #
          pygame.display.update()
          
