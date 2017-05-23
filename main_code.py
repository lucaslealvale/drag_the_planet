import pygame
import sys
from pygame.locals import *
import random
import math

pygame.init()
tela = pygame.display.set_mode((1200,720))
pygame.display.set_caption('Physics, Morty')
clock = pygame.time.Clock()
#Tomamos 100 pixeis como 1m
v=42
b=0.25
a=b*math.pi
print(a)
cont=0
aa=0

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
morty = pygame.image.load("morty.png").convert_alpha()
morty=pygame.transform.scale(morty, (87,240))
play=pygame.transform.scale(play, (100,100))
portais=["portal_sprite0.png","portal_sprite1.png","portal_sprite2.png","portal_sprite3.png","portal_sprite4.png","portal_sprite5.png"]
caixa_i=pygame.transform.scale(caixa_i, (100,105))
caixa=caixa(50,615)
#100 670
lugar=lugar(120)
playing = True

def simula(vx,vy,caixa,lugar):
    aa=0
    cont=0
    while True:
        print(aa)
        print()
        print(cont)
        print(portais[cont])
        if aa==5:
            if cont==5:
                cont=-1
            cont=cont+1
        aa=aa+1
        if aa==6:
            aa=0
        portal=pygame.image.load(portais[cont]).convert_alpha()
        portal=pygame.transform.scale(portal,(200,200))
    
        tela.blit(portal,(1000,520))
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
    if aa==5:
        if cont==5:
            cont=-1
        cont=cont+1
    aa=aa+1
    if aa==6:
        aa=0
    portal=pygame.image.load(portais[cont]).convert_alpha()
    portal=pygame.transform.scale(portal,(200,200))
    
    tela.blit(portal,(1000,520))
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
    #desenha vetor
    pygame.draw.line(fundo,(255,0,0),(100,670),(100+v*5*math.cos(a),670-v*5*math.sin(a)),2)
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
                vx=v*math.cos(a)
                vy=-v*math.sin(a)
                simula(vx,vy,caixa,lugar)
            if event.key==K_RIGHT:
                b=b+0.05
                a=math.pi*b
            if event.key==K_LEFT:
                b=b-0.05
                a=math.pi*b
        if event.type == pygame.QUIT:
            playing=False
            pygame.quit()
            quit()




    
    tela.blit(caixa_i,(caixa.x,caixa.y))
    pygame.display.update()
    clock.tick(60)
