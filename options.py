import pygame, sys, time
from pygame.locals import *

pygame.init()

img_names = ["arma_sprite0.png","arma_sprite1.png","arma_sprite2.png","arma_sprite3.png","arma_sprite4.png","arma_sprite5.png","arma_sprite6.png"] #sprite da arma

screen=pygame.display.set_mode((1200,720),0,32)

logo1=pygame.image.load('logo_maior.jpg')

myfont=pygame.font.Font("8-BIT WONDER.ttf", 40)

logo_name=pygame.image.load("options_logo.png")

d=0
x_RICK=[310,310]

music_1=myfont.render("Music",1,(205,205,205))
on_1=myfont.render("On",1,(205,205,205))
off_1=myfont.render("Off",1,(205,205,205))

music_2=myfont.render("Music",1,(173,255,47))
on_2=myfont.render("On",1,(173,255,47))
off_2=myfont.render("Off",1,(173,255,47))

x=music_2
y=on_2

#brightness_1=myfont.render("Brightness",1(205,205,205))
um_1=myfont.render("1",1,(205,205,205))
dois_1=myfont.render("2",1,(205,205,205))
tres_1=myfont.render("3",1,(205,205,205))
quatro_1=myfont.render("4",1,(205,205,205))
cinco_1=myfont.render("5",1,(205,205,205))

brightness_2=myfont.render("Brightness",1,(173,255,47))
um_2=myfont.render("1",1,(173,255,47))
dois_2=myfont.render("2",1,(173,255,47))
tres_2=myfont.render("3",1,(173,255,47))
quatro_2=myfont.render("4",1,(173,255,47))
cinco_2=myfont.render("5",1,(173,255,47))

marker=1

while True:
	if (d==6):
		d=0
	screen.fill([0,0,0])
	screen.blit(logo1, [0,0])
	screen.blit(logo_name, [330,50])
	screen.blit(pygame.image.load(img_names[d]), x_RICK)
	screen.blit(x, [400,300])
	screen.blit(y, [750,300])
	events=pygame.event.get()
	for event in events:
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_ESCAPE:
				import pygame_menu
			elif y==on_2 and event.key==pygame.K_RETURN:
				y=off_2
			elif y==off_2 and event.key==pygame.K_RETURN:
				y=on_2

	d=d+1
	pygame.display.update()
