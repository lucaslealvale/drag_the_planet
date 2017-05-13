import pygame
import sys
from pygame.locals import *
import random

pygame.init()
tela = pygame.display.set_mode((1200,720))
pygame.display.set_caption('Physics, Morty')
clock = pygame.time.Clock()
#Tomamos 100 pixeis como 1m
vx=30
vy=-30
class caixa:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy
class lugar:
    def __init__(self,gravidade):
        self.g=gravidade       

fundo = pygame.image.load("fundo.jpg").convert()
caixa_i = pygame.image.load("caixa.png").convert_alpha()
play = pygame.image.load("play.png").convert_alpha()
play=pygame.transform.scale(play, (100,100))
caixa_i=pygame.transform.scale(caixa_i, (100,105))
caixa=caixa(50,615)
lugar=lugar(120)
playing = True
def simula(vx,vy,caixa,lugar):
    while True:
        tela.blit(fundo,(0,0))
        tela.blit(play,(1200,720))
        caixa.move(vx,vy)
        
        #gravidade e atrito
        if caixa.y>=615:
            print(caixa.y)
            caixa.y=615
            tela.blit(caixa_i,(caixa.x,caixa.y))
            pygame.display.update()
            vx=0
            if vy>0:
                vy=0
            break
        else:
            vy=vy+(lugar.g/60)
        tela.blit(caixa_i,(caixa.x,caixa.y))
        pygame.display.update()
        clock.tick(60)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==K_SPACE:
                    caixa.x=50
                    caixa.y=615
                    return


while playing: 
    tela.blit(fundo,(0,0))
    tela.blit(play,(30,50))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key==K_SPACE:

                simula(vx,vy,caixa,lugar)
        if event.type == pygame.QUIT:
            playing=False
            pygame.quit()
            quit()




    
    tela.blit(caixa_i,(caixa.x,caixa.y))
    pygame.display.update()
    clock.tick(60)
