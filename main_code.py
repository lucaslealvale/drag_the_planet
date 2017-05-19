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
a=0
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

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==K_SPACE:
                    caixa.x=50
                    caixa.y=615
                    return
                    
                
            
        
        #gravidade e atrito
        if caixa.y>=615:
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
    #mostra gravidade
    
    myfont = pygame.font.SysFont("monospace", 30)
    pygame.draw.line(fundo,(0,0,0),(100,670),(1200,670),2)
    pygame.draw.line(fundo,(0,0,0),(100,670),(100,0),2)
    if a==1:
        
        pygame.draw.line(fundo,(0,0,0),(200,670),(200,0),1)
        pygame.draw.line(fundo,(0,0,0),(300,670),(300,0),1)
        pygame.draw.line(fundo,(0,0,0),(400,670),(400,0),1)
        pygame.draw.line(fundo,(0,0,0),(500,670),(500,0),1)
        pygame.draw.line(fundo,(0,0,0),(600,670),(600,0),1)
        pygame.draw.line(fundo,(0,0,0),(700,670),(700,0),1)
        pygame.draw.line(fundo,(0,0,0),(800,670),(800,0),1)
        pygame.draw.line(fundo,(0,0,0),(900,670),(900,0),1)
        pygame.draw.line(fundo,(0,0,0),(1000,670),(1000,0),1)
        pygame.draw.line(fundo,(0,0,0),(1100,670),(1100,0),1)
        pygame.draw.line(fundo,(0,0,0),(1200,670),(1200,0),1)
        pygame.draw.line(fundo,(0,0,0),(100,570),(1200,570),1)
        pygame.draw.line(fundo,(0,0,0),(100,470),(1200,470),1)
        pygame.draw.line(fundo,(0,0,0),(100,370),(1200,370),1)
        pygame.draw.line(fundo,(0,0,0),(100,270),(1200,270),1)
        pygame.draw.line(fundo,(0,0,0),(100,170),(1200,170),1)
        pygame.draw.line(fundo,(0,0,0),(100,70),(1200,70),1)
    elif a==2:
        fundo = pygame.image.load("fundo.jpg").convert()
        a=0
    # render text
    label = myfont.render("Gravidade: {0}".format(lugar.g), 1, (0,0,0))
    label1 = myfont.render("1m".format(lugar.g), 1, (0,0,0))
    tela.blit(label, (200, 100))
    #label = myfont.render("Gravidade: {0}".format(lugar.g), 1, (0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key==K_g:
                a=(a+1)%3
            if event.key==K_UP:
                lugar.g=lugar.g+10
            if event.key==K_DOWN:
                lugar.g=lugar.g-10
            if event.key==K_SPACE:

                simula(vx,vy,caixa,lugar)
        if event.type == pygame.QUIT:
            playing=False
            pygame.quit()
            quit()




    
    tela.blit(caixa_i,(caixa.x,caixa.y))
    pygame.display.update()
    clock.tick(60)
