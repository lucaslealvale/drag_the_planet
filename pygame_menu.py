import pygame,sys
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((1280,720),0,32) #inicia a tela

logo1=pygame.image.load('logo_maior.jpg')
logo_name=pygame.image.load('logo_1_physics.png') #Carrega as imagens
done=False
while True:
	screen.fill([0,0,0]) #a tela fica preta no fundo

	screen.blit(logo1, [0,0]) #a logo1 é posicionada nas coordenadas em 0,0

	screen.blit(logo_name, [0,0]) #a logo_name é posicionada nas coordenadas 50,50

	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE: done=True
		elif event.type==QUIT:
			done=True

	pygame.display.update() 

