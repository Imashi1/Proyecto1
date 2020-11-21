import servidor
import s_opciones
import s_ayuda
import funcionesgenerales
import pygame
import sys
pygame.init()
def ira1vs1(adminmusic):
     """Funcion que: corre la pantalla del servidor para ingresar datos, retorna el adminmusic para controlar la musica"""
     return servidor.server(adminmusic)
def iraopciones(adminmusic):
     """Funcion que: corre la pantalla opciones, retorna adminmusic para controlar la musica"""
     return s_opciones.opci(adminmusic)
def iraayuda(adminmusic):
     """Funcion que: corre la pantalla ayuda, retorna adminmusic para controlar la musica"""
     return s_ayuda.ayud(adminmusic)
def saliendo():
     """Funcion que: finaliza la pantalla del menu y ademas la pantalla del juego"""
     return False
def menup():
     """Pantalla principal del juego: 1152X700 pixeles, con 4 botones, 1VS1 OPCIONES AYUDA SALIR"""
     menu=pygame.display.set_mode((1152,700))
     """pone icono y nombre en la barra del programa"""
     pygame.display.set_caption("Battleship")
     icon=pygame.image.load('img/icon.png')
     pygame.display.set_icon(icon)
     """carga un sonido para los botones"""
     sonidoboton=pygame.mixer.Sound('sound/boton.wav')
     """define un cursor para la pantalla actual"""
     cursor1=funcionesgenerales.Cursor()
     """imagen del barco central"""
     ship1=pygame.image.load('img/gifship/ship.png')
     """imagen del fondo inferior"""
     ship2=pygame.image.load('img/n.png')
     """estado de musica cargada e inicializa la posicion o lugar de determinada musica"""
     haymusica=False
     posmusica=0
     """cargando imagenes de los botones"""
     unov1=pygame.image.load('img/btn1vs1.png')
     unov12=pygame.image.load('img/btn1vs12.png')
     opciones=pygame.image.load('img/btnopciones.png')
     opciones2=pygame.image.load('img/btnopciones2.png')
     ayuda=pygame.image.load('img/btnayuda.png')
     ayuda2=pygame.image.load('img/btnayuda2.png')
     salir=pygame.image.load('img/btnsalir.png')
     salir2=pygame.image.load('img/btnsalir2.png')
     """poniendo el titulo del juego, primero cargando una fuente, y luego renderizando un string con esa fuente"""
     mifuente=pygame.font.SysFont("Italic",96)
     titulo_menu=mifuente.render("BATTLESHIP",0,(255,255,255))
     """creando botones para el menu"""
     btn1v1=funcionesgenerales.Boton(unov1,unov12,30,580)
     btnopciones=funcionesgenerales.Boton(opciones,opciones2,310,580)
     btnayuda=funcionesgenerales.Boton(ayuda,ayuda2,590,580)
     btnsalir=funcionesgenerales.Boton(salir,salir2,870,580)
     """creando el administrador de una lista de musica, y la reproduce"""
     adminmusic=funcionesgenerales.Soundtrack()
     adminmusic.reproducir()
     """inicializando el estado de correr el juego y asi detectar cuando salir del bucle del juego"""
     running_menu=True
     while running_menu:
          """reproduce la musica que sigue"""
          adminmusic.circular()
          """bucle para manejar los eventos dados en el juego"""
          for event in pygame.event.get():
               """finaliza la pantalla del menu y ademas la pantalla del juego"""
               if event.type==pygame.QUIT:
                    running_menu=False
                    pygame.quit()
                    sys.exit()
               """verifica si se realizo un evento donde se pulso el boton hacia abajo del mouse"""
               if event.type==pygame.MOUSEBUTTONDOWN:
                    
                    if cursor1.colliderect(btn1v1.rect):
                         sonidoboton.play()
                         adminmusic=ira1vs1(adminmusic)
                         adminmusic.continuar()
                         adminmusic.reproducir()
                    
                    if cursor1.colliderect(btnopciones.rect):
                         sonidoboton.play()
                         adminmusic=iraopciones(adminmusic)
                         adminmusic.continuar()
                         adminmusic.reproducir()
                    
                    if cursor1.colliderect(btnayuda.rect):
                         sonidoboton.play()
                         adminmusic=iraayuda(adminmusic)
                         adminmusic.continuar()
                         adminmusic.reproducir()
                    if cursor1.colliderect(btnsalir.rect):
                         sonidoboton.play()
                         running_menu=saliendo()
                         pygame.quit()
                         sys.exit()
          """se le ingresa un color de relleno al menu"""
          menu.fill((50,150,200))
          """se muestra el titulo, imagenes,al menu a la pantalla"""
          menu.blit(titulo_menu,(340,13))
          menu.blit(ship1,(180,60))
          menu.blit(ship2,(0,557))
          """carga el cursor en la pantalla"""
          cursor1.update()
          """carga los botones del menu en la pantalla, ademas de enviar el cursor a utilizar"""
          btn1v1.update(menu,cursor1)
          btnopciones.update(menu,cursor1)
          btnayuda.update(menu,cursor1)
          btnsalir.update(menu,cursor1)
          """carga los elementos del update"""
          pygame.display.update()

"""corre la pantalla principal"""
menup()
