import pygame,sys,time
from pygame.locals import *

def animation():
	import main_code as game

	pygame.init()

	screen=pygame.display.set_mode((1200,720),0,32)

	pygame.display.set_caption('Physics, Morty')

	planeta=['sprite_terra00.png','sprite_terra01.png','sprite_terra02.png','sprite_terra03.png','sprite_terra04.png','sprite_terra05.png','sprite_terra06.png','sprite_terra07.png','sprite_terra08.png','sprite_terra09.png','sprite_terra10.png','sprite_terra11.png','sprite_terra12.png','sprite_terra13.png','sprite_terra14.png','sprite_terra15.png']

	d=0

	playing=True

	while playing:
		print(d)
		if d>15:
			game.jogo()
		screen.fill([0,0,0])
		screen.blit(pygame.image.load(planeta[d]),[0,0])

		events=pygame.event.get()
		for event in events:
			if event.type==pygame.KEYDOWN:
				if event.key==K_ESCAPE:
					sys.exit()
			if event.type==pygame.QUIT:
				sys.exit()

		d=d+1
		pygame.display.update()