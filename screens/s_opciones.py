#Libraries

#opciones loop
def opci():
     import pygame
     import sys
     sys.path.insert(0,'../')
     import funcionesgenerales
     opciones=pygame.display.set_mode((1152,700))
     cursor1=funcionesgenerales.Cursor()
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     mifuente=pygame.font.SysFont("Italic",96)
     titulo_sonido=mifuente.render("sonido",0,(255,255,255))
     titulo_tamanhomapa=mifuente.render("tamaño",0,(255,255,255))
     titulo_idioma=mifuente.render("idioma",0,(255,255,255))
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
          opciones.fill((50,150,200))
          opciones.blit(titulo_sonido,(20,60))
          opciones.blit(titulo_tamanhomapa,(20,260))
          opciones.blit(titulo_idioma,(20,460))
          cursor1.update()
          boton1.update(opciones,cursor1)
          pygame.display.update()
               
