import pygame,os,time,sys
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((1200,720),0,32)
pygame.display.set_caption('Physics, Morty')
logo1=pygame.image.load('logo_maior.jpg')
levels_name=pygame.image.load('levels.png')
cima_1=pygame.image.load('flechinha_cima_1.png')
baixo_1=pygame.image.load('flechinha_baixo_1.png')
cima_2=pygame.image.load('flechinha_cima_2.png')
baixo_2=pygame.image.load('flechinha_baixo_2.png')
myfont=pygame.font.Font("8-BIT WONDER.ttf", 72)
level=myfont.render("level",1,(205,205,205))

tutorial=myfont.render('tutorial',1,(205,205,205))
um=myfont.render('1',1,(205,205,205))
dois=myfont.render('2',1,(205,205,205))
tres=myfont.render('3',1,(205,205,205))
quatro=myfont.render('4',1,(205,205,205))
cinco=myfont.render('5',1,(205,205,205))
seis=myfont.render('6',1,(205,205,205))
sete=myfont.render('7',1,(205,205,205))
oito=myfont.render('8',1,(205,205,205))
nove=myfont.render('9',1,(205,205,205))
dez=myfont.render('10',1,(205,205,205))

xx=tutorial #marcador de número

xy_cima=[750,340] 
xy_baixo=[750,490]

xx_xy=[550,400]

while True:
	screen.fill([0,0,0])
	screen.blit(logo1,[0,0])
	screen.blit(levels_name,[270,100])
	screen.blit(cima_1,xy_cima)
	screen.blit(baixo_1,xy_baixo)
	screen.blit(level,[100,400])
	screen.blit(xx,xx_xy)


	events=pygame.event.get()
	for event in events:
		if event.type==pygame.KEYDOWN:
			if event.key==K_ESCAPE:
				pygame.mixer.music.fadeout(2)
				sys.exit()
			elif xx==tutorial and event.key==K_UP:
				xx=um
				xx_xy=[760,400]
				screen.blit(cima_2,xy_cima)
			elif xx==um and event.key==K_UP:
				xx=dois
				screen.blit(cima_2,xy_cima)
			elif xx==dois and event.key==K_UP:
				xx=tres
				screen.blit(cima_2,xy_cima)
			elif xx==tres and event.key==K_UP:
				xx=quatro
				screen.blit(cima_2,xy_cima)
			elif xx==quatro and event.key==K_UP:
				xx=cinco
				screen.blit(cima_2,xy_cima)
			elif xx==cinco and event.key==K_UP:
				xx=seis
				screen.blit(cima_2,xy_cima)
			elif xx==seis and event.key==K_UP:
				xx=sete 
				screen.blit(cima_2,xy_cima)
			elif xx==sete and event.key==K_UP:
				xx=oito
				screen.blit(cima_2,xy_cima)
			elif xx==oito and event.key==K_UP:
				xx=nove
				screen.blit(cima_2,xy_cima)
			elif xx==nove and event.key==K_UP:
				xx=dez
				screen.blit(cima_2,xy_cima)
			elif xx==dez and event.key==K_UP:
				xx=tutorial
				xx_xy=[550,400]
				screen.blit(cima_2,xy_cima)
			elif xx==tutorial and event.key==K_DOWN:
				xx=dez
				xx_xy=[760,400]
				screen.blit(baixo_2,xy_baixo)
			elif xx==dez and event.key==K_DOWN:
				xx=nove
				screen.blit(baixo_2,xy_baixo)
			elif xx==nove and event.key==K_DOWN:
				xx=oito
				screen.blit(baixo_2,xy_baixo)
			elif xx==oito and event.key==K_DOWN:
				xx=sete 
				screen.blit(baixo_2,xy_baixo)
			elif xx==sete and event.key==K_DOWN:
				xx=seis
				screen.blit(baixo_2,xy_baixo)
			elif xx==seis and event.key==K_DOWN:
				xx=cinco
				screen.blit(baixo_2,xy_baixo)
			elif xx==cinco and event.key==K_DOWN:
				xx=quatro 
				screen.blit(baixo_2,xy_baixo)
			elif xx==quatro and event.key==K_DOWN:
				xx=tres
				screen.blit(baixo_2,xy_baixo)
			elif xx==tres and event.key==K_DOWN:
				xx=dois
				screen.blit(baixo_2,xy_baixo)
			elif xx==dois and event.key==K_DOWN:
				xx=um
				screen.blit(baixo_2,xy_baixo)
			elif xx==um and event.key==K_DOWN:
				xx=tutorial
				xx_xy=[550,400]
				screen.blit(baixo_2,xy_baixo)
			#elif event.key==K_UP:
			#	screen.blit(cima_2,xy_cima)
			#elif event.key==K_DOWN:
			#	screen.blit(baixo_2,xy_baixo)
	pygame.display.update()
