import pygame, sys

pygame.init()
tela = pygame.display.set_mode((1200,720))
pygame.display.set_caption('Physics, Morty')
clock = pygame.time.Clock()
class caixa:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy
        

fundo = pygame.image.load("fundo.jpg").convert()
caixa_i = pygame.image.load("caixa.png").convert_alpha()
caixa_i=pygame.transform.scale(caixa_i, (100,105))
caixa=caixa(50,620)
playing = True

while playing:
    tela.blit(fundo,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing=False
        print(event)
    caixa.move(1,-1)
    tela.blit(caixa_i,(caixa.x,caixa.y))
    pygame.display.update()
    clock.tick(60)
