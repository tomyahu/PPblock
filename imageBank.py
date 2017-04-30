import pygame
from pygame.locals import *
from textura import *

pygame.init()


#Sprites
#Cajas
caja1Im = pygame.image.load('images/Caja1.png')

#Bolas
pokeIm = pygame.image.load('images/Pokebola.png')
pokeIm = pygame.transform.scale(pokeIm,(10,10))

pongIm = pygame.image.load('images/Pong.png')
pongIm = pygame.transform.scale(pongIm,(15,15))

#Flecha
flechaIm = pygame.image.load('images/Flecha3.png')
flechaIm = pygame.transform.scale(flechaIm,(120,120))


#Textura
#Cajas
caja1 = Textura(caja1Im,45,45)

#Bolas
pokebola = Textura(pokeIm,10,10)
pong = Textura(pongIm,15,15)

#Flecha
flecha = Textura(flechaIm,120,120)
