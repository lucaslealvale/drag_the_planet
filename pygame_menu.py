import pygame,sys, time
from pygame.locals import *
import levels as lvl
import options as opt

def menu():
	pygame.init()
	pygame.mixer.init()

	screen=pygame.display.set_mode((1200,720),0,32) #inicia a tela

	pygame.display.set_caption('Physics, Morty')

	img_names = ["arma_sprite0.png","arma_sprite1.png","arma_sprite2.png","arma_sprite3.png","arma_sprite4.png","arma_sprite5.png","arma_sprite6.png"] #sprite da arma

	logo1=pygame.image.load('logo_maior.jpg') #tamanho: 960x540

	logo_name=pygame.image.load('logo_name_maior.png') #Carrega as imagens

	myfont=pygame.font.Font("8-BIT WONDER.ttf", 40) #chamada da fonte

	label_1=myfont.render("New Game",1,(205,205,205)) #texto 1

	label_2=myfont.render("Options",1,(205,205,205))

	label_3=myfont.render("Quit Game",1,(205,205,205))

	label_1_NEW=myfont.render("New Game",1,(173,255,47))

	label_2_NEW=myfont.render("Options",1,(173,255,47))

	label_3_NEW=myfont.render("Quit Game",1,(173,255,47))

	enter=pygame.image.load('enter_img.png')

	enter=pygame.transform.scale(enter,(204,128)) #re-escalona a imagem do botão


	xp=label_1_NEW
	yp=label_2
	zp=label_3

	markerp=1 #marca a opção que estiver selecionada no menu

	d=0
	x_RICK=[350,305]

	soundtrack_1="tema.mp3"
	soundtrack_2="musica1.mp3"
	soundtrack_3="musica2.mp3"
	soundtrack_4="musica4.mp3"
	soundtrack_5="musica5.mp3"

	pygame.mixer.music.load(soundtrack_1) #Música
	pygame.mixer.music.play(-1)


	while True:
	
		if (d==6):
			d=0

		screen.fill([0,0,0]) #a tela fica preta no fundo

		screen.blit(logo1, [0,0]) #a logo1 é	 posicionada nas coordenadas em 0,0

		screen.blit(logo_name, [110,-100]) #a logo_name é posicionada nas coordenadas 50,50

		screen.blit(xp, [420,300])

		screen.blit(yp, [410,400])

		screen.blit(zp, [410,500])

		screen.blit(enter,[1000,600])
	
		screen.blit(pygame.image.load(img_names[d]), x_RICK)

		events=pygame.event.get()
		for event in events:
			if event.type==pygame.KEYDOWN:
				if event.key==K_ESCAPE:
					pygame.mixer.music.fadeout(2)
					sys.exit()
				elif xp==label_1_NEW and event.key==K_DOWN:
					xp=label_1
					yp=label_2_NEW
					zp=label_3
					markerp=2
					x_RICK=[340,405]
				elif xp==label_1_NEW and event.key==K_UP:
					xp=label_1
					yp=label_2
					zp=label_3_NEW
					markerp=3
					x_RICK=[340,505]
				elif yp==label_2_NEW and event.key==K_DOWN:
					xp=label_1
					yp=label_2
					zp=label_3_NEW
					markerp=3
					x_RICK=[340,505]
				elif yp==label_2_NEW and event.key==K_UP:
					xp=label_1_NEW
					yp=label_2
					zp=label_3
					markerp=1
					x_RICK=[350,305]
				elif zp==label_3_NEW and event.key==K_DOWN:
					xp=label_1_NEW
					yp=label_2
					zp=label_3
					markerp=1
					x_RICK=[350,305]
				elif zp==label_3_NEW and event.key==K_UP:
					xp=label_1
					yp=label_2_NEW
					zp=label_3
					markerp=2
					x_RICK=[340,405]
				elif markerp==1 and event.key==pygame.K_RETURN:
					lvl.fases()
				elif markerp==2 and event.key==pygame.K_RETURN:
					opt.opcoes()
				elif markerp==3 and event.key==pygame.K_RETURN:
					pygame.mixer.music.fadeout(2)
					sys.exit()
		d=d+1
		pygame.display.update()
menu()