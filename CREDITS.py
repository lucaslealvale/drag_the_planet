import time,sys
import pygame
from pygame.locals import *
import pygame_menu1 as b

	
def creditos():
	pygame.init()

	screen=pygame.display.set_mode((1200,720),0,32) #inicia a tela

	pygame.display.set_caption('Physics, Morty')

	#fundo=pygame.image.load('logo_maior.jpg')
	ganhou=pygame.image.load('VC_GANHOU.png')
	credito=pygame.image.load('credits_img.png')
	nave=['navevoand00.png','navevoand01.png','navevoand02.png','navevoand03.png','navevoand04.png','navevoand05.png','navevoand06.png','navevoand07.png','navevoand08.png','navevoand09.png','navevoand10.png','navevoand11.png','navevoand12.png','navevoand13.png','navevoand14.png','navevoand15.png','navevoand16.png','navevoand17.png','navevoand18.png','navevoand19.png','navevoand20.png','navevoand21.png','navevoand22.png','navevoand23.png','navevoand24.png','navevoand25.png','navevoand26.png','navevoand27.png']

	plotar=ganhou

	d=0

	while True:
		if d>=28 and plotar==ganhou:
			plotar=credito
			d=0
		elif d>=28 and plotar==credito:
			b.menu1()
		screen.fill([0,0,0])

		screen.blit(pygame.image.load(nave[d]),(0,0))


		#screen.blit(fundo,(0,0))

		screen.blit(plotar,(0,0))

		events=pygame.event.get()
		for event in events:
			if event.type==pygame.KEYDOWN:
				if event.key==K_ESCAPE:
					sys.exit()
		d=d+1

		pygame.display.update()
