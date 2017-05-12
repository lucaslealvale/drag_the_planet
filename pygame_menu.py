import pygame,sys, time
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((1200,720),0,32) #inicia a tela

logo1=pygame.image.load('logo_maior.jpg') #tamanho: 960x540

logo_name=pygame.image.load('logo_name_maior.png') #Carrega as imagens

myfont=pygame.font.Font("8-BIT WONDER.ttf", 40) #chamada da fonte

label_1=myfont.render("New Game",1,(205,205,205)) #texto 1

label_2=myfont.render("Load Game",1,(205,205,205))

label_3=myfont.render("Quit Game",1,(205,205,205))

label_1_NEW=myfont.render("New Game",1,(173,255,47))

label_2_NEW=myfont.render("Load Game",1,(173,255,47))

label_3_NEW=myfont.render("Quit Game",1,(173,255,47))

RICK_GUN=pygame.image.load('arma_rick.png')

x=label_1_NEW
y=label_2
z=label_3

x_RICK=[350,305]

while True:
	
	screen.fill([0,0,0]) #a tela fica preta no fundo

	screen.blit(logo1, [0,0]) #a logo1 é	 posicionada nas coordenadas em 0,0

	screen.blit(logo_name, [110,-100]) #a logo_name é posicionada nas coordenadas 50,50

	screen.blit(x, [420,300])

	screen.blit(y, [410,400])

	screen.blit(z, [410,500])

	screen.blit(RICK_GUN, x_RICK)

	events=pygame.event.get()
	for event in events:
		if event.type==pygame.KEYDOWN:
			if event.key==K_ESCAPE:
				sys.exit()
			elif y==label_2_NEW and event.key==K_DOWN:
				x=label_1
				y=label_2
				z=label_3_NEW
				x_RICK=[340,505]
			elif z==label_3_NEW and event.key==K_UP:
				x=label_1
				y=label_2_NEW
				z=label_3
				x_RICK=[340,405]
			elif z==label_3_NEW and event.key==K_DOWN:
				x=label_1_NEW
				y=label_2
				z=label_3
				x_RICK=[350,305]
			elif x==label_1_NEW and event.key==K_UP:
				x=label_1
				y=label_2
				z=label_3_NEW
				x_RICK=[340,505]
			elif y==label_2_NEW and event.key==K_UP:
				x=label_1_NEW
				y=label_2
				z=label_3
				x_RICK=[350,305]
			elif event.key==K_DOWN:
				x=label_1
				y=label_2_NEW
				z=label_3
				x_RICK=[340,405]

	pygame.display.update() 
