import os
import pygame
from pygame.locals import *
from consts import *
from math import *

#Importar Imagenes y sonidos
from imageBank import *
from soundBank import *

#Importar Objetos
from Bolita import Bola
from Casilla import Casilla


# Se inician modulos
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Se inicia la pantalla
surface = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('PP-Block')

# Se crea el reloj
clock = pygame.time.Clock()

########PRUEBA
ba = Bola(300,200,pong,surface)
ba.setVel(sqrt(10.0),sqrt(10.0))

ca = Casilla(200,200,caja1,100,surface)

# Entra en bucle principal
while True:

    # Setea el reloj
    clock.tick(FPS)

    # Busca eventos de aplicacion
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    # Dibuja la pantalla
    surface.fill(COLOR_Black)

    # Dibuja los Margenes
    pygame.draw.line(surface, COLOR_White, [0, marUp],[winWidth, marUp], 2)
    pygame.draw.line(surface, COLOR_White, [0, marDown], [winWidth, marDown], 2)

    ###########PRUEBA
    a = 0
    ba.updatePos()

    if ba.isInArea(ca.getXin()-a,ca.getXfin()+a,ca.getYin()-a, ca.getYfin()+a):
        ca.colisionBolita(ba)



    ba.draw()
    ca.draw()
    ca.drawCounter()

    # Vuelca lo dibujado en pantalla
    pygame.display.flip()