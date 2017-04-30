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
from Player import player

# Se inician modulos
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Se inicia la pantalla
surface = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('PP-Block')

# Se crea el reloj
clock = pygame.time.Clock()

# Mouse
mouse = pygame.mouse

########PRUEBA
player1 = player(surface,pong,flecha)
player2 = player(surface,pong,flecha)
player3 = player(surface,pong,flecha)
player4 = player(surface,pong,flecha)

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

    player1.draw(mouse)
    # Vuelca lo dibujado en pantalla
    pygame.display.flip()