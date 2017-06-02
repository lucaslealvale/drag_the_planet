import pygame
from pygame.locals import *
import time,sys
import levels as lvl


	
def HISTORIONA():
	pygame.init()

	screen=pygame.display.set_mode((1200,720),0,32) #inicia a tela

	pygame.display.set_caption('Physics, Morty')

	img0=pygame.image.load('historinha00.jpg')
	img1=pygame.image.load('historinha01.jpg')
	img2=pygame.image.load('historinha02.jpg')
	img3=pygame.image.load('historinha03.jpg')
	img4=pygame.image.load('historinha04.jpg')
	img5=pygame.image.load('historinha05.jpg')
	img6=pygame.image.load('historinha06.jpg')
	img7=pygame.image.load('historinha07.jpg')
	img8=pygame.image.load('historinha08.jpg')
	enter=pygame.image.load('enter_img.png')
	enter=pygame.transform.scale(enter,(204,128))

	d=img0

	while True:
		#if d>9:


		screen.fill([0,0,0])

		screen.blit(d,[0,0])

		screen.blit(enter,(1000,25))

		events=pygame.event.get()
		for event in events:
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RETURN and d==img0:
					d=img1
				elif event.key==pygame.K_RETURN and d==img1:
					d=img2
				elif event.key==pygame.K_RETURN and d==img2:
					d=img3
				elif event.key==pygame.K_RETURN and d==img3:
					d=img4
				elif event.key==pygame.K_RETURN and d==img4:
					d=img5
				elif event.key==pygame.K_RETURN and d==img5:
					d=img6
				elif event.key==pygame.K_RETURN and d==img6:
					d=img7
				elif event.key==pygame.K_RETURN and d==img7:
					d=img8
				elif event.key==pygame.K_RETURN and d==img8:
					lvl.fases()
				elif event.type==K_ESCAPE:
					sys.exit()

		pygame.display.update()

