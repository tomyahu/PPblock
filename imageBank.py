import pygame
from pygame.locals import *
from textura import *

pygame.init()



#Sprites Bolas
pokeIm = pygame.image.load('images/Pokebola.png')
pokeIm = pygame.transform.scale(pokeIm,(10,10))


#textura bolas
pokebola = textura(pokeIm,10,10)
