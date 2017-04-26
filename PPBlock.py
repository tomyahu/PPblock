import os
import pygame
from pygame.locals import *
from consts import *

# Se inician modulos
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Se inicia la pantalla
surface = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('PP-Block')

# Se crea el reloj
clock = pygame.time.Clock()

# Entra en bucle principal
while True:

    # Setea el reloj
    clock.tick(FPS)

    # Busca eventos de aplicacion
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    # Dibuja los Margenes
    pygame.draw.line(surface, COLOR_White, [0, marUp],[winWidth, marUp], 2)
    pygame.draw.line(surface, COLOR_White, [0, marDown], [winWidth, marDown], 2)

    # Vuelca lo dibujado en pantalla
    pygame.display.flip()