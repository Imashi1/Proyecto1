def juego(host,port):
     """Pantalla del juego, con botones para seleccionar barcos, misiles, confirmar jugada, etc"""
     import pygame
     import numpy as np
     import pandas as pd
     import sys
     import funcionesgenerales
     from player import Player
     from network import Network
     battleship=pygame.display.set_mode((1152,700))
     txt1=funcionesgenerales.Animacion('img/debescolocarbarcos/',500,60)
     txt2=funcionesgenerales.Animacion('img/cantidaddeestosbarcosagotados/',500,60)
     txt3=funcionesgenerales.Animacion('img/debescolocarmisiles/',500,60)
     ganaste=funcionesgenerales.Animacion('img/ganaste/',200,60)
     perdiste=funcionesgenerales.Animacion('img/perdiste/',200,60)
     advertencia=0
     """se crea un cursor para el juego"""
     cursor1=funcionesgenerales.Cursor()
     """carga sonido para el boton"""
     sonidoboton=pygame.mixer.Sound('sound/boton.wav')
     sonidoexplosion=pygame.mixer.Sound('sound/expl.wav')
     """se carga el fondo de los mapas"""
     fondomapai=funcionesgenerales.Animacion('img/mapa/',10,100)
     fondomapad=funcionesgenerales.Animacion('img/mapa/',590,100)
     fondomapai.activar()
     fondomapad.activar()
     """se crean los botones regresar y confirmar jugada"""
     btn_1v1=pygame.image.load('img/atras.png')
     btn_1v12=pygame.image.load('img/atras2.png')
     boton1=funcionesgenerales.Boton(btn_1v1,btn_1v12,10,10)
     btn_confirmar=pygame.image.load('img/btnconfirmarjugada.png')
     btn_confirmar2=pygame.image.load('img/btnconfirmarjugada2.png')
     botonconfirmarjugada=funcionesgenerales.Boton(btn_confirmar,btn_confirmar2,500,655)
     """texto es mi turno ó esperando jugada..."""
     mifuente=pygame.font.SysFont("Consolas",15)
     miturno=mifuente.render("es mi turno",0,(255,255,255))
     esperando=mifuente.render("esperando...",0,(255,255,255))
     mifuente2=pygame.font.SysFont("Consolas",100)
     """carga de imagenes de los barcos y misil a utilizar"""
     imagenbarco1=pygame.image.load('img/barco53.png')
     imagenbarco2=pygame.image.load('img/barco31.png')
     imagenbarco3=pygame.image.load('img/barco32.png')
     imagenbarco4=pygame.image.load('img/barco33.png')
     imagenbarco5=pygame.image.load('img/barco43.png')
     imagenmisilb=pygame.image.load('img/misilb.png')
     imagenmisilr=pygame.image.load('img/misilr.png')
     """carga de imagenes de los botones seleccionar barco"""
     btn_crearbarco1=pygame.image.load('img/boton1listo.png')
     btn_crearbarco1_2=pygame.image.load('img/boton1listo_2.png')
     btn_crearbarco2=pygame.image.load('img/boton2listo.png')
     btn_crearbarco2_2=pygame.image.load('img/boton2listo_2.png')
     btn_crearbarco3=pygame.image.load('img/boton3listo.png')
     btn_crearbarco3_2=pygame.image.load('img/boton3listo_2.png')
     btn_crearbarco4=pygame.image.load('img/boton4listo.png')
     btn_crearbarco4_2=pygame.image.load('img/boton4listo_2.png')
     btn_crearbarco5=pygame.image.load('img/boton5listo.png')
     btn_crearbarco5_2=pygame.image.load('img/boton5listo_2.png')
     btn_misil=pygame.image.load('img/btn_misil.png')
     btn_misil2=pygame.image.load('img/btn_misil2.png')
     """creacion de botones seleccionar barco, seleccionar misil"""
     crearbarco1=funcionesgenerales.Boton(btn_crearbarco1,btn_crearbarco1_2,10,67)
     crearbarco2=funcionesgenerales.Boton(btn_crearbarco2,btn_crearbarco2_2,123,61)
     crearbarco3=funcionesgenerales.Boton(btn_crearbarco3,btn_crearbarco3_2,236,61)
     crearbarco4=funcionesgenerales.Boton(btn_crearbarco4,btn_crearbarco4_2,349,61)
     crearbarco5=funcionesgenerales.Boton(btn_crearbarco5,btn_crearbarco5_2,462,61)
     botonmisil=funcionesgenerales.Boton(btn_misil,btn_misil2,850,57)
     """creacion de un objeto network como asistente para enviar la data al servidor"""
     n=Network(host,port)
     """creamos el primer jugador "de este codigo", y lo mantenemos
     conectado"""
     p = n.getP()
     if p==-1:
          return -1
     """definimos dataframes para los mapas del jugador de este codigo"""
     df=pd.DataFrame(np.array([['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']]))
     df2=pd.DataFrame(np.array([['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']]))
     """creamos listas para agregar objetos de barcos y misiles
     incluso de misiles rivales, y asi facilitar la organizacion
     de estos"""
     listabarcos=[]
     listamisiles=[]
     listamisilesrival=[]
     """x"""
     cantidadmaxima=7
     acuerdobarcos=[7,6,5,4,3]
     cuentabarcosespecial=[0,0,0,0,0]
     advertencia=0
     partida=True
     fin=0
     """inicializacion de contadores"""
     cuentabarcos=0
     cuentamisiles=0
     """estados para saber si se mueve o no un barco o misil"""
     barcomoviendo=False
     misilmoviendo=False
     perdiste.activar()
     ganaste.activar()
     """lista para agregar la anterior posicion"""
     antpos=[]
     running_juego=True
     while running_juego:
          """se crea un segundo jugador "del otro lado" y se mantiene conectado"""
          p2 = n.send(p)
          if p2.gethacercambio()==False:
               if p2.getmiturno()==True:
                    p.setmiturno(False)
               else:
                    p.setmiturno(True)
               p.sethacercambio(False)
          """muestra el ataque del jugador del otro lado en el jugador de este codigo
          ademas difiere si el misil coliciono con el barco del jugador de este codigo"""
          if antpos!=p2.getposatack():
               for pos in p2.getposatack():
                    if p.getmyship().iloc[pos[1]][pos[0]]!='-':
                         listamisilesrival.append(funcionesgenerales.Barco(imagenmisilr,imagenmisilr,54*pos[0]+20,54*pos[1]+110))
                         sonidoexplosion.play()
                         p.restarnrobloques(1)
                    else:
                         listamisilesrival.append(funcionesgenerales.Barco(imagenmisilb,imagenmisilb,54*pos[0]+20,54*pos[1]+110))
               antpos=p2.getposatack()
          if (p.getnroturno()==p2.getnroturno())and(p.getnrobloques()==0 or p2.getnrobloques()==0) and (p.getponersolobarcos()==False and p2.getponersolobarcos()==False):
               if p.getnrobloques()==0 and p2.getnrobloques()!=0:
                    fin=1
               elif p.getnrobloques()!=0 and p2.getnrobloques()==0:
                    fin=2
               else:
                    fin=3
          """bucle para detectar los eventos"""
          for event in pygame.event.get():
               """finaliza el programa del juego"""
               if event.type==pygame.QUIT:
                    running_juego=False
                    pygame.quit()
                    sys.exit()
               """permite la rotacion del barco que se esta usando"""
               if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                         if barcomoviendo:
                              listabarcos[cuentabarcos-1].rotar(90)
                              
               """se devuele a la pantalla del ingresar servidor"""
               if event.type==pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton1.rect):
                         sonidoboton.play()
                         running_juego=False
               if event.type==pygame.MOUSEBUTTONUP:
                    """boton para crear un nuevo misil"""
                    if cursor1.colliderect(botonmisil.rect)and(p.getmiturno()==True)and(p.getponersolobarcos()==False):
                         if misilmoviendo:
                              misilmoviendo=False
                              del listamisiles[cuentamisiles-1]
                              cuentamisiles=cuentamisiles-1
                         elif p.getnromisiles()==cuentamisiles:
                              listamisiles.append(funcionesgenerales.Barco(imagenmisilb,imagenmisilb,1,1,0))
                              cuentamisiles=cuentamisiles+1
                              misilmoviendo=True
                    if cursor1.colliderect(botonmisil.rect)and(p.getponersolobarcos()==True):
                         advertencia=1
                         txt1.activar()
                    """boton para crear un barco de tipo1"""
                    if cursor1.colliderect(crearbarco1.rect)and(p.getmiturno()==True)and(p.getponersolobarcos()==True):
                         if barcomoviendo:
                              """se elimina el "barco actual"""
                              barcomoviendo=False
                              cuentabarcosespecial[listabarcos[cuentabarcos-1].gettipobarco()-1]=cuentabarcosespecial[listabarcos[cuentabarcos-1].gettipobarco()-1]-1
                              del listabarcos[cuentabarcos-1]
                              cuentabarcos=cuentabarcos-1
                         elif p.getnrobarcos()+cantidadmaxima>cuentabarcos and cuentabarcosespecial[0]<acuerdobarcos[0]:
                              """se crea un nuevo barco"""
                              listabarcos.append(funcionesgenerales.Barco(imagenbarco1,imagenbarco1,1,1,1))
                              cuentabarcos=cuentabarcos+1
                              cuentabarcosespecial[0]=cuentabarcosespecial[0]+1
                              barcomoviendo=True
                         else:
                              advertencia=2
                              txt2.activar()
                    """boton para crear un barco de tipo2"""
                    if cursor1.colliderect(crearbarco2.rect)and(p.getmiturno()==True)and(p.getponersolobarcos()==True):
                         if barcomoviendo:
                              barcomoviendo=False
                              cuentabarcosespecial[listabarcos[cuentabarcos-1].gettipobarco()-1]=cuentabarcosespecial[listabarcos[cuentabarcos-1].gettipobarco()-1]-1
                              del listabarcos[cuentabarcos-1]
                              cuentabarcos=cuentabarcos-1
                         elif p.getnrobarcos()+cantidadmaxima>cuentabarcos and cuentabarcosespecial[1]<acuerdobarcos[1]:
                              listabarcos.append(funcionesgenerales.Barco(imagenbarco2,imagenbarco2,1,1,2))
                              cuentabarcos=cuentabarcos+1
                              cuentabarcosespecial[1]=cuentabarcosespecial[1]+1
                              barcomoviendo=True
                         else:
                              advertencia=2
                              txt2.activar()
                    """boton para crear un barco de tipo3"""
                    if cursor1.colliderect(crearbarco3.rect)and(p.getmiturno()==True)and(p.getponersolobarcos()==True):
                         if barcomoviendo:
                              barcomoviendo=False
                              cuentabarcosespecial[listabarcos[cuentabarcos-1].gettipobarco()-1]=cuentabarcosespecial[listabarcos[cuentabarcos-1].gettipobarco()-1]-1
                              del listabarcos[cuentabarcos-1]
                              cuentabarcos=cuentabarcos-1
                         elif p.getnrobarcos()+cantidadmaxima>cuentabarcos and cuentabarcosespecial[2]<acuerdobarcos[2]:
                              listabarcos.append(funcionesgenerales.Barco(imagenbarco3,imagenbarco3,1,1,3))
                              cuentabarcos=cuentabarcos+1
                              cuentabarcosespecial[2]=cuentabarcosespecial[2]+1
                              barcomoviendo=True
                         else:
                              advertencia=2
                              txt2.activar()
                    """boton para crear un barco de tipo4"""
                    if cursor1.colliderect(crearbarco4.rect)and(p.getmiturno()==True)and(p.getponersolobarcos()==True):
                         if barcomoviendo:
                              barcomoviendo=False
                              cuentabarcosespecial[listabarcos[cuentabarcos-1].gettipobarco()-1]=cuentabarcosespecial[listabarcos[cuentabarcos-1].gettipobarco()-1]-1
                              del listabarcos[cuentabarcos-1]
                              cuentabarcos=cuentabarcos-1
                         elif p.getnrobarcos()+cantidadmaxima>cuentabarcos and cuentabarcosespecial[3]<acuerdobarcos[3]:
                              listabarcos.append(funcionesgenerales.Barco(imagenbarco4,imagenbarco4,1,1,4))
                              cuentabarcos=cuentabarcos+1
                              cuentabarcosespecial[3]=cuentabarcosespecial[3]+1
                              barcomoviendo=True
                         else:
                              advertencia=2
                              txt2.activar()
                    """boton para crear un barco de tipo5"""
                    if cursor1.colliderect(crearbarco5.rect)and(p.getmiturno()==True)and(p.getponersolobarcos()==True):
                         if barcomoviendo:
                              barcomoviendo=False
                              cuentabarcosespecial[listabarcos[cuentabarcos-1].gettipobarco()-1]=cuentabarcosespecial[listabarcos[cuentabarcos-1].gettipobarco()-1]-1
                              del listabarcos[cuentabarcos-1]
                              cuentabarcos=cuentabarcos-1
                         elif p.getnrobarcos()+cantidadmaxima>cuentabarcos and cuentabarcosespecial[4]<acuerdobarcos[4]:
                              listabarcos.append(funcionesgenerales.Barco(imagenbarco5,imagenbarco5,1,1,5))
                              cuentabarcos=cuentabarcos+1
                              cuentabarcosespecial[4]=cuentabarcosespecial[4]+1
                              barcomoviendo=True
                         else:
                              advertencia=2
                              txt2.activar()
                    if ((cursor1.colliderect(crearbarco1.rect)==True or cursor1.colliderect(crearbarco2.rect)==True or cursor1.colliderect(crearbarco3.rect)==True or cursor1.colliderect(crearbarco4.rect)==True or cursor1.colliderect(crearbarco5.rect)==True) and (p.getponersolobarcos()==False)):
                         advertencia=3
                         txt3.activar()
                    """trabaja con el estado de barco moviendo y corrige la posicion del barco
                    a una valida, en caso de que el barco no este en movimiento"""
                    if cuentabarcos>0:
                         if cursor1.colliderect(listabarcos[cuentabarcos-1].rect)and(listabarcos[cuentabarcos-1].getconfirmado()==False):
                              if barcomoviendo:
                                   barcomoviendo=False
                                   listabarcos[cuentabarcos-1].mover(cursor1,54,[10,100],barcomoviendo,10,10)
                                   if listabarcos[cuentabarcos-1].superposicionb(listabarcos,listamisiles,listamisilesrival,botonconfirmarjugada):
                                        barcomoviendo=True
                              else:
                                   barcomoviendo=True
                    """trabaja con el estado misil en movimiento y corrige la posicion del misil
                    a una valida, en caso de que el misil no este en movimiento"""
                    if cuentamisiles>0:
                         if cursor1.colliderect(listamisiles[cuentamisiles-1].rect)and(listamisiles[cuentamisiles-1].getconfirmado()==False)and(p.getnromisiles()!=cuentamisiles):
                              if misilmoviendo:
                                   misilmoviendo=False
                                   listamisiles[cuentamisiles-1].mover(cursor1,54,[590,100],misilmoviendo,10,10)
                                   if listamisiles[cuentamisiles-1].superposicionm(listabarcos,listamisiles,listamisilesrival,botonconfirmarjugada):
                                        misilmoviendo=True
                              else:
                                   misilmoviendo=True
                    """se actualizan los mapas, ultimas posiciones, de el jugador de este codigo"""
                    if cursor1.colliderect(botonconfirmarjugada.rect)and(p.getmiturno()==True)and((p.getnrobarcos()+cantidadmaxima==cuentabarcos and barcomoviendo==False) or (p.getnromisiles()+1==cuentamisiles and misilmoviendo==False)):
                         if cuentabarcos>0 and p.getnrobarcos()+cantidadmaxima==cuentabarcos:
                              for i in range(p.getnrobarcos(),p.getnrobarcos()+cantidadmaxima):
                                   pos=listabarcos[i].obtenerposicion(54,[10,100],[0,0],10,10)
                                   for x in pos:
                                        """se marcan posiciones ocupadas al mapa de mis barcos"""
                                        df.iloc[x[1]][x[0]]='◘'
                                   p.setposship(pos)
                                   listabarcos[i].setconfirmado(True)
                              cuentabarcosespecial=[0,0,0,0,0]

                         if cuentamisiles>0:
                              pos2=listamisiles[cuentamisiles-1].obtenerposicion(54,[590,100],[0,0],10,10)
                              for x in pos2:
                                   """se marcan posiciones ocupadas al mapa de mis ataques"""
                                   df2.iloc[x[1]][x[0]]='☼'
                              p.setposatack(pos2)
                              listamisiles[cuentamisiles-1].setconfirmado(True)

                         if cuentabarcos>0 and cuentamisiles>0:
                              for pos in pos2:
                                   if p2.getmyship().iloc[pos[1]][pos[0]]!='-':                                          
                                        listamisiles[cuentamisiles-1]=funcionesgenerales.Barco(imagenmisilr,imagenmisilr,54*pos[0]+600,54*pos[1]+110,0)
                                        sonidoexplosion.play()
                         p.increnroturno()
                         if p.getponersolobarcos():
                              p.setmyship(df)
                              """se actualiza mapa mis barcos, al jugador de este codigo"""
                              p.increnrobarcos(cantidadmaxima)
                              p.setponersolobarcos(False)
                         else:
                              p.setmyatack(df2)
                              """se actualiza mapa mis ataques, al juagor de este codigo"""
                              p.increnromisiles()
                         p.sethacercambio(True)
          """se pone color de fondo de la pantalla"""
          battleship.fill((50,150,200))
          cursor1.update()
          """se muestran los mapas del juego"""
          fondomapai.update1(0.3,battleship)
          fondomapad.update1(0.3,battleship)
          """poner texto de mi turno o en espera"""
          if p.getmiturno()==True:
               battleship.blit(miturno,(900,30))
          else:
               battleship.blit(esperando,(900,30))
          battleship.blit(mifuente.render("Mis bloques restantes: "+str(p.getnrobloques()),0,(255,255,255)),(600,30))
          battleship.blit(mifuente.render("Bloques restantes rival: "+str(p2.getnrobloques()),0,(255,255,255)),(600,60))

          """se muestran los botones de seleccionar barco o misil"""
          crearbarco1.update(battleship,cursor1)
          crearbarco2.update(battleship,cursor1)
          crearbarco3.update(battleship,cursor1)
          crearbarco4.update(battleship,cursor1)
          crearbarco5.update(battleship,cursor1)
          botonmisil.update(battleship,cursor1)
          """se muestra el boton de confirmar jugada, y boton regresar"""
          botonconfirmarjugada.update(battleship,cursor1)
          boton1.update(battleship,cursor1)
          if advertencia==1:
               if txt1.getiniciar()==True:
                    txt1.update2(0.2,battleship)
               else:
                    advertencia=0
          if advertencia==2:
               if txt2.getiniciar()==True:
                    txt2.update2(0.2,battleship)
               else:
                    advertencia=0
          if advertencia==3:
               if txt3.getiniciar()==True:
                    txt3.update2(0.2,battleship)
               else:
                    advertencia=0
          """se muestran los barcos que estan en la lista de barcos"""
          for barco in listabarcos:
               barco.update(battleship,cursor1)
          """mueve el barco dependiendo del estado barcomoviendo"""
          if barcomoviendo:
               listabarcos[cuentabarcos-1].mover(cursor1,54,[10,100],barcomoviendo,10,10)
          """se muestran los misiles que estan en la lista de misiles"""
          for misil in listamisiles:
               misil.update(battleship,cursor1)
          """se muestran los misiles que estan en la lista de misiles del rival"""
          for misil in listamisilesrival:
               misil.update(battleship,cursor1)
          if fin==1:
               perdiste.update1(0.2,battleship)
          if fin==2:
               ganaste.update1(0.2,battleship)
          if fin==3:
                battleship.blit(mifuente2.render("EMPATE",0,(255,255,255)),(400,400))
          """mueve el misil dependiendo del estado misil moviendo"""
          if misilmoviendo:
               listamisiles[cuentamisiles-1].mover(cursor1,54,[590,100],misilmoviendo,10,10)
          """carga los elementos del update"""
          pygame.display.update()
 
               
