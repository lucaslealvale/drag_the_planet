import pygame,os,time,sys
from pygame.locals import *
import main_code as fase_tutorial
import main_code1 as fase_1
import main_code2 as fase_2
import main_code3 as fase_3
import main_code4 as fase_4
import main_code5 as fase_5
import main_code6 as fase_6
import main_code7 as fase_7
import main_code8 as fase_8
import main_code9 as fase_9
import main_code10 as fase_10

def fases():
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
	tut=pygame.image.load('tut_img.jpg')
	enter=pygame.image.load('enter_img.png')
	enter=pygame.transform.scale(enter,(204,128))

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

	f=0

	#class unit():
    #def __init__(self):
    #    self.last = pygame.time.get_ticks()
    #    self.cooldown = 300    
#
    #def fire(self):
    #    # fire gun, only if cooldown has been 0.3 seconds since last
    #    now = pygame.time.get_ticks()
    #    if now - self.last >= self.cooldown:
    #        self.last = now
    #        spawn_bullet()

	xx=tutorial #marcador de número

	xy_cima=[750,340] 
	xy_baixo=[750,490]

	xx_xy=[550,400]

	fundao=0

	while True:
		if (fundao==0):
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
				elif f==0 and fundao==0 and xx==tutorial and event.key==pygame.K_RETURN:
					f=1
					fundao=1
					screen.blit(tut,[0,0])
					screen.blit(enter,[1000,600])
				elif f==1 and fundao==1 and event.key==pygame.K_RETURN and xx==tutorial:
					f=0
					fase_tutorial.tutorial()
					fundao=0
				elif f==0 and fundao==0 and xx==um and event.key==pygame.K_RETURN:
					f=1
					fundao=1
					screen.blit(tut,[0,0])
					screen.blit(enter,[1000,600])
				elif f==1 and fundao==1 and xx==um and event.key==pygame.K_RETURN:
					fase_1.um()
				elif f==0 and fundao==0 and xx==dois and event.key==pygame.K_RETURN:
					f=1
					fundao=1
					screen.blit(tut,[0,0])
					screen.blit(enter,[1000,600])
				elif f==1 and fundao==1 and xx==dois and event.key==pygame.K_RETURN:
					fase_2.dois()
				elif f==0 and fundao==0 and xx==tres and event.key==pygame.K_RETURN:
					f=1
					fundao=1
					screen.blit(tut,[0,0])
					screen.blit(enter,[1000,600])
				elif f==1 and fundao==1 and xx==tres and event.key==pygame.K_RETURN:
					fase_3.tres()
				elif f==0 and fundao==0 and xx==quatro and event.key==pygame.K_RETURN:
					f=1
					fundao=1
					screen.blit(tut,[0,0])
					screen.blit(enter,[1000,600])
				elif f==1 and fundao==1 and xx==quatro and event.key==pygame.K_RETURN:
					fase_4.quatro()
				elif f==0 and fundao==0 and xx==cinco and event.key==pygame.K_RETURN:
					f=1
					fundao=1
					screen.blit(tut,[0,0])
					screen.blit(enter,[1000,600])
				elif f==1 and fundao==1 and xx==cinco and event.key==pygame.K_RETURN:
					fase_5.cinco()
				elif f==0 and fundao==0 and xx==seis and event.key==pygame.K_RETURN:
					f=1
					fundao=1
					screen.blit(tut,[0,0])
					screen.blit(enter,[1000,600])
				elif f==1 and fundao==1 and xx==seis and event.key==pygame.K_RETURN:
					fase_6.seis()
				elif f==0 and fundao==0 and xx==sete and event.key==pygame.K_RETURN:
					f=1
					fundao=1
					screen.blit(tut,[0,0])
					screen.blit(enter,[1000,600])
				elif f==1 and fundao==1 and xx==sete and event.key==pygame.K_RETURN:
					fase_7.sete()
				elif f==0 and fundao==0 and xx==oito and event.key==pygame.K_RETURN:
					f=1
					fundao=1
					screen.blit(tut,[0,0])
					screen.blit(enter,[1000,600])
				elif f==1 and fundao==1 and xx==oito and event.key==pygame.K_RETURN:
					fase_8.oito()
				elif f==0 and fundao==0 and xx==nove and event.key==pygame.K_RETURN:
					f=1
					fundao=1
					screen.blit(tut,[0,0])
					screen.blit(enter,[1000,600])
				elif f==1 and fundao==1 and xx==nove and event.key==pygame.K_RETURN:
					fase_9.nove()
				elif f==0 and fundao==0 and xx==dez and event.key==pygame.K_RETURN:
					f=1
					fundao=1
					screen.blit(tut,[0,0])
					screen.blit(enter,[1000,600])
				elif f==1 and fundao==1 and xx==dez and event.key==pygame.K_RETURN:
					fase_10.dez()
		pygame.display.update()
