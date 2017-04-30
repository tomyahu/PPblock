import os
import pygame
from pygame.locals import *
from consts import *
from math import *
from matCas import MatCas

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

Mat = MatCas(surface)

a = 0

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
    keys = pygame.key.get_pressed()
    if keys[K_DOWN] and a == 0:
        Mat.nextLevel()
        a = 1
    else:
        a = 0

    print a

    Mat.draw()


    # Vuelca lo dibujado en pantalla
    pygame.display.flip()