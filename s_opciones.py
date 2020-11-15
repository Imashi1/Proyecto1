#Libraries

#opciones loop
def opci(adminmusic):
     import pygame
     import sys
     import funcionesgenerales
     sonidoboton=pygame.mixer.Sound('sound/boton.wav')
     #se define la pantalla de opciones
     opciones=pygame.display.set_mode((1152,700))
     cursor1=funcionesgenerales.Cursor()
     #se define imagenes y rectangulo para el scrooll musica
     base=pygame.image.load('img/basemusica.png')
     scroll=pygame.image.load('img/scroll.png')
     rectscroll=scroll.get_rect()
     rectscroll.left,rectscroll.top=int(160*pygame.mixer.music.get_volume()+850),100 #(y)=0,5/80(x-850)
     #carga de imagenes boton play stop
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     btnpararmusica=pygame.image.load('img/conmusica.png')
     btnactivarmusica=pygame.image.load('img/sinmusica.png')
     #creacion de botones "regresar" play stop musica
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     btnmusicaon=funcionesgenerales.Boton(btnpararmusica,btnpararmusica,650,150)
     btnmusicaoff=funcionesgenerales.Boton(btnactivarmusica,btnactivarmusica,750,150) 
     #se carga un fuente para el texto "sonido"
     mifuente=pygame.font.SysFont("Consolas",96)
     titulo_sonido=mifuente.render("sonido",0,(255,255,255))
     #se inicializa un estado scroll moviendo
     moverscroll=False
     adminmusic.reproducir()
     #se inicializa el estado corriendo pantalla
     running_opc=True
     while running_opc:
          adminmusic.circular()
          for event in pygame.event.get():
               #finaliza el programa del juego
               if event.type==pygame.QUIT:
                    running_opc=False
                    pygame.quit()
                    sys.exit()
               if event.type==pygame.MOUSEBUTTONDOWN:
                    #retrocedemos a la pantalla del menu
                    if cursor1.colliderect(boton1.rect):
                         sonidoboton.play()
                         running_opc=False
                    #detenemos la musica actual
                    if cursor1.colliderect(btnmusicaon.rect):
                         adminmusic.sdetener()
                    #iniciamos la musica
                    if cursor1.colliderect(btnmusicaoff.rect):
                         adminmusic.activar()
                         adminmusic.reproducir()
                    #modificamos el estado del scrollmoviendo
                    if cursor1.colliderect(rectscroll):
                         if moverscroll==False:
                              moverscroll=True
                         else:
                              moverscroll=False
               if cursor1.colliderect(rectscroll)==False:
                         moverscroll=False
          #define el color de fondo de la pantalla y se agregan textos, scroll
          opciones.fill((50,150,200))
          opciones.blit(titulo_sonido,(200,120))
          opciones.blit(base,(850,105))
          opciones.blit(scroll,rectscroll)
          cursor1.update()
          #permite y restringe el movimiento del scroll
          #y al mismo tiempo baja o sube el volumen
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
          #se muestran los botones play stop
          btnmusicaon.update(opciones,cursor1)
          btnmusicaoff.update(opciones,cursor1)
          #se muestra el boton "regresar"
          boton1.update(opciones,cursor1)
          #carga los elementos del update
          pygame.display.update()
     adminmusic.saliendopantalla()
     return adminmusic
