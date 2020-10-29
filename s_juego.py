def juego():
     import pygame
     import numpy as np
     import pandas as pd
     import sys
     import funcionesgenerales
     from player import Player
     from network import Network
     battleship=pygame.display.set_mode((1152,700))
     cursor1=funcionesgenerales.Cursor()
     #fondo mapas
     mapad=pygame.image.load('img/mapa.png')
     mapai=pygame.image.load('img/mapa.png')
     fondomapai=funcionesgenerales.Boton(mapai,mapai,10,100)
     fondomapad=funcionesgenerales.Boton(mapad,mapad,590,100)
     #botones
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     btn_confirmar=pygame.image.load('img/btnconfirmarjugada.png')
     btn_confirmar2=pygame.image.load('img/btnconfirmarjugada2.png')
     botonconfirmarjugada=funcionesgenerales.Boton(btn_confirmar,btn_confirmar2,600,600)

     #objeto barco
     imagenbarco1=pygame.image.load('img/barco31.png')
     imagenbarco2=pygame.image.load('img/barco32.png')
     imagenbarco3=pygame.image.load('img/barco33.png')
     imagenbarco4=pygame.image.load('img/barco43.png')
     imagenbarco5=pygame.image.load('img/barco53.png')
     #
     btn_crearbarco1=pygame.image.load('img/1.png')
     btn_crearbarco1_2=pygame.image.load('img/1_2.png')
     btn_crearbarco2=pygame.image.load('img/2.png')
     btn_crearbarco2_2=pygame.image.load('img/2_2.png')
     btn_crearbarco3=pygame.image.load('img/3.png')
     btn_crearbarco3_2=pygame.image.load('img/3_2.png')
     btn_crearbarco4=pygame.image.load('img/4.png')
     btn_crearbarco4_2=pygame.image.load('img/4_2.png')
     btn_crearbarco5=pygame.image.load('img/5.png')
     btn_crearbarco5_2=pygame.image.load('img/5_2.png')
     
     #
     crearbarco1=funcionesgenerales.Boton(btn_crearbarco1,btn_crearbarco1_2,50,57)
     crearbarco2=funcionesgenerales.Boton(btn_crearbarco2,btn_crearbarco2_2,120,57)
     crearbarco3=funcionesgenerales.Boton(btn_crearbarco3,btn_crearbarco3_2,190,57)
     crearbarco4=funcionesgenerales.Boton(btn_crearbarco4,btn_crearbarco4_2,260,57)
     crearbarco5=funcionesgenerales.Boton(btn_crearbarco5,btn_crearbarco5_2,330,57)
     #
     n=Network()
     p = n.getP()
     #mapa
     df=pd.DataFrame(np.array([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]))
     #game loop
     listabarcos=[]
     cuentabarcos=0
     barcomoviendo=False
     running_juego=True
     while running_juego:
          p2 = n.send(p)
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    running_juego=False
                    pygame.quit()
                    sys.exit()
               if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                         if barcomoviendo:
                              listabarcos[cuentabarcos-1].rotar(90)
               if event.type==pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton1.rect):
                         running_juego=False
               if event.type==pygame.MOUSEBUTTONUP:
                    
                    if cursor1.colliderect(crearbarco1.rect):
                         #crear barcos
                         if barcomoviendo:
                              barcomoviendo=False
                              del listabarcos[cuentabarcos-1]
                              cuentabarcos=cuentabarcos-1
                         else:
                              listabarcos.append(funcionesgenerales.Barco(imagenbarco1,imagenbarco1,1,1))
                              cuentabarcos=cuentabarcos+1
                              barcomoviendo=True

                              
                    if cursor1.colliderect(crearbarco2.rect):
                         
                         if barcomoviendo:
                              barcomoviendo=False
                              del listabarcos[cuentabarcos-1]
                              cuentabarcos=cuentabarcos-1
                         else:
                              listabarcos.append(funcionesgenerales.Barco(imagenbarco2,imagenbarco2,1,1))
                              cuentabarcos=cuentabarcos+1
                              barcomoviendo=True

                              
                    if cursor1.colliderect(crearbarco3.rect):
                         
                         if barcomoviendo:
                              barcomoviendo=False
                              del listabarcos[cuentabarcos-1]
                              cuentabarcos=cuentabarcos-1
                         else:
                              listabarcos.append(funcionesgenerales.Barco(imagenbarco3,imagenbarco3,1,1))
                              cuentabarcos=cuentabarcos+1
                              barcomoviendo=True

                              
                    if cursor1.colliderect(crearbarco4.rect):
                         
                         if barcomoviendo:
                              barcomoviendo=False
                              del listabarcos[cuentabarcos-1]
                              cuentabarcos=cuentabarcos-1
                         else:
                              listabarcos.append(funcionesgenerales.Barco(imagenbarco4,imagenbarco4,1,1))
                              cuentabarcos=cuentabarcos+1
                              barcomoviendo=True

                              
                    if cursor1.colliderect(crearbarco5.rect):
                         
                         if barcomoviendo:
                              barcomoviendo=False
                              del listabarcos[cuentabarcos-1]
                              cuentabarcos=cuentabarcos-1
                         else:
                              listabarcos.append(funcionesgenerales.Barco(imagenbarco5,imagenbarco5,1,1))
                              cuentabarcos=cuentabarcos+1
                              barcomoviendo=True
                    if cuentabarcos>0:
                         if cursor1.colliderect(listabarcos[cuentabarcos-1].rect):
                              if barcomoviendo:
                                   barcomoviendo=False
                              else:
                                   barcomoviendo=True
                    if cursor1.colliderect(botonconfirmarjugada.rect):
                         if cuentabarcos>0:
                              pos=listabarcos[cuentabarcos-1].obtenerposicion(54,[10,100],[0,0])
                              print(pos)
                              for x in pos:
                                   df.iloc[x[1]][x[0]]=1
                         print("DataFrame:")
                         print(df)
          battleship.fill((50,150,200))
          cursor1.update()
          fondomapai.update(battleship,cursor1)
          fondomapad.update(battleship,cursor1)
          crearbarco1.update(battleship,cursor1)
          crearbarco2.update(battleship,cursor1)
          crearbarco3.update(battleship,cursor1)
          crearbarco4.update(battleship,cursor1)
          crearbarco5.update(battleship,cursor1)
          botonconfirmarjugada.update(battleship,cursor1)
          boton1.update(battleship,cursor1)
          for barco in listabarcos:
               barco.update(battleship,cursor1)
          if barcomoviendo:
               listabarcos[cuentabarcos-1].mover(cursor1)
          p.move()
          p.draw(battleship)
          p2.draw(battleship)
          pygame.display.update()
 
               
