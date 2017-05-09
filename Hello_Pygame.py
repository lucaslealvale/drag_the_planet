import pygame, sys
from pygame.locals import *

#Pygame
pygame.init()

#Janela
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello world!')

#Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Fonte
basicFont = pygame.font.SysFont(None, 48)

#Texto
text = basicFont.render('Hello world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

#Background branco
windowSurface.fill(WHITE)

#Polígono
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

#Linhas azuis
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

#Circulo azul
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# Elípse vermelha
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# Retângulos
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

#Pixel array 
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# Desenhar na superfície
windowSurface.blit(text, textRect)

# Desenhar tela
pygame.display.update()

# Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()