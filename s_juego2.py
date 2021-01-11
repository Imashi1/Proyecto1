def juego():
     """Pantalla del juego, con botones para seleccionar barcos, misiles, confirmar jugada, etc"""
     import pygame
     import numpy as np
     import pandas as pd
     import sys
     import funcionesgenerales
     from player import Player
     import random
     battleship=pygame.display.set_mode((1152,700))
     txt1=funcionesgenerales.Animacion('img/debescolocarbarcos/',400,550)
     txt2=funcionesgenerales.Animacion('img/cantidaddeestosbarcosagotados/',400,550)
     txt3=funcionesgenerales.Animacion('img/debescolocarmisiles/',400,550)
     ganaste=funcionesgenerales.Animacion('img/ganaste/',400,60)
     perdiste=funcionesgenerales.Animacion('img/perdiste/',400,60)
     explos=funcionesgenerales.Animacion('img/explosion/',300,300)
     advertencia=0
     """se crea un cursor para el juego"""
     cursor1=funcionesgenerales.Cursor()
     """carga sonido para el boton"""
     sonidoboton=pygame.mixer.Sound('sound/boton.wav')
     sonidoexplosion=pygame.mixer.Sound('sound/expl.mp3')
     sonidolanzar=pygame.mixer.Sound('sound/lanzar.mp3')
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
     marcador1=pygame.image.load('img/contadores/azul/azul.png')
     marcador2=pygame.image.load('img/contadores/rojo/rojo.png')
     marcador3=pygame.image.load('img/contadores/negro/negro.png')
     p=Player(0,0,50,50,(255,0,0),True)
     p2=Player(100,100,50,50,(0,0,255),False)

     
     dfizq=pd.DataFrame(np.array([['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']]))
     dfder=pd.DataFrame(np.array([['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']]))


     listaizq=[]
     listader=[]     


     explosion=False#
     marcador1anim=False
     marcador2anim=False
     animar1=funcionesgenerales.Animacion('img/contadores/azul/',590,20)
     animar2=funcionesgenerales.Animacion('img/contadores/rojo/',590,50)
     cantidadmaxima=7
     acuerdobarcos=[7,6,5,4,3]
     cuentabarcosespecial=[0,0,0,0,0]

     
     advertencia=0
     partida=True
     fin=0
     adminmusic=funcionesgenerales.Soundtrack(['music/Big Trap 24-12-2020 07-08.mp3','music/Come Fly Away 30-12-2020 11-56.mp3'])
     adminmusic.reproducir()
     cuentabarcosizq=0
     cuentabarcosder=0
     cuentamisilesizq=0
     cuentamisilesder=0

     
     barcomoviendo=False
     misilmoviendo=False
     finalgame=False
     estados=[True,False]
     dimx=10
     dimy=10
     ############################################################
     tamanhos=[1,2,3,4,5]
     
     ############################################################
     running_juego=True
     while running_juego:
          adminmusic.circular()
          if finalgame==False and (p.getnrobloques()==0 or p2.getnrobloques()==0) and (p.getponersolobarcos()==False and p2.getponersolobarcos()==False):
               p.setfin(True)
               finalgame=True
               if p.getnrobloques()==0 and p2.getnrobloques()!=0:
                    perdiste.activar()
                    fin=1
               elif p.getnrobloques()!=0 and p2.getnrobloques()==0:
                    ganaste.activar()
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
                              listaizq[cuentabarcosizq-1].rotar(90)
                              
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
                              del listader[cuentamisilesder-1]
                              cuentamisilesder=cuentamisilesder-1
                         elif p.getnromisiles()==cuentamisilesder:
                              listader.append(funcionesgenerales.Barco(imagenmisilb,imagenmisilb,1,1,0))
                              cuentamisilesder=cuentamisilesder+1
                              misilmoviendo=True
                    if cursor1.colliderect(botonmisil.rect)and(p.getponersolobarcos()==True):
                         advertencia=1
                         txt1.activar()


                         
                    """boton para crear un barco de tipo1"""
                    if cursor1.colliderect(crearbarco1.rect)and(p.getmiturno()==True)and(p.getponersolobarcos()==True):
                         if barcomoviendo:
                              """se elimina el "barco actual"""
                              barcomoviendo=False
                              cuentabarcosespecial[listaizq[cuentabarcosizq-1].gettipobarco()-1]=cuentabarcosespecial[listaizq[cuentabarcosizq-1].gettipobarco()-1]-1
                              del listaizq[cuentabarcosizq-1]
                              cuentabarcosizq=cuentabarcosizq-1
                         elif p.getnrobarcos()+cantidadmaxima>cuentabarcosizq and cuentabarcosespecial[0]<acuerdobarcos[0]:
                              """se crea un nuevo barco"""
                              listaizq.append(funcionesgenerales.Barco(imagenbarco1,imagenbarco1,1,1,1))
                              cuentabarcosizq=cuentabarcosizq+1
                              cuentabarcosespecial[0]=cuentabarcosespecial[0]+1
                              barcomoviendo=True
                         else:
                              advertencia=2
                              txt2.activar()


                              
                    """boton para crear un barco de tipo2"""
                    if cursor1.colliderect(crearbarco2.rect)and(p.getmiturno()==True)and(p.getponersolobarcos()==True):
                         if barcomoviendo:
                              barcomoviendo=False
                              cuentabarcosespecial[listaizq[cuentabarcosizq-1].gettipobarco()-1]=cuentabarcosespecial[listaizq[cuentabarcosizq-1].gettipobarco()-1]-1
                              del listaizq[cuentabarcosizq-1]
                              cuentabarcosizq=cuentabarcosizq-1
                         elif p.getnrobarcos()+cantidadmaxima>cuentabarcosizq and cuentabarcosespecial[1]<acuerdobarcos[1]:
                              listaizq.append(funcionesgenerales.Barco(imagenbarco2,imagenbarco2,1,1,2))
                              cuentabarcosizq=cuentabarcosizq+1
                              cuentabarcosespecial[1]=cuentabarcosespecial[1]+1
                              barcomoviendo=True
                         else:
                              advertencia=2
                              txt2.activar()


                              
                    """boton para crear un barco de tipo3"""
                    if cursor1.colliderect(crearbarco3.rect)and(p.getmiturno()==True)and(p.getponersolobarcos()==True):
                         if barcomoviendo:
                              barcomoviendo=False
                              cuentabarcosespecial[listaizq[cuentabarcosizq-1].gettipobarco()-1]=cuentabarcosespecial[listaizq[cuentabarcosizq-1].gettipobarco()-1]-1
                              del listaizq[cuentabarcosizq-1]
                              cuentabarcosizq=cuentabarcosizq-1
                         elif p.getnrobarcos()+cantidadmaxima>cuentabarcosizq and cuentabarcosespecial[2]<acuerdobarcos[2]:
                              listaizq.append(funcionesgenerales.Barco(imagenbarco3,imagenbarco3,1,1,3))
                              cuentabarcosizq=cuentabarcosizq+1
                              cuentabarcosespecial[2]=cuentabarcosespecial[2]+1
                              barcomoviendo=True
                         else:
                              advertencia=2
                              txt2.activar()


                              
                    """boton para crear un barco de tipo4"""
                    if cursor1.colliderect(crearbarco4.rect)and(p.getmiturno()==True)and(p.getponersolobarcos()==True):
                         if barcomoviendo:
                              barcomoviendo=False
                              cuentabarcosespecial[listaizq[cuentabarcosizq-1].gettipobarco()-1]=cuentabarcosespecial[listaizq[cuentabarcosizq-1].gettipobarco()-1]-1
                              del listaizq[cuentabarcosizq-1]
                              cuentabarcosizq=cuentabarcosizq-1
                         elif p.getnrobarcos()+cantidadmaxima>cuentabarcosizq and cuentabarcosespecial[3]<acuerdobarcos[3]:
                              listaizq.append(funcionesgenerales.Barco(imagenbarco4,imagenbarco4,1,1,4))
                              cuentabarcosizq=cuentabarcosizq+1
                              cuentabarcosespecial[3]=cuentabarcosespecial[3]+1
                              barcomoviendo=True
                         else:
                              advertencia=2
                              txt2.activar()


                              
                    """boton para crear un barco de tipo5"""
                    if cursor1.colliderect(crearbarco5.rect)and(p.getmiturno()==True)and(p.getponersolobarcos()==True):
                         if barcomoviendo:
                              barcomoviendo=False
                              cuentabarcosespecial[listaizq[cuentabarcosizq-1].gettipobarco()-1]=cuentabarcosespecial[listaizq[cuentabarcosizq-1].gettipobarco()-1]-1
                              del listaizq[cuentabarcosizq-1]
                              cuentabarcosizq=cuentabarcosizq-1
                         elif p.getnrobarcos()+cantidadmaxima>cuentabarcosizq and cuentabarcosespecial[4]<acuerdobarcos[4]:
                              listaizq.append(funcionesgenerales.Barco(imagenbarco5,imagenbarco5,1,1,5))
                              cuentabarcosizq=cuentabarcosizq+1
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
                    if cuentabarcosizq>0:
                         if cursor1.colliderect(listaizq[cuentabarcosizq-1].rect)and(listaizq[cuentabarcosizq-1].getconfirmado()==False):
                              if barcomoviendo:
                                   barcomoviendo=False
                                   listaizq[cuentabarcosizq-1].mover(cursor1,54,[10,100],barcomoviendo,10,10)
                                   if listaizq[cuentabarcosizq-1].superposicionb2(listaizq,botonconfirmarjugada):
                                        barcomoviendo=True
                              else:
                                   barcomoviendo=True






                                   
                    """trabaja con el estado misil en movimiento y corrige la posicion del misil
                    a una valida, en caso de que el misil no este en movimiento"""
                    if cuentamisilesder>0:
                         if cursor1.colliderect(listader[cuentamisilesder-1].rect)and(listader[cuentamisilesder-1].getconfirmado()==False)and(p.getnromisiles()!=cuentamisilesder):
                              if misilmoviendo:
                                   misilmoviendo=False
                                   listader[cuentamisilesder-1].mover(cursor1,54,[590,100],misilmoviendo,10,10)
                                   if listader[cuentamisilesder-1].superposicionm2(listader,botonconfirmarjugada):
                                        misilmoviendo=True
                              else:
                                   misilmoviendo=True




                                   
                    """se actualizan los mapas, ultimas posiciones, de el jugador de este codigo"""
                    if cursor1.colliderect(botonconfirmarjugada.rect)and(p.getmiturno()==True)and((p.getnrobarcos()+cantidadmaxima==cuentabarcosizq and barcomoviendo==False) or (p.getnromisiles()+1==cuentamisilesder and misilmoviendo==False)):
                         if cuentabarcosizq>0 and p.getnrobarcos()+cantidadmaxima==cuentabarcosizq:
                              for i in range(p.getnrobarcos(),p.getnrobarcos()+cantidadmaxima):
                                   pos=listaizq[i].obtenerposicion(54,[10,100],[0,0],10,10)
                                   for x in pos:
                                        """se marcan posiciones ocupadas al mapa de mis barcos"""
                                        dfizq.iloc[x[1]][x[0]]='◘'
                                   listaizq[i].setconfirmado(True)
                                   p.setnrobloques(p.getnrobloques()+len(pos))
                              cuentabarcosespecial=[0,0,0,0,0]

                         if cuentamisilesder>0:
                              pos2=listader[cuentamisilesder-1].obtenerposicion(54,[590,100],[0,0],10,10)
                              for x in pos2:
                                   """se marcan posiciones ocupadas al mapa de mis ataques"""
                                   auxpos=dfder.iloc[x[1]][x[0]]
                                   dfder.iloc[x[1]][x[0]]='☼'
                              listader[cuentamisilesder-1].setconfirmado(True)
                              sonidolanzar.play()

                         if cuentabarcosizq>0 and cuentamisilesder>0:
                              for pos in pos2:
                                   if auxpos!='-':                                          
                                        listader[cuentamisilesder-1]=funcionesgenerales.Barco(imagenmisilr,imagenmisilr,54*pos[0]+600,54*pos[1]+110,0)
                                        sonidoexplosion.play()
                                        explosion=True
                                        explos.setpos(54*pos[0]+600-50,54*pos[1]+110-50)
                                        explos.activar()
                                        p2.restarnrobloques(1)
                                        marcador2anim=True
                                        animar2.activar()
                         p.increnroturno()
                         if p.getponersolobarcos():
                              """se actualiza mapa mis barcos, al jugador de este codigo"""
                              p.increnrobarcos(cantidadmaxima)
                              p.setponersolobarcos(False)
                         else:
                              """se actualiza mapa mis ataques, al juagor de este codigo"""
                              p.increnromisiles()
                         p.setmiturno(False)
                         p2.setmiturno(True)
                         marcador1anim=True
                         
          """se pone color de fondo de la pantalla"""
          battleship.fill((50,150,200))
          cursor1.update()
          """se muestran los mapas del juego"""
          fondomapai.update1(0.3,battleship)
          fondomapad.update1(0.3,battleship)
          battleship.blit(marcador1,(590,20))
          battleship.blit(marcador2,(590,50))
          battleship.blit(marcador3,(890,20))
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
                    txt1.update2(0.02,battleship)
               else:
                    advertencia=0
          if advertencia==2:
               if txt2.getiniciar()==True:
                    txt2.update2(0.02,battleship)
               else:
                    advertencia=0
          if advertencia==3:
               if txt3.getiniciar()==True:
                    txt3.update2(0.02,battleship)
               else:
                    advertencia=0
          """se muestran los barcos que estan en la lista de barcos"""
          for barco in listaizq:
               barco.update(battleship,cursor1)
          """mueve el barco dependiendo del estado barcomoviendo"""
          if barcomoviendo:
               listaizq[cuentabarcosizq-1].mover(cursor1,54,[10,100],barcomoviendo,10,10)
          """se muestran los misiles que estan en la lista de misiles"""
          for misil in listader:
               misil.update(battleship,cursor1)
          if fin==1:
               perdiste.update1(0.2,battleship)
          if fin==2:
               ganaste.update1(0.2,battleship)
          if fin==3:
                battleship.blit(mifuente2.render("EMPATE",0,(255,255,255)),(400,400))
          """mueve el misil dependiendo del estado misil moviendo"""
          if misilmoviendo:
               listader[cuentamisilesder-1].mover(cursor1,54,[590,100],misilmoviendo,10,10)
          """carga los elementos del update"""
          if explosion==True:
               if explos.getiniciar()==True:
                    explos.update2(0.5,battleship)
               else:
                    explosion=False
          if marcador1anim==True:
               if animar1.getiniciar()==True:
                    animar1.update2(0.4,battleship)
               else:
                    marcador1anim=False
          if marcador2anim==True:
               if animar2.getiniciar()==True:
                    animar2.update2(0.4,battleship)
               else:
                    marcador2anim=False
               
               
          pygame.display.update()
          ##################################################################
          auxcuentamisiles=cuentamisilesizq
          while p2.getmiturno()==True:
               if p2.getponersolobarcos()==True:
                    tamsombra=tamanhos[random.randint(0,4)]
                    direchorizontal=estados[random.randint(0,1)]
                    if direchorizontal==True:
                         indices=[random.randint(0,dimx-tamsombra),random.randint(0,dimy-1)]
                         #poscursor=[indices[0]*54+590,indices[1]*54+100]
                         estavacio=True
                         for x in range(indices[0],indices[0]+tamsombra):
                                   if dfder.iloc[x][indices[1]]!='-':
                                        estavacio=False
                                        break
                         if estavacio:
                              for x in range(indices[0],indices[0]+tamsombra):
                                   dfder.iloc[x][indices[1]]='◘'
                              cuentabarcosder=cuentabarcosder+1
                              p2.setnrobloques(p2.getnrobloques()+tamsombra)
                         else:
                              continue
                    else:
                         indices=[random.randint(0,dimx-1),random.randint(0,dimy-tamsombra)]
                         #poscursor=[indices[0]*54+590,indices[1]*54+100]
                         estavacio=True
                         for y in range(indices[1],indices[1]+tamsombra):
                                   if dfder.iloc[indices[1]][y]!='-':
                                        estavacio=False
                                        break
                         if estavacio:
                              for y in range(indices[1],indices[1]+tamsombra):
                                   dfder.iloc[indices[0]][y]='◘'
                              cuentabarcosder=cuentabarcosder+1
                              p2.setnrobloques(p2.getnrobloques()+tamsombra)
                         else:
                              continue
               else:
                    indices=[random.randint(0,dimx-1),random.randint(0,dimy-1)]
                    auxpos=dfizq.iloc[indices[0]][indices[1]]
                    if cuentamisilesizq==auxcuentamisiles and (dfizq.iloc[indices[0]][indices[1]]=='◘' or dfizq.iloc[indices[0]][indices[1]]=='-'):
                         dfizq.iloc[indices[0]][indices[1]]='☼'
                         listaizq.append(funcionesgenerales.Barco(imagenmisilb,imagenmisilb,54*indices[1]+20,54*indices[0]+110))
                         if auxpos=='◘':
                              sonidoexplosion.play()
                              explosion=True
                              explos.setpos(54*indices[1]+20-50,54*indices[0]+110-50)
                              explos.activar()
                              p.restarnrobloques(1)
                              marcador1anim=True
                              animar1.activar()
                              listaizq=listaizq[:-1]
                              listaizq.append(funcionesgenerales.Barco(imagenmisilr,imagenmisilr,54*indices[1]+20,54*indices[0]+110))
                         cuentamisilesizq=cuentamisilesizq+1
               if cuentabarcosder==cantidadmaxima and p2.getponersolobarcos()==True:
                    p2.setmiturno(False)
                    p.setmiturno(True)
                    p2.setponersolobarcos(False)
               if cuentamisilesizq!=auxcuentamisiles and p2.getponersolobarcos()==False:
                    p2.setmiturno(False)
                    p.setmiturno(True)
     adminmusic.sdetener()
