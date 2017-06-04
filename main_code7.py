import pygame
import sys
from pygame.locals import *
import random, time
import math
import animation_out_world as ani
import main_code8 as fase8

    
def sete():
    pygame.init()
    tela = pygame.display.set_mode((1200,720))
    pygame.display.set_caption('Physics, Morty')
    clock = pygame.time.Clock()
    #Tomamos 100 pixeis como 1m
    v=42
    b=0.25
    ang=b*math.pi
    a=0
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
    class portal:
        def __init__(self,x,y):
            self.x=x
            self.y=y
    class obs:
        def __init__(self,x,y):
            self.x=x
            self.y=y

    fundo = pygame.image.load("fundo.jpg").convert()
    caixa_i = pygame.image.load("caixa.png").convert_alpha()
    caixa_fixa = pygame.image.load("caixa2.png").convert_alpha()
    caixa_fixa1 = obs(500, 420)

    play = pygame.image.load("play.png").convert_alpha()
    morty = pygame.image.load("morty.png").convert_alpha()
    morty=pygame.transform.scale(morty, (87,240))
    play=pygame.transform.scale(play, (100,100))

    portais=["portal_sprite0.png","portal_sprite1.png","portal_sprite2.png","portal_sprite3.png","portal_sprite4.png","portal_sprite5.png"]
    caixa_i=pygame.transform.scale(caixa_i, (100,105))
    caixa=caixa(100,667.5)
    portal1=portal(1100,620)
    lugar=lugar(150)
    playing = True
    myfont = pygame.font.SysFont("monospace", 30)
    myfont2 = pygame.font.SysFont("monospace", 60)
    label_win=pygame.image.load("ganhou.png")
    label_lose=pygame.image.load("perdeu.png")
    inicio=0
    lvl_7_img=pygame.image.load('lvl_7_img.png')
    enter=pygame.image.load('enter_img.png')
    enter=pygame.transform.scale(enter,(204,128))
    fundinho=pygame.image.load('back_fundo.png')
    meeseeks1=pygame.image.load('meeseeks2.png')
    meeseeks2=pygame.image.load('meeseeks1.png')
    diag_1=pygame.image.load('dialogo_meeseeks5.png')


    def simula(v,caixa,lugar):
        aa=0
        cont=0
        vy=-v*math.sin(ang)
        vx=v*math.cos(ang)
        while True:
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
            tela.blit(caixa_fixa, (400,320))

            #calcula distancia entre caixa e portal
            r=((portal1.x - caixa.x)**2+(portal1.y - caixa.y)**2)**0.5
            d=((caixa_fixa1.x - caixa.x)**2+(caixa_fixa1.y - caixa.y)**2)**0.5
            #colisao real
            
            #print (r)
            #print(caixa.x,caixa.y)
            #print(caixa_fixa1.x,caixa_fixa1.y)
            #print()
            if d<= 150:
                #tela.blit(label_lose,(320,250))
                #tela.blit(caixa_i, (400,500))
                #vx=0
                caixa.x=100
                caixa.y=667.5
                #tela.blit(label_lose,(320,250))
                return
            if r<=150:
                #codigo se ganhou
                tela.blit(label_win,(320,250))
                fase8.oito()
                
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==K_SPACE:
                        time.clock()
                        caixa.x=100
                        caixa.y=667.5
                        return
                        
                    
                
            
            #gravidade e atrito
            if caixa.y>=667.5:
                caixa.y=667.5
                tela.blit(caixa_i,(caixa.x-50,caixa.y-52.5))
                pygame.display.update()
                vx=0
                if vy>0:
                    vy=0
                break
            else:
                vy=vy+(lugar.g/60)
         
            tela.blit(caixa_i,(caixa.x-50,caixa.y-52.5))
            portal=pygame.image.load(portais[cont]).convert_alpha()
            portal=pygame.transform.scale(portal,(200,200))
        
            tela.blit(portal,(1000,520))
            pygame.display.update()
            clock.tick(60)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==K_SPACE:
                        caixa.x=100
                        caixa.y=667.5
                        return


    while playing:
        if inicio==0:
            tela.blit(fundo,(0,0))
            tela.blit(caixa_fixa, (400,320))
            pygame.draw.line(fundo,(255,0,0),(100,667.5),(100+v*5*math.cos(ang),667.5-v*5*math.sin(ang)),2)
            tela.blit(play,(30,50))
            tela.blit(caixa_i,(caixa.x-50,caixa.y-52.5))
            tela.blit(fundinho,(0,0))
            tela.blit(lvl_7_img,(320,200))
            tela.blit(enter,[1000,600])
            tela.blit(meeseeks1,[-15,400])
            tela.blit(diag_1,[0,150])
            
        elif inicio==1:
            tela.blit(fundo,(0,0))
            tela.blit(caixa_fixa, (400,320))
            pygame.draw.line(fundo,(255,0,0),(100,667.5),(100+v*5*math.cos(ang),667.5-v*5*math.sin(ang)),2)
            tela.blit(play,(30,50))
            tela.blit(caixa_i,(caixa.x-50,caixa.y-52.5))
            tela.blit(portal,(1000,520))
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
        
        #tela.blit(portal,(1000,520))
        
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
        label = myfont.render("Gravidade: {0}".format(lugar.g/100), 1, (0,0,0))
        label1 = myfont.render("1m".format(lugar.g), 1, (0,0,0))
        tela.blit(label, (200, 100))
        #desenha vetor
        
        #label = myfont.render("Gravidade: {0}".format(lugar.g), 1, (0,0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==K_g:
                    a=(a+1)%3
                if inicio==0 and event.key==pygame.K_RETURN:
                    inicio=1
                if event.key==K_UP:
                    lugar.g=lugar.g+10
                if event.key==K_DOWN:
                    lugar.g=lugar.g-10
                if event.key==K_SPACE:
                    
                    
                    simula(v,caixa,lugar)
                if lugar.g<0 and event.key==K_SPACE:
                    ani.animation7()
                if event.key==K_a:
                    fundo = pygame.image.load("fundo.jpg").convert()
                    v=v-5
                if event.key==K_s:
                    fundo = pygame.image.load("fundo.jpg").convert()
                    v=v+5
                if event.key==K_LEFT:
                    fundo = pygame.image.load("fundo.jpg").convert()
                    b=b+0.05
                    ang=math.pi*b
                if event.key==K_RIGHT:
                    fundo = pygame.image.load("fundo.jpg").convert()
                    b=b-0.05
                    ang=math.pi*b
                    tela.blit(fundo,(0,0))
                if event.key==K_ESCAPE:
                	sys.exit()
            if event.type == pygame.QUIT:
                playing=False
                pygame.quit()
                quit()




        
        pygame.display.update()
        clock.tick(60)
#sete()