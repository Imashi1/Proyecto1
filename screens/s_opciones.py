#Libraries

#opciones loop
def opci():
     import pygame
     import sys
     sys.path.insert(0,'../')
     import funcionesgenerales
     opciones=pygame.display.set_mode((1152,700))
     cursor1=funcionesgenerales.Cursor()
     #imagen botones
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     btnpararmusica=pygame.image.load('img/conmusica.png')
     btnactivarmusica=pygame.image.load('img/sinmusica.png')
     #botones
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     btnmusicaon=funcionesgenerales.Boton(btnpararmusica,btnpararmusica,700,50)
     btnmusicaoff=funcionesgenerales.Boton(btnactivarmusica,btnactivarmusica,900,50) 
     #titulos
     mifuente=pygame.font.SysFont("Italic",96)
     titulo_sonido=mifuente.render("sonido",0,(255,255,255))
     titulo_tamanhomapa=mifuente.render("tamaño",0,(255,255,255))
     titulo_idioma=mifuente.render("idioma",0,(255,255,255))
     
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
                         running_opc=False
                    if cursor1.colliderect(btnmusicaon.rect):
                         pygame.mixer.music.stop()
                    if cursor1.colliderect(btnmusicaoff.rect):
                         pygame.mixer.music.play(-1)   
                         
          opciones.fill((50,150,200))
          opciones.blit(titulo_sonido,(20,60))
          opciones.blit(titulo_tamanhomapa,(20,260))
          opciones.blit(titulo_idioma,(20,460))
          cursor1.update()
          btnmusicaon.update(opciones,cursor1)
          btnmusicaoff.update(opciones,cursor1)
          boton1.update(opciones,cursor1)
          #
          pygame.display.update()
               
