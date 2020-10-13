#Libraries
import pygame

#server loop
def server():
     serv=pygame.display.set_mode((1152,700))
     running_server=True
     while running_server:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running_server=False
                

        serv.fill((255,0,0))
        pygame.display.update()
