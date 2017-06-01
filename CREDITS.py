import time,sys
import pygame
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((1200,720),0,32) #inicia a tela

pygame.display.set_caption('Physics, Morty')

fundo=pygame.image.load('logo_maior.jpg')
ganhou=pygame.image.load('VC_GANHOU.png')
credito=pygame.image.load('credits_img.png')

while True:
	screen.fill([0,0,0])

	screen.blit(fundo,(0,0))

	screen.blit(ganhou,(0,0))

	events=pygame.event.get()
	for event in events:
		if event.type==pygame.KEYDOWN:
			if event.key==K_ESCAPE:
				sys.exit()

	pygame.display.update()
