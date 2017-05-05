import pygame
from pygame.locals import *
from textura import *

pygame.init()


#Sprites
#Cajas
caja1Im = pygame.image.load('images/Caja1.png')

bolaExtraIm = pygame.image.load('images/BolaExtra.png')
bolaExtraIm = pygame.transform.scale(bolaExtraIm,(25,25))

randomThIm = pygame.image.load('images/RandomThrow.png')
randomThIm = pygame.transform.scale(randomThIm,(25,25))

blowFilaIm = pygame.image.load('images/BlowFila.png')
blowFilaIm = pygame.transform.scale(blowFilaIm,(25,25))

blowColIm = pygame.image.load('images/BlowColumna.png')
blowColIm = pygame.transform.scale(blowColIm,(25,25))



#Bolas
pokeIm = pygame.image.load('images/Pokebola.png')
pokeIm = pygame.transform.scale(pokeIm,(10,10))

pongIm = pygame.image.load('images/Pong.png')
pongIm = pygame.transform.scale(pongIm,(15,15))

#Botones
playIm = pygame.image.load('images/Play.png')
playIm = pygame.transform.scale(playIm,(57*4,80))
playIm2 = pygame.image.load('images/Play2.png')
playIm2 = pygame.transform.scale(playIm2,(57*4,80))

restartIm = pygame.image.load('images/Restart.png')
restartIm = pygame.transform.scale(restartIm,(57*4,80))
restartIm2 = pygame.image.load('images/Restart2.png')
restartIm2 = pygame.transform.scale(restartIm2,(57*4,80))

pausaIm = pygame.image.load('images/botonPausa.png')
pausaIm = pygame.transform.scale(pausaIm,(50,50))
pausaIm2 = pygame.image.load('images/botonPausa2.png')
pausaIm2 = pygame.transform.scale(pausaIm2,(50,50))

quitIm = pygame.image.load('images/Quit1.png')
quitIm = pygame.transform.scale(quitIm,(57*4,80))
quitIm2 = pygame.image.load('images/Quit2.png')
quitIm2 = pygame.transform.scale(quitIm2,(57*4,80))

#Flecha
flechaIm = pygame.image.load('images/Flecha3.png')
flechaIm = pygame.transform.scale(flechaIm,(120,120))

#Fondo
gameOverScreen = pygame.image.load('images/gameOver.png')

#Textura
#Cajas
caja1 = Textura(caja1Im,45,45)
bolaExtra = Textura(bolaExtraIm,25,25)
randomThrow = Textura(randomThIm,25,25)
blFila = Textura(blowFilaIm,25,25)
blCol = Textura(blowColIm,25,25)

#Bolas
pokebola = Textura(pokeIm,10,10)
pong = Textura(pongIm,15,15)

todasLasBolas = [pong,pokebola]

#Flecha
flecha = Textura(flechaIm,120,120)

#Botones
playTex = [Textura(playIm,57*4,80),Textura(playIm2,57*4,80)]
restartTex = [Textura(restartIm,57*4,80),Textura(restartIm2,57*4,80)]
pausaTex = [Textura(pausaIm,50,50),Textura(pausaIm2,50,50)]
quitTex = [Textura(quitIm,57*4,80),Textura(quitIm2,57*4,80)]
