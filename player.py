import pygame
import numpy as np
import pandas as pd
class Player():
        def __init__(self,x,y,width,height,color):
                self.x=x
                self.y=y
                self.width=width
                self.height=height
                self.color=color
                self.rect=(x,y,width,height)
                self.vel=4
                self.myship=pd.DataFrame(np.array([['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']]))
                self.myatack=pd.DataFrame(np.array([['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']]))
                self.posship=[]
                self.posatack=[]
        def draw(self,win):
                pygame.draw.rect(win,self.color,self.rect)
        def move(self):
                keys=pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                        self.x-=self.vel
                if keys[pygame.K_RIGHT]:
                        self.x+=self.vel
                if keys[pygame.K_UP]:
                        self.y-=self.vel
                if keys[pygame.K_DOWN]:
                        self.y+=self.vel
                self.update()
        def update(self):
                self.rect = (self.x,self.y,self.width,self.height)
        def getmyship(self):
                return self.myship
        def getmyatack(self):
                return self.myatack
        def setmyship(self,mapship):
                self.myship=mapship
        def setmyatack(self,mapatack):
                self.myatack=mapatack
        def getposship(self):
                return self.posship
        def getposatack(self):
                return self.posatack
        def setposship(self,posship):
                self.posship=posship
        def setposatack(self,posatack):
                self.posatack=posatack
