import pygame, sys, time
from pygame.locals import *

pygame.init()
#pygame.mixer.init()

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

sound_1=myfont.render("Soundtrack",1,(205,205,205))
sound_2=myfont.render("Soundtrack",1,(173,255,47))
sound_3=myfont.render("Soundtrack",1,(88,88,92))

um_1=myfont.render("1",1,(205,205,205))
um_2=myfont.render("1",1,(173,255,47))
um_3=myfont.render("1",1,(88,88,92))

dois_1=myfont.render("2",1,(205,205,205))
dois_2=myfont.render("2",1,(173,255,47))
dois_3=myfont.render("2",1,(88,88,92))

tres_1=myfont.render("3",1,(205,205,205))
tres_2=myfont.render("3",1,(173,255,47))
tres_3=myfont.render("3",1,(88,88,92))

quatro_1=myfont.render("4",1,(205,205,205))
quatro_2=myfont.render("4",1,(173,255,47))
quatro_3=myfont.render("4",1,(88,88,92))

cinco_1=myfont.render("5",1,(205,205,205))
cinco_2=myfont.render("5",1,(173,255,47))
cinco_3=myfont.render("5",1,(88,88,92))

PLAYGAME_1=myfont.render("PLAY GAME",1,(205,205,205))
PLAYGAME_2=myfont.render("PLAY GAME",1,(173,255,47))

pygame.mixer.music.load('tema.mp3') #Música

soundtrack_1="tema.mp3"
soundtrack_2="musica1.mp3"
soundtrack_3="musica2.mp3"
soundtrack_4="musica4.mp3"
soundtrack_5="musica5.mp3"

x=music_2
y=on_2
w=sound_1
z=um_1
marker=1
play=PLAYGAME_1

while True:
	if (d==6):
		d=0
	screen.fill([0,0,0])
	screen.blit(logo1, [0,0])
	screen.blit(logo_name, [330,50])
	screen.blit(pygame.image.load(img_names[d]), x_RICK)
	screen.blit(x, [400,300])
	screen.blit(y, [750,300])
	screen.blit(w, [300,400])
	screen.blit(z, [800,400])
	screen.blit(play, [420, 500])
	events=pygame.event.get()
	for event in events:
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_ESCAPE:
				import pygame_menu
			elif marker==1 and y==on_2 and z==um_1 and event.key==pygame.K_RETURN:
				y=off_2
				pygame.mixer.music.stop()
				w=sound_3
				z=um_3
			elif marker==1 and y==on_2 and z==dois_1 and event.key==pygame.K_RETURN:
				y=off_2
				pygame.mixer.music.stop()
				w=sound_3
				z=dois_3
			elif marker==1 and y==on_2 and z==tres_1 and event.key==pygame.K_RETURN:
				y=off_2
				pygame.mixer.music.stop()
				w=sound_3
				z=tres_3
			elif marker==1 and y==on_2 and z==quatro_1 and event.key==pygame.K_RETURN:
				y=off_2
				pygame.mixer.music.stop()
				w=sound_3
				z=quatro_3
			elif marker==1 and y==on_2 and z==cinco_1 and event.key==pygame.K_RETURN:
				y=off_2
				pygame.mixer.music.stop()
				w=sound_3
				z=cinco_3
			elif marker==1 and y==off_2 and z==um_3 and event.key==pygame.K_RETURN:
				y=on_2
				pygame.mixer.music.play()
				w=sound_1
				z=um_1
			elif marker==1 and y==off_2 and z==dois_3 and event.key==pygame.K_RETURN:
				y=on_2
				pygame.mixer.music.play()
				w=sound_1
				z=dois_1
			elif marker==1 and y==off_2 and z==tres_3 and event.key==pygame.K_RETURN:
				y=on_2
				pygame.mixer.music.play()
				w=sound_1
				z=tres_1
			elif marker==1 and y==off_2 and z==quatro_3 and event.key==pygame.K_RETURN:
				y=on_2
				pygame.mixer.music.play()
				w=sound_1
				z=quatro_1
			elif marker==1 and y==off_2 and z==cinco_3 and event.key==pygame.K_RETURN:
				y=on_2
				pygame.mixer.music.play()
				w=sound_1
				z=cinco_1
			elif marker==1 and y==on_2 and z==um_1 and event.key==K_DOWN:
				x=music_1
				y=on_1
				w=sound_2
				z=um_2
				pygame.mixer.init()
				pygame.mixer.music.load(soundtrack_1)
				pygame.mixer.music.play(10)
				marker=2
				x_RICK=[220,400]
			elif marker==1 and y==on_2 and z==dois_1 and event.key==K_DOWN:
				x=music_1
				y=on_1
				w=sound_2
				z=dois_2
				marker=2
				x_RICK=[220,400]
			elif marker==1 and y==on_2 and z==tres_1 and event.key==K_DOWN:
				x=music_1
				y=on_1
				w=sound_2
				z=tres_2
				marker=2
				x_RICK=[220,400]
			elif marker==1 and y==on_2 and z==quatro_1 and event.key==K_DOWN:
				x=music_1
				y=on_1
				w=sound_2
				z=quatro_2
				marker=2
				x_RICK=[220,400]
			elif marker==1 and y==on_2 and z==cinco_1 and event.key==K_DOWN:
				x=music_1
				y=on_1
				w=sound_2
				z=cinco_2
				marker=2
				x_RICK=[220,400]
			elif marker==1 and y==off_2 and event.key==K_DOWN:
				x=music_1
				y=off_1
				play=PLAYGAME_2
				x_RICK=[340,510]
				marker=3
			elif marker==2 and y==on_1 and z==um_2 and event.key==K_DOWN:
				z=um_1
				w=sound_1
				play=PLAYGAME_2
				marker=3
				x_RICK=[340,510]
			elif marker==2 and y==on_1 and z==dois_2 and event.key==K_DOWN:
				z=dois_1
				w=sound_1
				play=PLAYGAME_2
				marker=3
				x_RICK=[340,510]
			elif marker==2 and y==on_1 and z==tres_2 and event.key==K_DOWN:
				z=tres_1
				w=sound_1
				play=PLAYGAME_2
				marker=3
				w=sound_1
				x_RICK=[340,510]
			elif marker==2 and y==on_1 and z==quatro_2 and event.key==K_DOWN:
				z=quatro_1
				w=sound_1
				play=PLAYGAME_2
				marker=3
				x_RICK=[340,510]
			elif marker==2 and y==on_1 and z==cinco_2 and event.key==K_DOWN:
				z=cinco_1
				w=sound_1
				play=PLAYGAME_2
				marker=3
				x_RICK=[340,510]
			elif marker==2 and z==um_2 and event.key==pygame.K_RETURN:
				z=dois_2
				pygame.mixer.init()
				pygame.mixer.music.load(soundtrack_2)
				pygame.mixer.music.play(10)
			elif marker==2 and z==dois_2 and event.key==pygame.K_RETURN:
				z=tres_2
				pygame.mixer.init()
				pygame.mixer.music.load(soundtrack_3)
				pygame.mixer.music.play(10)
			elif marker==2 and z==tres_2 and event.key==pygame.K_RETURN:
				z=quatro_2
				pygame.mixer.init()
				pygame.mixer.music.load(soundtrack_4)
				pygame.mixer.music.play(10)
			elif marker==2 and z==quatro_2 and event.key==pygame.K_RETURN:
				z=cinco_2
				pygame.mixer.init()
				pygame.mixer.music.load(soundtrack_5)
				pygame.mixer.music.play(10)
			elif marker==2 and z==cinco_2 and event.key==pygame.K_RETURN:
				z=um_2
				pygame.mixer.init()
				pygame.mixer.music.load(soundtrack_1)
				pygame.mixer.music.play(10)
			elif marker==3 and y==on_1 and z==um_1 and event.key==K_UP:
				marker=2
				z=um_2
				w=sound_2
				play=PLAYGAME_1
				x_RICK=[220,400]
			elif marker==3 and y==on_1 and z==dois_1 and event.key==K_UP:
				marker=2
				z=dois_2
				w=sound_2
				play=PLAYGAME_1
				x_RICK=[220,400]
			elif marker==3 and y==on_1 and z==tres_1 and event.key==K_UP:
				marker=2
				z=tres_2
				w=sound_2
				play=PLAYGAME_1
				x_RICK=[220,400]
			elif marker==3 and y==on_1 and z==quatro_1 and event.key==K_UP:
				marker=2
				z=quatro_2
				w=sound_2
				play=PLAYGAME_1
				x_RICK=[220,400]
			elif marker==3 and y==on_1 and z==cinco_1 and event.key==K_UP:
				marker=2
				z=cinco_2
				w=sound_2
				play=PLAYGAME_1
				x_RICK=[220,400]
			elif marker==3 and y==off_1 and event.key==K_UP:
				marker=1
				y=off_2
				x=music_2
				play=PLAYGAME_1
				x_RICK=[310,310]
			elif marker==3 and event.key==pygame.K_RETURN:
				import main_code
			elif marker==3 and y==on_1 and event.key==K_DOWN:
				marker=1
				y=on_2
				x=music_2
				play=PLAYGAME_1
				x_RICK=[310,310]
			elif marker==3 and y==off_1 and event.key==K_DOWN:
				marker=1
				y=off_2
				x=music_2
				play=PLAYGAME_1
				x_RICK=[310,310]
			elif marker==1 and y==on_2 and event.key==K_UP:
				marker=3
				y=on_1
				play=PLAYGAME_2
				x=music_1
				x_RICK=[340,510]
			elif marker==2 and y==on_1 and z==um_2 and event.key==K_UP:
				y=on_2
				marker=1
				z=um_1
				x=music_2
				w=sound_1
				x_RICK=[310,310]
			elif marker==2 and y==on_1 and z==dois_2 and event.key==K_UP:
				y=on_2
				marker=1
				z=dois_1
				x=music_2
				w=sound_1
				x_RICK=[310,310]
			elif marker==2 and y==on_1 and z==tres_2 and event.key==K_UP:
				y=on_2
				marker=1
				z=tres_1
				x=music_2
				w=sound_1
				x_RICK=[310,310]
			elif marker==2 and y==on_1 and z==quatro_2 and event.key==K_UP:
				y=on_2
				marker=1
				z=quatro_1
				x=music_2
				w=sound_1
				x_RICK=[310,310]
			elif marker==2 and y==on_1 and z==cinco_2 and event.key==K_UP:
				y=on_2
				marker=1
				z=cinco_1
				x=music_2
				w=sound_1
				x_RICK=[310,310]

		elif event.type==pygame.QUIT:
			mainloop=False
			sys.exit()

	d=d+1
	pygame.display.update()
