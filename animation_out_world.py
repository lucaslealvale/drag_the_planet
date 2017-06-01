import pygame,sys,time
from pygame.locals import *
import main_code as game_tutorial
import main_code1 as game_1
import main_code2 as game_2
import main_code3 as game_3
import main_code4 as game_4
import main_code5 as game_5
import main_code6 as game_6
import main_code7 as game_7
import main_code8 as game_8


def animation():

	pygame.init()

	screen=pygame.display.set_mode((1200,720),0,32)

	pygame.display.set_caption('Physics, Morty')

	planeta=['sprite_terra00.png','sprite_terra01.png','sprite_terra02.png','sprite_terra03.png','sprite_terra04.png','sprite_terra05.png','sprite_terra06.png','sprite_terra07.png','sprite_terra08.png','sprite_terra09.png','sprite_terra10.png','sprite_terra11.png','sprite_terra12.png','sprite_terra13.png','sprite_terra14.png','sprite_terra15.png']

	d=0

	playing=True

	while playing:
		if d>15:
			game_tutorial.tutorial()
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

def animation1():

	pygame.init()

	screen=pygame.display.set_mode((1200,720),0,32)

	pygame.display.set_caption('Physics, Morty')

	planeta=['sprite_terra00.png','sprite_terra01.png','sprite_terra02.png','sprite_terra03.png','sprite_terra04.png','sprite_terra05.png','sprite_terra06.png','sprite_terra07.png','sprite_terra08.png','sprite_terra09.png','sprite_terra10.png','sprite_terra11.png','sprite_terra12.png','sprite_terra13.png','sprite_terra14.png','sprite_terra15.png']

	d=0

	playing=True

	while playing:
		if d>15:
			game_1.um()
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

def animation2():

	pygame.init()

	screen=pygame.display.set_mode((1200,720),0,32)

	pygame.display.set_caption('Physics, Morty')

	planeta=['sprite_terra00.png','sprite_terra01.png','sprite_terra02.png','sprite_terra03.png','sprite_terra04.png','sprite_terra05.png','sprite_terra06.png','sprite_terra07.png','sprite_terra08.png','sprite_terra09.png','sprite_terra10.png','sprite_terra11.png','sprite_terra12.png','sprite_terra13.png','sprite_terra14.png','sprite_terra15.png']

	d=0

	playing=True

	while playing:
		if d>15:
			game_2.dois()
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

def animation3():

	pygame.init()

	screen=pygame.display.set_mode((1200,720),0,32)

	pygame.display.set_caption('Physics, Morty')

	planeta=['sprite_terra00.png','sprite_terra01.png','sprite_terra02.png','sprite_terra03.png','sprite_terra04.png','sprite_terra05.png','sprite_terra06.png','sprite_terra07.png','sprite_terra08.png','sprite_terra09.png','sprite_terra10.png','sprite_terra11.png','sprite_terra12.png','sprite_terra13.png','sprite_terra14.png','sprite_terra15.png']

	d=0

	playing=True

	while playing:
		if d>15:
			game_3.tres()
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

def animation4():

	pygame.init()

	screen=pygame.display.set_mode((1200,720),0,32)

	pygame.display.set_caption('Physics, Morty')

	planeta=['sprite_terra00.png','sprite_terra01.png','sprite_terra02.png','sprite_terra03.png','sprite_terra04.png','sprite_terra05.png','sprite_terra06.png','sprite_terra07.png','sprite_terra08.png','sprite_terra09.png','sprite_terra10.png','sprite_terra11.png','sprite_terra12.png','sprite_terra13.png','sprite_terra14.png','sprite_terra15.png']

	d=0

	playing=True

	while playing:
		if d>15:
			game_4.quatro()
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

def animation5():

	pygame.init()

	screen=pygame.display.set_mode((1200,720),0,32)

	pygame.display.set_caption('Physics, Morty')

	planeta=['sprite_terra00.png','sprite_terra01.png','sprite_terra02.png','sprite_terra03.png','sprite_terra04.png','sprite_terra05.png','sprite_terra06.png','sprite_terra07.png','sprite_terra08.png','sprite_terra09.png','sprite_terra10.png','sprite_terra11.png','sprite_terra12.png','sprite_terra13.png','sprite_terra14.png','sprite_terra15.png']

	d=0

	playing=True

	while playing:
		if d>15:
			game_5.cinco()
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

def animation6():

	pygame.init()

	screen=pygame.display.set_mode((1200,720),0,32)

	pygame.display.set_caption('Physics, Morty')

	planeta=['sprite_terra00.png','sprite_terra01.png','sprite_terra02.png','sprite_terra03.png','sprite_terra04.png','sprite_terra05.png','sprite_terra06.png','sprite_terra07.png','sprite_terra08.png','sprite_terra09.png','sprite_terra10.png','sprite_terra11.png','sprite_terra12.png','sprite_terra13.png','sprite_terra14.png','sprite_terra15.png']

	d=0

	playing=True

	while playing:
		if d>15:
			game_6.seis()
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

def animation7():

	pygame.init()

	screen=pygame.display.set_mode((1200,720),0,32)

	pygame.display.set_caption('Physics, Morty')

	planeta=['sprite_terra00.png','sprite_terra01.png','sprite_terra02.png','sprite_terra03.png','sprite_terra04.png','sprite_terra05.png','sprite_terra06.png','sprite_terra07.png','sprite_terra08.png','sprite_terra09.png','sprite_terra10.png','sprite_terra11.png','sprite_terra12.png','sprite_terra13.png','sprite_terra14.png','sprite_terra15.png']

	d=0

	playing=True

	while playing:
		if d>15:
			game_7.sete()
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

def animation8():

	pygame.init()

	screen=pygame.display.set_mode((1200,720),0,32)

	pygame.display.set_caption('Physics, Morty')

	planeta=['sprite_terra00.png','sprite_terra01.png','sprite_terra02.png','sprite_terra03.png','sprite_terra04.png','sprite_terra05.png','sprite_terra06.png','sprite_terra07.png','sprite_terra08.png','sprite_terra09.png','sprite_terra10.png','sprite_terra11.png','sprite_terra12.png','sprite_terra13.png','sprite_terra14.png','sprite_terra15.png']

	d=0

	playing=True

	while playing:
		if d>15:
			game_8.oito()
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

def animation9():

	pygame.init()

	screen=pygame.display.set_mode((1200,720),0,32)

	pygame.display.set_caption('Physics, Morty')

	planeta=['sprite_terra00.png','sprite_terra01.png','sprite_terra02.png','sprite_terra03.png','sprite_terra04.png','sprite_terra05.png','sprite_terra06.png','sprite_terra07.png','sprite_terra08.png','sprite_terra09.png','sprite_terra10.png','sprite_terra11.png','sprite_terra12.png','sprite_terra13.png','sprite_terra14.png','sprite_terra15.png']

	d=0

	playing=True

	while playing:
		if d>15:
			game_8.oito()
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

def animation10():

	pygame.init()

	screen=pygame.display.set_mode((1200,720),0,32)

	pygame.display.set_caption('Physics, Morty')

	planeta=['sprite_terra00.png','sprite_terra01.png','sprite_terra02.png','sprite_terra03.png','sprite_terra04.png','sprite_terra05.png','sprite_terra06.png','sprite_terra07.png','sprite_terra08.png','sprite_terra09.png','sprite_terra10.png','sprite_terra11.png','sprite_terra12.png','sprite_terra13.png','sprite_terra14.png','sprite_terra15.png']

	d=0

	playing=True

	while playing:
		if d>15:
			game_8.oito()
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

