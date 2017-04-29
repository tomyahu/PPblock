import pygame
from pygame.locals import *
from textura import *

pygame.init()


#Sprites Cajas
caja1Im = pygame.image.load('images/Caja1.png')


#Textura Cajas
caja1 = textura(caja1Im,45,45)


#Sprites Bolas
pokeIm = pygame.image.load('images/Pokebola.png')
pokeIm = pygame.transform.scale(pokeIm,(10,10))


#Textura Bolas
pokebola = textura(pokeIm,10,10)
